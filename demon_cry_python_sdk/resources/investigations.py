from ..models import OSINTRequest, OSINTResponse

class InvestigationsResource:
    def __init__(self, http):
        self._http = http

    async def create(self, target: str) -> OSINTResponse:
        request = OSINTRequest(target=target)
        response = await self._http.post("/api/investigate", json=request.model_dump())
        return OSINTResponse.model_validate(response)
