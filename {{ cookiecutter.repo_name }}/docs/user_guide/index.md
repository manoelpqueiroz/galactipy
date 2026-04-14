{% raw -%}
---
tags:
  - Section Intros
  - User Guides
---

{% endraw -%}
# User Guide

The User Guide covers all of {{ cookiecutter.project_name }}
by topic area.
Each page introduces a topic
(such as "<!-- RECORD an example of a topic in your application -->")
and discusses
how {{ cookiecutter.project_name }} approaches the problem,
with examples included for clarity.

Users brand new to {{ cookiecutter.project_name }}
should start with [_10 Minutes to {{ cookiecutter.project_name }}_][10min].

For a high level summary
of the {{ cookiecutter.project_name }} fundamentals,
see [_Essential Basic Functionality_][basics].

Further information
on any specific
class, method or function
can be retrieved from the [API Reference][api].

## How to read these guides

In these guides,
you will see either
input code inside clode blocks
such as:

```py
import {{ cookiecutter.package_name }}
{{ cookiecutter.package_name }}.__version__
```

or:

```
In [1]: import {{ cookiecutter.package_name }}

In [2]: {{ cookiecutter.package_name }}.__version__
Out[2]: '0.1.0'
```

The first block is a standard Python input,
whereas the second
(with the `In [1]` guide)
indicates the input is made
inside a [Jupyter Notebook][1].
In a Jupyer Notebook,
the last line is printed
and plots are shown inline.

So:

```
In [3]: a = 1

In [4]: a
Out[4]: 1
```

is equivalent to:

```py
a = 1
print(a)
```

<!-- Anchors -->

[10min]: ./10min.md
[basics]: ./basics.md
[api]: ../reference/index.md

[1]: https://jupyter.org/
