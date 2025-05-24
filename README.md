# Python Environment with Poetry

## One-time Setup

### For local machine

```bash
# Install once on your computer
brew install poetry direnv
echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc && source ~/.zshrc  # Install directory watcher that auto-activates when you cd into project
```

### For Project

```bash
# Run in project directory
poetry install

# Setup auto-activation
echo 'source .venv/bin/activate' > .envrc               # Activates venv when you cd into directory (auto-deactivates when you leave)
echo 'export PATH="$PWD/.venv/bin:$PATH"' >> .envrc     # Ensures tools run directly without poetry run prefix
direnv allow .                                          # Security measure: explicitly approve this .envrc script
```

## Day-to-day Workflow

### Using Tools (just work after auto-activation)

```bash
python script.py
black .       # Format code (like prettier)
isort .       # Organize imports
flake8        # Lint code (like eslint)

# Run tests
pytest        # Run all tests
pytest -v     # Verbose output
pytest -k "test_name"  # Run specific test
pytest --cov  # Run with coverage report
```

### Managing Packages

```bash
# Add packages
poetry add requests              # Regular dependency (like npm install)
poetry add --group dev pytest    # Dev dependency (like npm install --save-dev)

# Remove packages
poetry remove requests

# Update packages
poetry update

# Show packages
poetry show                      # List all packages (like npm list)
```

## Troubleshooting

```bash
# If things break, try these:
poetry cache clear --all pypi     # Clear cache
poetry env remove --all           # Reset environment
rm poetry.lock && poetry install  # Start fresh
```

## Comparison: Pip Workflow vs Poetry

| Feature                   | Traditional Pip Workflow                                       | Poetry Workflow                                                 |
| ------------------------- | -------------------------------------------------------------- | --------------------------------------------------------------- |
| **Dependency Management** | `requirements.txt` file, manually maintained                   | `pyproject.toml` + `poetry.lock` (automatically managed)        |
| **Environment Creation**  | `python -m venv venv` (separate step)                          | `poetry install` (creates `.venv` automatically)                |
| **Activation**            | `source venv/bin/activate` (manual every time)                 | Auto-activates with direnv when entering directory              |
| **Adding Packages**       | `pip install <package>` then `pip freeze > requirements.txt`   | `poetry add <package>` (automatically updates files)            |
| **Dev Dependencies**      | Mixed with production deps or in separate requirements-dev.txt | `poetry add --group dev <package>` (cleanly separated)          |
| **Version Resolution**    | Manual conflict resolution                                     | Sophisticated dependency resolver                               |
| **Configuration**         | Multiple files (`.flake8`, etc.)                               | Everything in `pyproject.toml`                                  |
| **Command Usage**         | Needs manual env activation for each terminal                  | Tools work directly (`black .` instead of `poetry run black .`) |

## Package Management: Pip vs Poetry

| Feature                 | Pip                                                          | Poetry                                                     |
| ----------------------- | ------------------------------------------------------------ | ---------------------------------------------------------- |
| **Config File**         | `requirements.txt` (flat list)                               | `pyproject.toml` (structured with sections)                |
| **Lock File**           | None built-in (requires `pip-tools` for `requirements.lock`) | `poetry.lock` (automatically generated)                    |
| **Package Creation**    | `setup.py` + `setup.cfg` (imperative)                        | `pyproject.toml` (declarative)                             |
| **Publishing**          | `python setup.py sdist bdist_wheel` + `twine upload`         | `poetry build` + `poetry publish`                          |
| **Git Dependencies**    | `git+https://github.com/user/repo.git@tag#egg=package`       | `{package = {git = "https://github.com/user/repo.git"}}`   |
| **Cross-system Usage**  | Add git URL to `requirements.txt` to use Poetry packages     | `poetry export -f requirements.txt` to generate for pip    |
| **Dev Dependencies**    | Separate file or mixed with production deps                  | Separate sections in same file (`[tool.poetry.group.dev]`) |
| **Package Building**    | Multi-step process with setuptools                           | One command: `poetry build`                                |
| **Private Packages**    | Reference private Git repos with auth in URL                 | Same, plus better support for private repositories         |
| **Version Constraints** | Basic constraints (`==`, `>=`)                               | Extended constraints (`^`, `~`, `*`, etc.)                 |
| **Package Format**      | Works with traditional and PEP 517 packages                  | Fully PEP 517 compliant                                    |
