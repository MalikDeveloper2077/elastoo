from fastapi import APIRouter

from app.v1.endpoints.tasks import router as tasks_router


router = APIRouter()
router.include_router(tasks_router, prefix='/tasks', tags=['Tasks'])
