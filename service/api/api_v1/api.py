from fastapi import APIRouter
from .endpoints.hello import router as triage_router
from .endpoints.vinted.search import router as vinted_search
from .endpoints.vestiaire_collectif.search import router as vc_search
from .endpoints.all_marketplace.search import router as all_search

router = APIRouter()
#router.include_router(triage_router)
router.include_router(vinted_search)
router.include_router(vc_search)
router.include_router(all_search)
