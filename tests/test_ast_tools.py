import pytest

from flake8_obey_import_goat.ast_tools import is_import_matches


@pytest.mark.xfail
@pytest.mark.parametrize(
    'import_as_text, rule, expected',
    [
        ('from foo import bar', 'foo.*', True),
        ('from foo import bar', 'foo.bar', True),
        ('from foo import bar', 'foo.fuz', False),
        ('from foo import bar, baz', 'foo.baz', True),
        ('from foo import bar, baz', 'foo.bar', True),
        ('from fuz import bar', 'foo.*', False),
    ],
)
def test_is_import_matches_main_cases(import_as_text, rule, expected, construct_import):
    _import = construct_import(import_as_text)
    assert is_import_matches(rule, _import) == expected
