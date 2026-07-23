import httpx
from .models import OSINTRequest, OSINTResponse

class DemonCryClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self._client = httpx.AsyncClient()

    async def investigate(self, target: str, max_tokens: int = 15000) -> OSINTResponse:
        request = OSINTRequest(target=target, max_tokens=max_tokens)
        response = await self._client.post(
            f"{self.base_url}/api/investigate",
            json=request.model_dump()
        )
        response.raise_for_status()
        return OSINTResponse.model_validate(response.json())

    async def aclose(self):
        await self._client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.aclose()