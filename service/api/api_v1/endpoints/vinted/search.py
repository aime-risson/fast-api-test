from fastapi import APIRouter, Depends
from pyVinted import Vinted, requester
from service.core.models.vinted.search import VintedSearchParameters

from requests_ip_rotator import ApiGateway

gateway = ApiGateway(
    "https://www.vinted.fr",
    ["eu-west-1", "eu-west-2", "eu-west-3"],
)
# ["eu-west-1", "eu-west-2", "eu-west-3", "eu-north-1", "eu-central-1"],
gateway.start()

router = APIRouter()
vinted = Vinted()
requester.setCookies()
requester.session.mount("https://www.vinted.fr", gateway)

to_remove = ["is_favourite","favourite_group_id","badge","conversion","service_fee","user", "search_tracking_params","view_count"]
@router.get("/vinted/items", tags=["Vinted"], name="Search")
def vinted_search(search: VintedSearchParameters = Depends(VintedSearchParameters)):
    """
    Lets you search items on vinted:
    * return list of items
    """

    items = requester.get("https://www.vinted.fr/api/v2/catalog/items",params=vars(search))
    if items.status_code == 200:
        items = items.json()["items"]
        for _item in items:
            for _to_remove in to_remove:
                _item.pop(_to_remove)

        return {"items": items}
    else:
        requester.session.adapters.pop("https://www.vinted.fr")
        requester.setCookies()
        return {"statusCode": 500}

