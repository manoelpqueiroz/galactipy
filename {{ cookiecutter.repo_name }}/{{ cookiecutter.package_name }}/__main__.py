from {{ cookiecutter.package_name }}.cli.root_command import app

app(prog_name="{{ cookiecutter.repo_name }}-mod")
