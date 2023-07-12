"""Routers."""
from fastapi import APIRouter
from .endpoints.get_coin import router as router_get_coin
from .endpoints.register import router as router_register
from .endpoints.fetch import router as router_fetch
from .endpoints.delete import router as router_delete
from .endpoints.update import router as router_update

router = APIRouter()
router.include_router(router_get_coin)
router.include_router(router_register)
router.include_router(router_fetch)
router.include_router(router_delete)
router.include_router(router_update)
