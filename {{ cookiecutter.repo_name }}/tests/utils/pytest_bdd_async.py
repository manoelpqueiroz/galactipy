"""Allow asynchronous functions to be used with the `pytest-bdd` framework."""

import inspect
from collections.abc import Callable
from functools import wraps


# FYI pytest-bdd does not support async operations natively, this is a workaround
# https://github.com/pytest-dev/pytest-bdd/issues/223
# https://github.com/pytest-dev/pytest-asyncio/issues/195
class AsyncStepConverter:
    """Utility class to convert pytest-bdd async step functions."""

    @staticmethod
    def convert(step_func: Callable) -> Callable:
        """Convert an async step function to a synchronous one."""
        signature = inspect.signature(step_func)
        parameters = list(signature.parameters.values())

        has_event_loop = any(param.name == "event_loop" for param in parameters)

        if not has_event_loop:
            event_loop_param = inspect.Parameter(
                "event_loop", inspect.Parameter.POSITIONAL_OR_KEYWORD
            )
            parameters.append(event_loop_param)
            step_func.__signature__ = signature.replace(parameters=parameters)

        @wraps(step_func)
        def sync_wrapper(*args, **kwargs):
            loop = kwargs["event_loop"] if has_event_loop else kwargs.pop("event_loop")

            return loop.run_until_complete(step_func(*args, **kwargs))

        return sync_wrapper


def async_step(step_func: Callable) -> Callable:
    """Decorator interface for async step function conversion."""
    return AsyncStepConverter.convert(step_func)
