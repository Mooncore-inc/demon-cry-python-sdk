from pydantic import BaseModel, ConfigDict

class OSINTRequest(BaseModel):
    target: str
    max_tokens: int = 15000

class OSINTResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    status: str
    result: str | None = None
    tools_used: list[dict] = []
    total_tokens: int = 0