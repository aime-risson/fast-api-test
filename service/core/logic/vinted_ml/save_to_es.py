from elasticsearch import Elasticsearch
from pydantic import BaseModel
from fastapi import Depends
from pyVinted import Vinted, requester
import re

es = Elasticsearch(
    "https://es.vitalert.fr:443",
    basic_auth=("elastic", "virajElastic"),
    verify_certs=False,
)

ML_INDEX = "vinted_item_ml_data"
class VintedMlInput(BaseModel):
    item_url: str
    should_buy: bool

v = Vinted()
requester.setCookies()

item_id_re_expression = "(?<=\/)([0-9])+(?=-)"

def save_data(data: VintedMlInput = Depends(VintedMlInput)):

    item_id = re.search(item_id_re_expression, data.item_url).group(0)
    print(item_id)
    item = requester.get(f"https://www.vinted.fr/api/v2/items/{item_id}").json()["item"]
    item["should_buy"] = data.should_buy
    es.update(index=ML_INDEX, id=item_id , doc=item, doc_as_upsert=True)
