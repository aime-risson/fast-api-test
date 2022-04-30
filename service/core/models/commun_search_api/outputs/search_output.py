from pydantic import BaseModel, Field
from typing import List

class Item(BaseModel):
    id: int = Field(..., title="Item id on given platform")
    title: str = Field(..., title="Item title")
    price: float = Field(..., title="Item price")
    brand: str = Field(..., title="Item brand")
    description: str = Field(..., title="Item description")
    platform: str = Field(..., title="Platform where the item was found")
    country: str = Field(..., title="Item's country of origin")
    likes: int = Field(..., title="Number of likes the item got")
    images: List[str] = Field(..., title="List of the item's photos")
    link: str = Field(..., title="Link to article")
    condition: str = Field(..., title="Item condition")
    created_at: int = Field(..., title="Creation timestamp")

class SearchOutput(BaseModel):
    items: List[Item]
