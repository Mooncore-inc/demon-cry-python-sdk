from ..models import HealthResponse as Model

class HealthResource:
    def __init__(self, http):
        self._http = http

    async def get(self) -> Model:
        """Get health status of the API."""
        response = await self._http.get("/api/health")
        return Model.model_validate(response)
