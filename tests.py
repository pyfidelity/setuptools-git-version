from pytest import mark
from version import format_version


@mark.parametrize('git_describe, version', [
    ('v25.6-879-gca0be43', 'v25.6.dev879+ca0be43'),
    ('28-0-gca0be43', '28'),
    ('28.0-0-gca0be43', '28.0'),
    ('28.0-1-gca0be43', '28.0.dev1+ca0be43'),
])
def test_git_describe(git_describe, version):
    fmt = '{tag}.dev{commitcount}+{gitsha}'
    assert format_version(git_describe, fmt) == version
