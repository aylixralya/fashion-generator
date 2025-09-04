"""
models.py
Datenmodelle und Validierung für Fashion Generator.
"""
from pydantic import BaseModel, validator
from enum import Enum
from typing import Optional

class Category(str, Enum):
    dress = "dress"
    shirt = "shirt"
    pants = "pants"
    accessory = "accessory"

class FashionItem(BaseModel):
    style: str
    category: Category
    size: str
    color: str
    pattern: Optional[str] = None

    @validator('size')
    def size_must_be_valid(cls, v):
        if v not in ['XS', 'S', 'M', 'L', 'XL']:
            raise ValueError('Ungültige Größe')
        return v

    def validate(self):
        self.__validate__()

    def serialize(self) -> dict:
        return self.dict()
