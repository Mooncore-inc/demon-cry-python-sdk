from pydantic import BaseModel, ConfigDict

class HealthResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    status: str
    latency_ms: int