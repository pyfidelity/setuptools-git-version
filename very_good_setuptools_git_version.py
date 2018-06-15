"""Methods to extract version information from a git repository."""
import subprocess


def get_tag():
    """Return the last tag for the git repository."""
    # another possible option is: 'git tag | sort -V | tail -n1'
    return subprocess.getoutput('git tag --sort=version:refname | tail -n1')


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
    """Parse the `version_format` keyword in a client setup.py script."""
    dist.metadata.version = get_version(template)


# explicitly define the outward facing API of this module
__all__ = [
    get_tag.__name__,
    get_commit_count.__name__,
    get_gitsha.__name__,
    get_version.__name__,
    validate_version_format.__name__,
]
