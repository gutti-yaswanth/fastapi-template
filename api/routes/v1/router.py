from fastapi import APIRouter
from api.routes.v1.users import router as user_router
from api.routes.v1.health import router as health_router

router = APIRouter(prefix="/api/v1")

router.include_router(user_router)
router.include_router(health_router)
