from toolkit import __author__, __author_email__, __version__

BASE_CONTEXT = {
    "author": __author__,
    "author_email": __author_email__,
    "github_username": "fujiawei-dev",
    "pypi_username": "fujiawei",
    "version": __version__,
}

COOKIECUTTER_CONTEXT = {"_new_lines": "\n"}

USER_INPUT_CONTEXT = {
    "project_short_description": "A short description of your project.",
}
