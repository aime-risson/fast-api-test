from fastapi import APIRouter, Depends
from pyVinted import Vinted, requester
from service.core.models.commun_search_api.Inputs.search import CommunSearchParameters
from service.core.logic.vestiaire_collectif.search_vc import vc_search as SearchVC
from service.core.logic.vinted.search_vinted import search as SearchVINTED
from service.core.models.vinted.search import VintedSearchParameters

#from ..from_VINTED_to_api_data import transform_data_vinted
from requests_ip_rotator import ApiGateway

def search_marketplaces(search: CommunSearchParameters = Depends(CommunSearchParameters)):
    data = []
    if "VC" in search.marketplaces:
        vc_items = SearchVC(search_text=search.search_text, number_of_items=search.per_page//len(search.marketplaces))
        data.append(vc_items)

    if "VINTED" in search.marketplaces:
        v_search = VintedSearchParameters(search_text=search.search_text, per_page=search.per_page // len(search.marketplaces))

        vinted_items = SearchVINTED(v_search)
        data.append(vinted_items)

    to_return = {"items": []}
    for list_item in data:
        for item in list_item["items"]:
            to_return["items"].append(item)
    print(to_return["items"])
    return to_return
