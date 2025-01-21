from wnba.routes.boxscores.boxscore_router import boxscore_router
from pydantic import BaseModel

class ImportBoxScoreSingleRequest(BaseModel):
    rapid_api_id: str

@boxscore_router.post("/import_boxscore_single")
def import_boxscore_single(request: ImportBoxScoreSingleRequest) -> None:
    pass