from fastapi import APIRouter


router = APIRouter()

class candidato_controller:
    def __init__(self):
        self.service = candidato_service()