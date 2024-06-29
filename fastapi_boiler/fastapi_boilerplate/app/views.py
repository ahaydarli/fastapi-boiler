from fastapi import APIRouter

from app.v1 import routers

router = APIRouter()

for r in routers:
    router.include_router(r)
