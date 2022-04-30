from pydantic import BaseModel, Field
from typing import Optional, List
from fastapi import Query

class CommunSearchParameters:
    def __init__(self, marketplaces: Optional[List[str]] = Query(None), search_text: Optional[str] = None, per_page: Optional[int] = 24):
        self.search_text = search_text,
        self.per_page = per_page
        self.marketplaces = marketplaces