# TUI Reference

{{ cookiecutter.project_name }} uses [Textual][1]
to provide a terminal user interface.
The basic structure of the `tui` package
is as follows:

```
tui/
├── components
│   ├── component_1.md
│   ├── component_2.md
⋮    ⋮
│   └── component_n.md
├── css
│   ├── stylesheet_1.tcss
│   ├── stylesheet_2.tcss
⋮    ⋮
│   └── stylesheet_n.tcss
├── __init__.py
├── main_window.py
└── themes.py
```

- [`components/`][2] stores
  the individual Textual widgets
  for the TUI;
- [`css/`][3] stores
  the different [Textual CSS][4] files
  that fine-tune
  how certain elements are displayed
  and behave
  when the application is running;
- [`main_window.py`][5]
  collects all components
  and implements the top-level class
  to run the application;
- [`themes.py`][6] defines
  the several color schemes
  that will be provided to the user
  besides Textual's defaults.

<!-- Anchors -->

[1]: https://textual.textualize.io/
[2]: {{ cookiecutter.__scm_link_url }}/tree/master/{{ cookiecutter.package_name }}/tui/components
[3]: {{ cookiecutter.__scm_link_url }}/tree/master/{{ cookiecutter.package_name }}/tui/css
[4]: https://textual.textualize.io/guide/CSS/
[5]: {{ cookiecutter.__scm_link_url }}/blob/master/{{ cookiecutter.package_name }}/tui/main_window.py
[6]: {{ cookiecutter.__scm_link_url }}/blob/master/{{ cookiecutter.package_name }}/tui/themes.py
