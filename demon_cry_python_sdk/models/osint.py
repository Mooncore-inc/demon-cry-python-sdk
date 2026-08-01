from pydantic import BaseModel, ConfigDict


class OSINTRequest(BaseModel):
    target: str


class OSINTResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    status: str
    result: str
    tools_used: list[dict] = []
    total_tokens: int = 0
