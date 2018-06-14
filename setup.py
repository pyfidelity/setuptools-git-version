from setuptools import setup


setup(
    name='very-good-setuptools-git-version',
    version='1.1.0',
    url='https://github.com/Kautenja/very-good-setuptools-git-version',
    author='Chritian Kauten',
    author_email='kautencreations@gmail.com',
    description='Automatically set package version from Git.',
    license='MIT',
    classifiers=[
        'Framework :: Setuptools Plugin',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
    py_modules=['very_good_setuptools_git_version'],
    install_requires=[
        'setuptools >= 8.0',
    ],
    entry_points="""
        [distutils.setup_keywords]
        version_format = very_good_setuptools_git_version:validate_version_format
        [console_scripts]
        very-good-setuptools-git-version = very_good_setuptools_git_version:get_version
    """,
)
