# Options & Settings

{{ cookiecutter.project_name }} provides configuration files,
located by default at `$XDG_CONFIG_HOME/{{ cookiecutter.project_name }}`,
that fine-tune the application's behaviour.
On this page,
we go through each one of these settings
so users can extract more value
and customise how {{ cookiecutter.project_name }}
looks and feels to them.

Operations related to the config
are handled by the `{{ cookiecutter.repo_name }} config` CLI command
and its subcommands:

??? abstract "Get"

    **`{{ cookiecutter.repo_name }} config get [--path <file>] [--secret | -s] [KEY]`**

    Retrieve a key from the configuration file.
    If no key is provided,
    will return the entire configuration.

    > :fontawesome-solid-border-none:{ .middle }
    > :fontawesome-solid-font:{ .middle }
    > **`KEY`**
    >
    > The configuration key
    > to be retrieved.

    ---

    > :fontawesome-solid-border-none:{ .middle }
    > :fontawesome-solid-folder-tree:{ .middle }
    > **`--path`**
    >
    > Specify
    > a custom configuration file.

    ---

    > :fontawesome-solid-toggle-off:{ .middle }
    > **`--secret` / `-s`**
    >
    > Retrieve configuration
    > from the secret manager instead.

??? success "Set"

    **`{{ cookiecutter.repo_name }} config set [--path <file>] [--secret | -s] KEY VALUE`**

    Store a key in the configuration file.

    > :fontawesome-solid-font:{ .middle }
    > **`KEY`**
    >
    > The configuration key
    > to be retrieved. **[required]**

    ---

    > :fontawesome-solid-font:{ .middle }
    > :fontawesome-solid-hashtag:{ .middle }
    > :fontawesome-solid-sitemap:{ .middle }
    > **`VALUE`**
    >
    > The value to be stored
    > with the key. **[required]**

    ---

    > :fontawesome-solid-border-none:{ .middle }
    > :fontawesome-solid-folder-tree:{ .middle }
    > **`--path`**
    >
    > Specify
    > a custom configuration file.

    ---

    > :fontawesome-solid-toggle-off:{ .middle }
    > **`--secret` / `-s`**
    >
    > Store configuration
    > in the secret manager instead.

??? note "Extend"

    **`{{ cookiecutter.repo_name }} config extend [--path <file>] [--secret | -s] [--create-on-missing | -c] KEY VALUE`**

    Extend an array key in the configuration file.

    > :fontawesome-solid-font:{ .middle }
    > **`KEY`**
    >
    > The configuration key
    > to be extended. **[required]**

    > :fontawesome-solid-font:{ .middle }
    > :fontawesome-solid-hashtag:{ .middle }
    > :fontawesome-solid-sitemap:{ .middle }
    > **`VALUE`**
    >
    > The value to be appended
    > to the key. **[required]**

    > :fontawesome-solid-border-none:{ .middle }
    > :fontawesome-solid-folder-tree:{ .middle }
    > **`--path`**
    >
    > Specify
    > a custom configuration file.

    > :fontawesome-solid-toggle-off:{ .middle }
    > **`--secret`** / **`-s`**
    >
    > Store configuration
    > in the secret manager instead.

    > :fontawesome-solid-toggle-off:{ .middle }
    > **`--create-on-missing`** / **`-c`**
    >
    > Add the provided value
    > in an array
    > if the setting does not exist.
    > Will raise an error
    > otherwise.

??? danger "Unset"

    **`{{ cookiecutter.repo_name }} config unset [--path <file>] [--secret | -s] KEY`**

    Remove a top-level key from the configuration.
    Will not work with deeply nested keys.

    > :fontawesome-solid-font:{ .middle }
    > **`KEY`**
    >
    > The configuration key
    > to be removed. **[required]**

    > :fontawesome-solid-border-none:{ .middle }
    > :fontawesome-solid-folder-tree:{ .middle }
    > **`--path`**
    >
    > Specify
    > a custom configuration file.

    > :fontawesome-solid-toggle-off:{ .middle }
    > **`--secret`** / **`-s`**
    >
    > Retrieve configuration
    > from the secret manager instead.

## Themes

> Configuration key: **`theme`**

The terminal interface theme
can be changed
either temporarily at runtime
or permanently through the config.

At runtime,
users should launch the command palette
with ++ctrl+p++
and select the **Theme** command
to pick one of the available options.

This,
however,
will only change the theme
for the current session.
Once you quit {{ cookiecutter.project_name }}
and relaunch it,
it will revert back
to the default theme.
To permanently change it,
use the **`set`** command
to change the `theme` key
with one of the following options:

<div class="grid cards" markdown>

-   :lucide-sun:{ .middle } [`catppuccin-latte`][latte]

    :lucide-moon:{ .middle } [`catppuccin-mocha`][mocha]

    :lucide-moon:{ .middle } [`dracula`][dracula]

    :lucide-moon:{ .middle } [`flexoki`][flex]

    :lucide-moon:{ .middle } [`gruvbox`][gruv]

    :lucide-moon:{ .middle } [`monokai`][mono]

    :lucide-moon:{ .middle } [`noctis`][noctis]

    :lucide-moon:{ .middle } [`noctis-azureus`][azureus]

    :lucide-moon:{ .middle } [`noctis-bordo`][bordo]

    :lucide-sun:{ .middle } [`noctis-hibernus`][hibernus]

    :lucide-sun:{ .middle } [`noctis-lilac`][lilac]

    :lucide-sun:{ .middle } [`noctis-lux`][lux]

-   :lucide-moon:{ .middle } [`noctis-minimus`][minimus]

    :lucide-moon:{ .middle } [`noctis-uva`][uva]

    :lucide-moon:{ .middle } [`noctis-viola`][viola]

    :lucide-moon:{ .middle } [`nord`][nord]

    :lucide-moon:{ .middle } [`rose-pine`][rose]

    :lucide-sun:{ .middle } [`rose-pine-dawn`][dawn]

    :lucide-moon:{ .middle } [`rose-pine-moon`][moon]

    :lucide-moon:{ .middle } [`solarized-dark`][solard]

    :lucide-sun:{ .middle } [`solarized-light`][solarl]

    :lucide-moon:{ .middle } [`textual-dark`][textuald]

    :lucide-sun:{ .middle } [`textual-light`][textuall]

    :lucide-moon:{ .middle } [`tokyo-night`][tokyo]

</div>

<!-- RECORD additional options as new configuration keys are structured for {{ cookiecutter.project_name }} -->

<!-- Anchors -->

[latte]: ../img/catppuccin-latte.png
[mocha]: ../img/catppuccin-mocha.png
[dracula]: ../img/dracula.png
[flex]: ../img/flexoki.png
[gruv]: ../img/gruvbox.png
[mono]: ../img/monokai.png
[azureus]: ../img/noctis-azureus.png
[bordo]: ../img/noctis-bordo.png
[hibernus]: ../img/noctis-hibernus.png
[lilac]: ../img/noctis-lilac.png
[lux]: ../img/noctis-lux.png
[minimus]: ../img/noctis-minimus.png
[uva]: ../img/noctis-uva.png
[viola]: ../img/noctis-viola.png
[noctis]: ../img/noctis.png
[nord]: ../img/nord.png
[dawn]: ../img/rose-pine-dawn.png
[moon]: ../img/rose-pine-moon.png
[rose]: ../img/rose-pine.png
[solard]: ../img/solarized-dark.png
[solarl]: ../img/solarized-light.png
[textuald]: ../img/textual-dark.png
[textuall]: ../img/textual-light.png
[tokyo]: ../img/tokyo-night.png
