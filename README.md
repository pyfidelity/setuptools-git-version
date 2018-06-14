# setuptools-git-version

*Automatically set package version from Git.*

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


## Changes

### 1.0.4 - 2016-06-22

- [feature] allow to build a package using a git-based version without modifying it upfront

### 1.0.3 - 2015-04-23

- [bugfix] rename module to avoid import conflicts

### 1.0.2 - 2015-04-14

- [bugfix] make it work with Python 3(.4)

### 1.0.1 - 2015-04-14

- brownbag release

### 1.0 - 2015-04-10

- initial public release
