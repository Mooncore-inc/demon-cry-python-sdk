from pydantic import BaseModel, ConfigDict


class TokenUsage(BaseModel):
    total: int = 0
    prompt: int = 0
    completion: int = 0
    reasoning: int = 0
    cache_hit: int = 0
    cache_miss: int = 0


class OSINTRequest(BaseModel):
    target: str


class OSINTResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    status: str
    result: str
    tools_used: list[dict] = []
    tokens: TokenUsage = TokenUsage()
