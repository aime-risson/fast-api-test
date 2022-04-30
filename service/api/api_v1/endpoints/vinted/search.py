from fastapi import APIRouter, Depends
from service.core.models.vinted.search import VintedSearchParameters
from service.core.logic.vinted.search_vinted import search as SearchVinted
from service.core.models.commun_search_api.outputs.search_output import SearchOutput
from typing import List
router = APIRouter()


@router.get("/vinted/items", tags=["Vinted"], name="Search", response_model=SearchOutput)
def vinted_search(search: VintedSearchParameters = Depends(VintedSearchParameters)):
    """
    Lets you search items on vinted:
    * return list of items
    """
    return SearchVinted(search)



