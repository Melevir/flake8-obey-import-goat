import ast
from typing import List

from flake8_obey_import_goat.custom_types import SomeImport
from flake8_obey_import_goat.rules import is_rule_matched


def extract_imports_from(tree: ast.Module) -> List[SomeImport]:
    return [
        n for n in ast.walk(tree)
        if isinstance(n, (ast.ImportFrom, ast.Import))
    ]


def is_import_matches(rule: str, _import: SomeImport) -> bool:
    importables = extract_importables_from(_import)
    return any(is_rule_matched(importable, rule) for importable in importables)


def extract_importables_from(_import: SomeImport) -> List[str]:
    if isinstance(_import, ast.ImportFrom):
        return [f'{_import.module}.{n.name}' for n in _import.names]
    else:
        return [n.name for n in _import.names]
