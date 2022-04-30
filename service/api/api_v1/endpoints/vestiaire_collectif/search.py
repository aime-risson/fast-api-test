from fastapi import APIRouter, Depends
from service.core.models.vinted.search import VintedSearchParameters
from service.core.logic.vestiaire_collectif.search_vc import vc_search as SearchVC
from service.core.models.commun_search_api.outputs.search_output import SearchOutput

# from typing import List
router = APIRouter()

@router.get("/vestiaire/items", tags=["Vestiaire Collectif"], name="Search", response_model=SearchOutput)
def vc_search(search: VintedSearchParameters = Depends(VintedSearchParameters)):
    """
    Lets you search items on vinted:
    * return list of items
    """
    return SearchVC(search_text=search.search_text, number_of_items=search.per_page)