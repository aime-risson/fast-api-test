from fastapi import APIRouter
from .endpoints.hello import router as triage_router
from .endpoints.vinted.search import router as vinted_search



router = APIRouter()
router.include_router(triage_router)
router.include_router(vinted_search)
