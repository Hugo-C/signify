import hashlib
from typing import Callable

from typing_extensions import TypeAlias

HashFunction: TypeAlias = Callable[[], "hashlib._Hash"]
