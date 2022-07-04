from fastapi import APIRouter

from app.v1.endpoints.tasks import router as users_router


router = APIRouter()
router.include_router(users_router, prefix='/tasks', tags=['Tasks'])
