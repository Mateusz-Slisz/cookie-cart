from dataclasses import dataclass
from typing import Optional


@dataclass
class ItemEntity:
    external_id: str
    name: str = ""
    value: Optional[int] = None
