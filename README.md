# very-good-setuptools-git-version

*Automatically set package version from Git.* This is a re-release with fixes
from the original [here](https://github.com/pyfidelity/setuptools-git-version).

## Introduction

Instead of hardcoding the package version in ``setup.py`` like:

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
