# very-good-setuptools-git-version

[![PackageVersion][pypi-version]][pypi-home]
[![PythonVersion][python-version]][python-home]
[![Stable][pypi-status]][pypi-home]
[![Format][pypi-format]][pypi-home]
[![License][pypi-license]](LICENSE)

[pypi-version]: https://badge.fury.io/py/very-good-setuptools-git-version.svg
[pypi-license]: https://img.shields.io/pypi/l/very-good-setuptools-git-version.svg
[pypi-status]: https://img.shields.io/pypi/status/very-good-setuptools-git-version.svg
[pypi-format]: https://img.shields.io/pypi/format/very-good-setuptools-git-version.svg
[pypi-home]: https://badge.fury.io/py/very-good-setuptools-git-version
[python-version]: https://img.shields.io/pypi/pyversions/very-good-setuptools-git-version.svg
[python-home]: https://python.org

Automatically set package version from Git. This is a re-release of
[setuptools-git-version][] with fixes and improvements.

[setuptools-git-version]: https://github.com/pyfidelity/setuptools-git-version

## Introduction

Instead of hard-coding the package version in ``setup.py`` like:

```python
setup(
    name='foobar',
    version='1.0',
    ...
)
```

this package allows to extract it from the underlying Git repository:

```python
setup(
    name='foobar',
    version_format='{tag}.dev{commits}+{sha}',
    setup_requires=['setuptools-git-version'],
    ...
)
```
