from pkg_resources import get_distribution
from subprocess import check_output


command = 'git describe --tags --long --dirty'


def validate_version_format(dist, attr, value):
    try:
        version = check_output(command.split()).strip()
    except:
        version = get_distribution(dist.get_name()).version
    else:
        version = format_version(version=version, fmt=value)
    dist.metadata.version = version


def format_version(version, fmt):
    parts = version.split('-')
    assert len(parts) in (3, 4)
    dirty = len(parts) == 4
    tag, count, sha = parts[:3]
    if count == '0' and not dirty:
        return tag
    return fmt.format(tag=tag, commitcount=count, gitsha=sha.lstrip('g'))
