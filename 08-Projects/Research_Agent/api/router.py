from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from models.input_model import ImputModel
from Core.get_reposne import get_response_stream

router = APIRouter()

@router.post("/get_response")
async def get_response_endpoint(input: ImputModel):
    return StreamingResponse(
        get_response_stream(input.question),
        media_type="text/plain"
    )

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.get("/version")
async def version_check():
    return {"version": "1.1.0"}

