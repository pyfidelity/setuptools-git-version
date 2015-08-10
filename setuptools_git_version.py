from pkg_resources import get_distribution
from distutils.errors import DistutilsSetupError
from subprocess import check_output


command = 'git describe --tags --long --dirty'


def validate_version_format(dist, attr, value):
    if dist.metadata.version:
        # Probably called by write_version_files already
        return
    try:
        version = check_output(command.split()).decode('utf-8').strip()
    except:
        version = get_distribution(dist.get_name()).version
    else:
        version = format_version(version=version, fmt=value)
    dist.metadata.version = version


def write_version_files(dist, attr, value):
    """Write the version in one or more files

    If file ends in __version__.py, write: "__version__ = 'VERSION'", else just
    dump the version in the file.

    Only change files if it would be different
    """
    if not dist.metadata.version:
        if dist.version_format:
            # Force evaluation of version
            validate_version_format(dist, 'version_format', dist.version_format)
        else:
            raise DistutilsSetupError("'version_format' must be defined for %r to work" % attr)

    if isinstance(value, basestring):
        value = [value, ]
    for path in value:
        if path.endswith('__version__.py'):
            content = "__version__ = %r\n" % dist.metadata.version
        else:
            content = dist.metadata.version
        overwrite = False
        try:
            with open(path) as reader:
                current_content = reader.read()
            if current_content != content:
                overwrite = True
        except:
            overwrite = True
        if overwrite:
            with open(path, 'w') as writer:
                writer.write(content)


def format_version(version, fmt):
    parts = version.split('-')
    assert len(parts) in (3, 4)
    dirty = len(parts) == 4
    tag, count, sha = parts[:3]
    if count == '0' and not dirty:
        return tag
    return fmt.format(tag=tag, commitcount=count, gitsha=sha.lstrip('g'))
