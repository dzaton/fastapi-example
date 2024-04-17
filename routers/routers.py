from fastapi import APIRouter

from routers.controllers import candidato_controller

api_router = APIRouter()
api_router.include_router(candidato_controller.r)