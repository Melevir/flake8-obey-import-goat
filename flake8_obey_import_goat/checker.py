import collections
from typing import Generator, Tuple

from flake8_obey_import_goat import __version__ as version
from flake8_obey_import_goat.ast_tools import (
    extract_imports_from, is_import_matches,
)
from flake8_obey_import_goat.rules import collect_rules_for


class ImportsChecker:
    name = 'flake8-obey-import-goat'
    version = version
    forbidden_imports = None

    def __init__(self, tree, filename: str):
        self.filename = filename
        self.tree = tree

    @classmethod
    def add_options(cls, parser) -> None:
        parser.add_option(
            '--forbidden-imports',
            parse_from_config=True,
        )

    @classmethod
    def parse_options(cls, options) -> None:
        raw_imports_data = options.forbidden_imports
        if not raw_imports_data:
            return
        lines = raw_imports_data.strip().split('\n')
        forbidden_imports = collections.defaultdict(list)
        for line in lines:
            import_from, raw_forbidden_imports = line.split(': ')
            importable, comment = raw_forbidden_imports.split(', ')
            forbidden_imports[import_from.strip()].append(
                (importable, comment),
            )
        cls.forbidden_imports = dict(forbidden_imports)

    def run(self) -> Generator[Tuple[int, int, str, type], None, None]:
        if not self.forbidden_imports:
            return
        matching_rules = collect_rules_for(self.filename, all_rules=self.forbidden_imports)
        if matching_rules:
            all_imports = extract_imports_from(self.tree)
            for _import in all_imports:
                for rule, comment in matching_rules:
                    if is_import_matches(rule, _import):
                        error_text = f'OIG001 {rule} import is forbidden, since {comment}.'
                        yield _import.lineno, _import.col_offset, error_text, type(self)
                        break
