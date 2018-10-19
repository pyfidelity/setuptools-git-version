from pkg_resources import get_distribution
from subprocess import check_output


command = 'git describe --tags --long --dirty'
fmt = '{tag}.{commitcount}+{gitsha}'


def validate_version_format(dist, attr, value):
    try:
        version = check_output(command.split()).decode('utf-8').strip()
    except:
        version = get_distribution(dist.get_name()).version
    else:
        version = format_version(version=version, fmt=value)
    dist.metadata.version = version


def format_version(version, fmt=fmt):
    dirty = False
    parts = version.split('-')
    sha = parts.pop()
    if sha == 'dirty':
        dirty = True
        sha = parts.pop()
    count = parts.pop()
    tag = '-'.join(parts)
    if count == '0' and not dirty:
        return tag
    return fmt.format(tag=tag, commitcount=count, gitsha=sha.lstrip('g'))


def get_git_version():
    git_version = check_output(command.split()).decode('utf-8').strip()
    return format_version(version=git_version)


if __name__ == "__main__":
    # determine version from git
    git_version = get_git_version()

    # monkey-patch `setuptools.setup` to inject the git version
    import setuptools
    original_setup = setuptools.setup

    def setup(version=None, *args, **kw):
        return original_setup(version=git_version, *args, **kw)

    setuptools.setup = setup

    # import the packages's setup module
    import setup
