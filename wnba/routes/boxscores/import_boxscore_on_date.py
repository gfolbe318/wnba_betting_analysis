from wnba.routes.boxscores.boxscore_router import boxscore_router
from pydantic import BaseModel
from wnba.models.game import Game
from wnba.routes.boxscores.boxscore_utils import get_boxscores_from_game_data

from pathlib import Path
import json


class ImportBoxScoreSingleRequest(BaseModel):
    year: str
    month: str
    day: str

@boxscore_router.post("/import_boxscore_on_date")
def import_boxscore_on_date(request: ImportBoxScoreSingleRequest) -> None:
    # Make API call to scoreboard on given date
    # Parse through all the games on that given date

    data_path = Path(__file__).parents[2].joinpath("resources", "sample_game_data.json").absolute()
    json_data = json.load(data_path.open("r"))
    
    rapid_api_home_team_id: str # Convert to game_id
    rapid_api_away_team_id: str # Convert to game id
    
    if json_data["teams"][0]["homeAway"] == "away":
        rapid_api_away_team_id = json_data["teams"][0]["team"]["id"]
        rapid_api_home_team_id = json_data["teams"][1]["team"]["id"]
    else:
        rapid_api_home_team_id = json_data["teams"][0]["team"]["id"]
        rapid_api_away_team_id = json_data["teams"][1]["team"]["id"]
        
    # Get the date and winning/losing team id from the boxscore    
    game = Game(
        json_data["id"],
        odds_api_game_id=None,
        date="YYYMMMDD", # Get this from boxscore
        home_team_id=0, # Fix this
        away_team_id=0, # Fix this
        winning_team_id=0, # Fix this
        losing_team_id=0 # Fix this
    )
    
    box_scores = get_boxscores_from_game_data(json_data)