from pydantic import BaseModel, Field
from typing import Optional

class VintedSearchParameters:
    def __init__(self, search_text: Optional[str] = None, per_page: Optional[int] = 24):
        self.search_text = search_text,
        self.per_page = per_page

