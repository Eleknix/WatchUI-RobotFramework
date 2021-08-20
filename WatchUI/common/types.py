'''Type aliases are here.
'''

from typing import Any, Literal, Union
from pathlib import Path

ImageFormat = Literal["png", "jpg"]
CustomPath = Union[str, Path]
Unknown = Any
RFLibraries = Literal["selenium", "playwright"]