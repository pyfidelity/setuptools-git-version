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
        version_format='{tag}.dev{commitcount}+{gitsha}-{dirty}',
        setup_requires=['setuptools-git-version'],
        ...)

Please ensure that your git repository has at least one `annotated tag <https://git-scm.com/book/en/v2/Git-Basics-Tagging>`_,
as ``setuptools-git-version`` will uses tags to determine your current git version. 

Fields
------
``setuptools-git-version`` provides three fields as options for the ``version_format`` string:

* ``tag``: The latest tag (probably a release version like ``v1.0.3``) in your repository
* ``commitcount``: The number of additional commits on top of this tag (e.g. ``13``)
* ``gitsha``: An abbreviated commit hash of the latest commit in your repository
* ``dirty``: Result of the --dirty git option

Implementation Details
----------------------

``setuptools-git-version`` uses the following git command to obtain commit information:

.. code-block:: bash

    git describe --tags --long --dirty

To ensure that ``setuptools-git-version`` is compatible with your project, please ensure this command runs correctly in
your repository


Changes
-------

1.0.5 - 2019-07-17
++++++++++++++++++

- [feature] added dirty to version_format

1.0.4 - 2016-06-22
++++++++++++++++++

- [feature] allow to build a package using a git-based version without modifying it upfront

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

