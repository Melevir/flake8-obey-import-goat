import ast

import pytest


@pytest.fixture
def construct_import():
    def import_constructor(import_as_text):
        return ast.parse(import_as_text).body[0]
    return import_constructor


@pytest.fixture
def all_rules():
    return {
        'a.*': [('a', '')],
        '*.bar': [('b', '')],
        '*.fuz.*': [('f', '')],
    }
