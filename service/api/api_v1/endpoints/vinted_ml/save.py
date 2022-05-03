from fastapi import APIRouter, Depends
from service.core.logic.vinted_ml.save_to_es import save_data
from service.core.models.commun_search_api.outputs.search_output import SearchOutput
from typing import List
from pydantic import BaseModel

router = APIRouter()

class VintedMlInput(BaseModel):
    item_url: str
    should_buy: bool


@router.post("/vinted-ml/save", tags=["Vinted-ML"], name="Add item to db")
def vinted_search(mlData: VintedMlInput = Depends(VintedMlInput)):
    save_data(mlData)
    return {"statusCode": 200}



