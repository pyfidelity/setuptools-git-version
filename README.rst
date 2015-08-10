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


Writing the version in a python file
------------------------------------

If you also want it in a readily accessible files:

.. code-block:: python

    setup(
        name='foobar',
        version_format='{tag}.dev{commitcount}+{gitsha}',
        version_files='foobar/__version__.py'
        setup_requires=['setuptools-git-version'],
        ...)

For this to work, do the following:

.. code-block:: bash

    $ echo foobar/__version__.py >> .gitignore

Then add this to your __init__.py:

.. code-block:: python

    try:
        from __version__ import __version__
    except:
        __version__ = 'notset; run setup.py'

Now, everytime you run setuptools, it will update the __version__.py file.

And you can get the version like this:

.. code-block:: python

    >>> import foobar
    >>> print foobar.__version


Changes
-------

1.0.4 - 2015-08-10
++++++++++++++++++

- [feature] add version_files

1.0.3 - 2015-04-23
++++++++++++++++++

- [bugfix] rename module to avoid import conflicts


1.0.2 - 2015-04-14
++++++++++++++++++

- [bugfix] make it work with Python 3(.4)


1.0.1 - 2015-04-14
++++++++++++++++++

- brownbag release


1.0 - 2015-04-10
++++++++++++++++

- initial public release

