from pydantic import BaseModel

class ResponseModel(BaseModel):
    generated_prompt: str