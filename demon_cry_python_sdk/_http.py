import httpx
from tenacity import retry, stop_after_attempt, wait_exponential
from .exceptions import APIError, RateLimitError, UnauthorizedError


class HTTPClient:
    def __init__(
        self, base_url: str, api_key: str | None, timeout: float, max_retries: int
    ):
        headers = {"Accept": "application/json"}
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"

        self._client = httpx.AsyncClient(
            base_url=base_url, headers=headers, timeout=timeout
        )
        self.max_retries = max_retries

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        reraise=True,
    )
    async def post(self, path: str, json: dict) -> dict:
        """Send a POST request.

        Args:
            path: URL path relative to the base URL.
            json: JSON-serializable request body.

        Returns:
            Parsed JSON response as a dictionary.

        Raises:
            RateLimitError: If the API returns ``429``.
            UnauthorizedError: If the API returns ``401``.
            APIError: For any other ``4xx``/``5xx`` status code.
        """
        response = await self._client.post(path, json=json)
        self._handle_errors(response)
        return response.json()

    async def get(self, path: str) -> dict:
        """Send a GET request.

        Args:
            path: URL path relative to the base URL.

        Returns:
            Parsed JSON response as a dictionary.

        Raises:
            RateLimitError: If the API returns ``429``.
            UnauthorizedError: If the API returns ``401``.
            APIError: For any other ``4xx``/``5xx`` status code.
        """
        response = await self._client.get(path)
        self._handle_errors(response)
        return response.json()

    def _handle_errors(self, response: httpx.Response):
        if response.status_code == 429:
            raise RateLimitError(429, "Rate limit exceeded")
        if response.status_code == 401:
            raise UnauthorizedError(401, "Invalid or missing API key")
        if response.status_code >= 400:
            raise APIError(response.status_code, response.text)

    async def aclose(self):
        await self._client.aclose()
