from ._http import HTTPClient
from .resources import InvestigationsResource, HealthResource


class DemonCryClient:
    """Client for interacting with the DEMON CRY API.

    Provides async access to investigations and health endpoints.
    """

    def __init__(
        self,
        base_url: str,
        api_key: str | None = None,
        timeout: float = 60.0,
        max_retries: int = 3,
    ):
        """Initialize the DEMON CRY client.

        Args:
            base_url: Base URL of the DEMON CRY API.
            api_key: API key for authentication. If ``None``, requests are
                sent without an ``Authorization`` header.
            timeout: Default request timeout in seconds.
            max_retries: Maximum number of retries for failed requests.
        """
        self._http = HTTPClient(
            base_url=base_url,
            api_key=api_key,
            timeout=timeout,
            max_retries=max_retries,
        )

        self.investigations = InvestigationsResource(self._http)
        self.health = HealthResource(self._http)

    async def aclose(self):
        """Close the underlying HTTP client and release resources.

        Raises:
            httpx.HTTPError: If closing the transport fails.
        """
        await self._http.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.aclose()
