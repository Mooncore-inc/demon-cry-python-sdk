from ..models import HealthResponse as Model


class HealthResource:
    """Resource for checking API health status."""

    def __init__(self, http):
        self._http = http

    async def get(self) -> Model:
        """Get health status of the API.

        Returns:
            HealthResponse containing ``status`` and ``latency_ms``.

        Example:
            >>> async with DemonCryClient(base_url="...", api_key="...") as client:
            ...     health = await client.health.get()
            ...     print(health.status, health.latency_ms)
        """
        response = await self._http.get("/api/health")
        return Model.model_validate(response)
