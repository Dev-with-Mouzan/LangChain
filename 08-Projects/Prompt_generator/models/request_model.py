from pydantic import BaseModel

class RequestModel(BaseModel):
    user_input: str
    tone: str

    