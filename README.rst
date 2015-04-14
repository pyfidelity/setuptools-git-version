setuptools-git-version
======================

*Automatically set package version from Git.*


Introduction
------------

Instead of hardcoding the package version in ``setup.py`` like:

.. code-block:: python

    setup(
        name='foobar',
        version='1.0',
        ...)

this package allows to extract it from the underlying Git repository:

.. code-block:: python

    setup(
        name='foobar',
        version_format='{tag}.dev{commitcount}+{gitsha}',
        setup_requires=['setuptools-git-version'],
        ...)


Changes
-------

1.0.1 - 2015-04-14
++++++++++++++++++

- [bugfix] make it work with Python 3(.4)


1.0 2015-04-10
++++++++++++++

- initial public release

