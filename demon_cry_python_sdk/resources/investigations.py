from ..models import OSINTRequest, OSINTResponse


class InvestigationsResource:
    """Resource for creating and managing OSINT investigations."""

    def __init__(self, http):
        self._http = http

    async def create(self, target: str) -> OSINTResponse:
        """Create a new OSINT investigation.

        Args:
            target: Target to investigate (domain, IP, username, etc.).

        Returns:
            OSINTResponse with investigation results.

        Raises:
            UnauthorizedError: If the API returns ``401``.
            APIError: For any other ``4xx``/``5xx`` status code.

        Example:
            >>> async with DemonCryClient(base_url="...", api_key="...") as client:
            ...     result = await client.investigations.create(target="example.com")
            ...     print(result.status, result.tools_used)
        """
        request = OSINTRequest(target=target)
        response = await self._http.post("/api/investigate", json=request.model_dump())
        return OSINTResponse.model_validate(response)
