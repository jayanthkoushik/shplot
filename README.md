# pyseed
Template repository for Python projects.

## Usage
Use the GitHub interface to create a new repository with the template. Then, follow the steps below to initialize the project.

1. Replace templates (all template names are suffixed with `_TEMPLATE`).
   + Rename `mainpackage_TEMPLATE` folder.
   + Replace `year_TEMPLATE` and `author_TEMPLATE` in file `LICENSE`.
   + Update `pyproject.toml`:
     + Replace `project_TEMPLATE` in `name = ...` with the project name.
     + Replace `description_TEMPLATE` with the project description.
     + Replace `author_TEMPLATE` and `email_TEMPLATE` in `authors = ...`, and add additional authors if present.
     + Replace `repo_TEMPLATE` with the project repository URL.
     + Replace `mainpackage_TEMPLATE` in `packages = ...` with the folder's new name.
     + [Optional] Uncomment `keywords = ...` and add project keywords.
     + [Optional] Add additional trove classifiers in `classifiers = ...`.

2. Setup workflows.
   + Delete unneeded workflows from `.github/workflows`:
     + `github-release` creates GitHub releases when tags of the form `v*` are pushed. If keeping this workflow, create a GitHub token for `conventional-github-releaser`, and create a GitHub secret named `CONVENTIONAL_GITHUB_RELEASER_TOKEN` with this token.
     + `pypi-publish` publishes new releases (tagged `v*`) of the project to PyPI. If keeping this workflow, create `PYPI_TOKEN` GitHub secret with the PyPI token for the project.
     + `tests-run` runs unittests inside the `tests` folder on every code changing push.

3. Set up environment.
   + Ensure the following are installed:
     + [python >= v3.8](https://www.python.org/downloads/).
     + [poetry >= v1.0](https://python-poetry.org/docs/#installation).
     + [poetry-dynamic-versioning](https://github.com/mtkennerly/poetry-dynamic-versioning)
     + [tox](https://github.com/tox-dev/tox)
     + [npm >= v5.2](https://nodejs.org/en/download/).
   + Create Python virtual env. If the minimum version needed by the project differs from the specification inside `pyproject.toml`, update it. Also update `python-version: ...` in the `pypi-publish`, and `tests-run` workflows. And update the `env_list` in `tox.ini`.
   + Add dependencies to `pyproject.toml`.
   + If working with jupyter notebooks, add `extras = ["jupyter"]` to the dependency specification for `black` inside `pyproject.toml`.
   + Install basic dependencies: `poetry install`. If the generated lock file should be pushed to the repo, remove the `poetry.lock` line from `.gitignore`.
   + Install git hooks: `pre-commit install -t pre-commit -t commit-msg`.

### Workflow
After initial setup, the workflow consists of these steps.

1. Code.
   + Use [Google's style guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) for docstrings.
     + Enclose inline literals in `, and code blocks in ```.
     + [Sphinx](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#module-sphinx.ext.napoleon) will automatically generate documentation using the docstrings.
     + To manually generate docs, run `docs/make.sh`.
   + Write unit tests in files named `test_*`, and put them in the `tests` folder
   + Remove `py.typed` in the package folder if not providing type hints

2. Commit.
   + Follow the [conventional commits specification](https://www.conventionalcommits.org/en/v1.0.0/) for commit messages.
   + Committing will trigger the pre-commit hooks, which will, among other things, lint and format the code, and generate documentation.
   + If any of the hooks fails, the commit will fail--fix the issues, `git add` the modified files, and commit again.
   + [Optional] Push to trigger GitHub workflows.

3. Release a new version of the project with `./release.sh`.
   + This will bump the version, generate a changelog, and push the changes with a new tag.
   + Versions are managed automatically based on commit messages, and version numbers don't need to be manually edited anywhere.
   + For the first release, run `./release.sh -r 1.0.0 --skip.changelog` to create a `v1.0.0` release with no changelog.
