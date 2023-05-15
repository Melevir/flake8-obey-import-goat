# flake8-obey-import-goat

An extension for flake8 that forbids some imports statements
in some modules.

**Important**: this project is developed using DDD, so some of the docs
can not exists. Stay tuned :)

## Installation

```terminal
pip install flake8-obey-import-goat
```

## Example

```python
# foo.py
from datetime import datetime
from typing import Optional

def foo():
    pass


# users/bar.py
from foo import foo


# users/domain.py
def foo():
    pass


# users/implementation.py
from users.domain import foo


# orders/implementation.py
from users.domain import foo
```

```
# setup.cfg
[flake8]
forbidden-imports =
    *: datetime.datetime, stdlib modules should be imported as a module
    *: typing.Optional, we use T | None instead of Optional[T]
    users.*: foo.*, users module should not use foo module
    *.implementation.*: *.domain.*, implementation layer should not use domain layer
```

Usage:

```terminal
$ flake8 test.py
foo.py:1:1: OIG001 datetime.datetime is forbidden, since stdlib modules should be imported as a module.
foo.py:2:1: OIG001 typing.Optional is forbidden, since we use T | None instead of Optional[T].
users/bar.py:1:1: OIG001 foo.foo import is forbidden is forbidden, since users module should not use foo module.
users/implementation.py:1:1: OIG001 *.domain.* import is forbidden is forbidden, since implementation layer should not use domain layer.
orders/implementation.py:1:1: OIG001 *.domain.* import is forbidden is forbidden, since implementation layer should not use domain layer.

```

Tested on Python 3.8+ and flake8 4.0+.

## Error codes

| Error code |                     Description          |
|:----------:|:----------------------------------------:|
|   OIG001   | importable is forbidden, since reason |
