from typing import Generator, Tuple

from flake8_obey_import_goat import __version__ as version


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
        lines = raw_imports_data.strip().split('\n')
        forbidden_imports = []
        for line in lines:
            import_from, raw_forbidden_imports = line.split(': ')
            importable, comment = raw_forbidden_imports.split(', ')
            forbidden_imports.append(
                (import_from.strip(), importable, comment),
            )
        cls.forbidden_imports = forbidden_imports

    def run(self) -> Generator[Tuple[int, int, str, type], None, None]:
        pass
