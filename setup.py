from setuptools import setup


def README():
    """Return the contents of the README file for this project."""
    with open('README.md') as README_file:
        return README_file.read()


setup(
    name='very-good-setuptools-git-version',
    version='1.0.0',
    url='https://github.com/Kautenja/very-good-setuptools-git-version',
    author='Chritian Kauten',
    author_email='kautencreations@gmail.com',
    description='Automatically set package version from Git.',
    long_description=README(),
    long_description_content_type='text/markdown',
    keywords='setuptools git version-control',
    license='MIT',
    classifiers=[
        'Framework :: Setuptools Plugin',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    py_modules=['very_good_setuptools_git_version'],
    install_requires=[
        'setuptools >= 8.0',
    ],
    entry_points={
        'distutils.setup_keywords': [
            'version_format = very_good_setuptools_git_version:validate_version_format'
        ],
        'console_scripts': [
            'very-good-setuptools-git-version = very_good_setuptools_git_version:get_version'
        ]
    }
)
