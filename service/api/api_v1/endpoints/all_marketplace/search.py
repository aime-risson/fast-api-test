from fastapi import APIRouter, Depends
from service.core.models.commun_search_api.Inputs.search import CommunSearchParameters
from service.core.logic.vestiaire_collectif.search_vc import vc_search as SearchVC
from service.core.models.commun_search_api.outputs.search_output import SearchOutput
from service.core.logic.vinted.search_vinted import search as SearchVinted
from service.core.logic.multiple_search.searc_multiple_marketplaces import search_marketplaces as SearchALL
# from typing import List
router = APIRouter()

@router.get("/all_markets/items", tags=["All Marketplaces"], name="Search", response_model=SearchOutput)
def vc_search(search: CommunSearchParameters = Depends(CommunSearchParameters)):
    """
    Lets you search items on vinted:
    * return list of items
    """

    return SearchALL(search)