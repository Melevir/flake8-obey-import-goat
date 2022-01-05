import ast

from flake8_obey_import_goat.custom_types import SomeImport


def extract_imports_from(tree: ast.Module) -> list[SomeImport]:
    return []


def is_import_matches(rule: str, _import: SomeImport) -> bool:
    return False


def extract_path_from(_import: SomeImport) -> str:
    return ''
