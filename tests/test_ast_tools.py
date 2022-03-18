import pytest

from flake8_obey_import_goat.ast_tools import is_import_matches


@pytest.mark.parametrize(
    'import_as_text, rule, expected',
    [
        ('from foo import bar', '*', True),
        ('from foo import bar', 'foo.*', True),
        ('from foo import bar', 'foo.bar', True),
        ('from foo import bar', 'foo.fuz', False),
        ('from foo import bar, baz', 'foo.baz', True),
        ('from foo import bar, baz', 'foo.bar', True),
        ('from fuz import bar', 'foo.*', False),
        ('from fuz import bar', '*.bar', True),
        ('from fuz import bar', '*.fuz', False),
        ('from foo.fuz import bar', 'foo.*.bar', True),
        ('from foo.fuz import bar', 'foo.*.baz', False),
        ('import foo.fuz.bar', 'foo.*.bar', True),
        ('from foo.fuz import bar', '*.fuz.*', True),
        ('from foo.fuz.bar import baz', '*.fuz.*', True),
        ('from foo.fuz.bar import baz', '*.fuz.bar.*', True),
        ('from foo.fuz import bar', '*.fuz.bar.*', False),
        ('from fuz import bar', 'fuz.bar.*', False),
        ('import foo.fuz.bar', '*.fuz.bar.*', False),
        ('import fuz.bar', 'fuz.bar.*', False),
    ],
)
def test_is_import_matches_main_cases(import_as_text, rule, expected, construct_import):
    _import = construct_import(import_as_text)
    assert is_import_matches(rule, _import) == expected
