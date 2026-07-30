from ._http import HTTPClient
from .resources import InvestigationsResource, HealthResource

class DemonCryClient:
    """
    Client for interacting with the DEMON CRY API.
    """
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
        self.health = HealthResource(self._http)

    async def aclose(self):
        await self._http.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.aclose()