from fastapi import APIRouter
from models.request_model import RequestModel
from models.response_model import ResponseModel
from core.prompt import generate_prompt

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok"}

# connect index.html to the root endpoint
@router.get("/")
async def read_root():
    return {"message": "Welcome to the AI Prompt Generator API. Use the /generate_prompt endpoint to create professional prompts."}

@router.post("/generate_prompt", response_model=ResponseModel)
async def generate_prompt_endpoint(request: RequestModel):
    generated_prompt = generate_prompt(request.user_input, request.tone)
    return ResponseModel(generated_prompt=generated_prompt)

