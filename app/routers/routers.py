from fastapi import APIRouter

from routers.controllers import candidate_controller

api_router = APIRouter()
api_router.include_router(candidate_controller.router)