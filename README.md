![testing](https://github.com/wsad1/learn_actions/actions/testing.yml/badge.svg)
# learn_actions
A small repository that uses github actions for CI.

## Setting up for development
To install in develop mode create a new python environment and run.
```
python setup.py develop
```
This will symlink all the python files from the current source tree into python.  

Run the entire test suite with.
```python setup.py test```

## Github actions
`.github/workflow` contains two yamls. `testing.yml` runs this packages test-suite. `linting.yml` runs flake8.
Read [this](https://docs.github.com/en/actions/guides/building-and-testing-python) for a detailed explanation of setting up CI workflows for a python project.
