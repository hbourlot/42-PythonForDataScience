# ex09 - Package and distribution project

This exercise focuses on creating a Python package, configuring packaging metadata, and preparing a distributable project structure.

## Project structure

- `ft_package/`: package source code
- `pyproject.toml`: package configuration for build tools
- `dist/`: generated distribution artifacts
- `LICENSE`: project license

## Objective

The goal is to understand how Python packages are built and distributed using modern packaging tools such as `pyproject.toml` and standard setuptools configuration.

## Main skills practiced

- packaging a Python project
- creating a reusable package layout
- configuring metadata and dependencies
- building source and wheel distributions

## Typical usage

From the project root, you can install or build the package with tools such as:

```bash
python3 -m pip install .
python3 -m build
```

## Notes

This exercise is part of the 42 Python for Data Science piscine and is designed to introduce the basics of Python package distribution and project organization.
