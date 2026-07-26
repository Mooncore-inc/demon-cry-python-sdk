from ._http import HTTPClient
from .models import HealthResponse
from .resources import InvestigationsResource

class DemonCryClient:
    def __init__(
        self,
        base_url: str,
        api_key: str | None = None,
        timeout: float = 60.0,
        max_retries: int = 3
    ):
        self._http = HTTPClient(
            base_url=base_url,
            api_key=api_key,
            timeout=timeout,
            max_retries=max_retries
        )
        
        # Resources
        self.investigations = InvestigationsResource(self._http)

    async def health(self) -> HealthResponse:
        response = await self._http.get("/api/health")
        return HealthResponse.model_validate(response)

    async def aclose(self):
        await self._http.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.aclose()