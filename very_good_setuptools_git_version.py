"""Methods to extract version information from a git repository."""
import subprocess


def get_tag():
    """Return the last tag for the git repository."""
    return subprocess.getoutput('git tag | tail -n1')


def get_commit_count():
    """Return the number of commits since the last tag."""
    return subprocess.getoutput('git rev-list --all --count')


def get_gitsha():
    """Return the sha key of HEAD."""
    return subprocess.getoutput('git rev-parse HEAD')


def get_version(template='{tag}.{commits}+{sha}'):
    """
    Return the full git version using the given template.

    Args:
        template: the string format template to use. It can use these keys:
            {tag}: the tag from the git repository
            {commits}: the number of commits since the last tag
            {sha}: the sha key of HEAD

    Returns:
        the formatted version for the git repository

    """
    tag = get_tag()
    commits = get_commit_count()
    sha = get_gitsha()

    return template.format(tag=tag, commits=commits, sha=sha)


def validate_version_format(dist, _, template):
    """Validate the `version_format` template in client setup.py."""
    dist.metadata.version = get_version(template)


# if __name__ == "__main__":
#     # determine version from git
#     version = get_version()

#     # monkey-patch `setuptools.setup` to inject the git version
#     import setuptools
#     original_setup = setuptools.setup

#     def setup(version=None, *args, **kw):
#         return original_setup(version=version, *args, **kw)

#     setuptools.setup = setup

#     # import the package's setup module
#     import setup
