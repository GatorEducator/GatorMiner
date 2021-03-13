# Contributing Guidelines

Thank you for taking time to contribute to TextMining! This guide will help you
to effectively get stared and contribute to the project.

## Table of Contents

- [Contributing Guidelines](#contributing-guidelines)
  - [Table of Contents](#table-of-contents)
  - [Code of Conduct](#code-of-conduct)
  - [Raise an Issue](#raise-an-issue)
  - [Make a Pull Request](#make-a-pull-request)
  - [Project Overview](#project-overview)
    - [Development Environment](#development-environment)
    - [Contribute with Github Flow Model](#contribute-with-github-flow-model)
    - [Automated Testing](#automated-testing)
*
## Code of Conduct

To build a diverse and inclusive community, we ask that everyone contributing to this project follow the [code of conduct](https://github.com/Allegheny-Ethical-CS/textMining/blob/master/CODE_OF_CONDUCT.md).

## Raise an Issue

If you have a new issue to raise (bug report, feature request, etc.), go ahead and raise it in the [Issue Tracker](https://github.com/Allegheny-Ethical-CS/textMining/issues) (the *Issues* tab on the top of the GitHub repository page)! Please follow the provided issue template and try to fill out the template with **as much detail as you can** when describing the raised issue.

## Make a Pull Request

The development team uses the [GitHub Flow Model](https://guides.github.com/introduction/flow/) to guide our engineering of this tool and we invite you to also follow it as you make a contribution. Once you have made some new changes and want the maintainers to merge them into the project, we encourgae you to go ahead and open a [pull request](https://github.com/Allegheny-Ethical-CS/textMining/pulls) on the GitHub repository. Please follow the provided pull request template and describe the new feature or bug fix that you are proposing with the necessary information. The proposed change should not break the existing test cases or features, as each PR will be checked with our Continuous Integration service (code standard, test suites, etc.) We hope your proposed change is well-documented and highly recommend you to provide tests along with the PR if you are making a code contribution.

## Project Overview

### Development Environment

In order to contribute code or documentation to the project, the project maintainers suggest installing the release of Python versions above 3.6. In addition to installing `Git` to access the project's GitHub repository, you should also install `Pipenv` for its support of package and virtual environment management. Once you have installed `Git` and `Pipenv`, you can type the following command in your terminal window to clone the GitHub repository:

```sh
git clone git@github.com:Allegheny-Mozilla-Fellows/textMining.git
```

You can install and set up the development dependencies with `Pipenv` as follows:

```bash
pipenv install --dev --skip-lock
```

### Contribute with Github Flow Model

If you are already a collaborator on the project and would like to contribute a new feature or bug fix, you should create and publish your new branch via the following command. Substitute the name of your feature/branch for the word feature-name.

```bash
git checkout -b feature-name
git checkout master
git push -u origin feature-name
```

If you are not yet a collaborator on this project, then we recommend you to first fork the repository, add your new feature, document and test it as appropriate.

### Automated Testing

You can run the test suites locally as follows:

```ba
pipenv run pytest
```

It might also be helpful for you to run the following command to see the test
coverage and lines that are currently not tested:

```bash
pipenv run pytest --cov-config pytest.cov --cov --cov-report term-missing
```
