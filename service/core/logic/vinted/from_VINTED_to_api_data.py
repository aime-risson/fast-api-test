from typing import List, Dict
from service.core.models.commun_search_api.outputs.search_output import SearchOutput


def transform_data_vinted(json_items_list: List[Dict] )-> List[SearchOutput] :
    """
    Transforms raw data from vinted api to a commun data structure for the api
    """
    transformed_data = []
    for _item in json_items_list:
        data = {}
        data["id"] = _item["id"]
        data['title'] = _item['title']
        data["price"] = _item["price"]
        data["brand"] = _item["brand_title"]
        data["description"] = ""
        data["platform"] = "VINTED"
        data["country"] = ""
        data["likes"] = _item["favourite_count"]
        data["images"] = [_item["photo"]["url"]]
        data["link"] = _item['url']
        data["condition"] = ""
        data["created_at"] = _item["photo"]["high_resolution"]["timestamp"]
        transformed_data.append(data)

    return {"items": transformed_data}
