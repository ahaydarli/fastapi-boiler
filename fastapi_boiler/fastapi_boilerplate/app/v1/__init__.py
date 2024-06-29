from fastapi import APIRouter
from .health.router import router as health_router

g = globals().copy()
routers = [obj for name, obj in g.items() if isinstance(obj, APIRouter)]
