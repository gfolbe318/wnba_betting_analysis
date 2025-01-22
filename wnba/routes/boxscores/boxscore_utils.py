from pathlib import Path
import json
from wnba.models.game import Game
from wnba.models.player_boxscore import PlayerBoxScore



def get_stat_index(header: str, headers_list: list[str]) -> int:
    """
    I'm pretty sure the list of headers is in the same order every time.
    Better safe than sorry

    Args:
        header (str): The header that we want
        headers_list (list[str]): The list of statistic headers in the response.

    Returns:
        int: The index of the statistic that we're looking for
    """
    return headers_list.index(header)

def get_boxscores_from_game_data(
    json_data: dict
) -> list[PlayerBoxScore]:
    """Returns a list of boxscores from json response

    Args:
        json_data (dict): The response from the boxscore api

    Returns:
        list[BoxScore]: A list of boxscores data models
    """
   
    box_scores: list[PlayerBoxScore] = []
    for players in json_data["players"]:
        stat_headers: list[str] = players["statistics"][0]["names"]
        
        rapid_api_team_id: str = players["team"]["id"] # Convert to internal id
        
        for athlete in players["statistics"][0]["athletes"]:
                
            rapid_api_player_id: str = athlete["athlete"]["id"] # Convert to internal id
            stats: list[str] = athlete["stats"]
            
            # Empty list if the player doesn't play
            if stats:        
                box_scores.append(
                    PlayerBoxScore(
                        player_id=0,
                        team_id=0,
                        opponent_team_id=0,
                        game_id=0,
                        minutes=int(stats[get_stat_index("MIN", stat_headers)]),
                        field_goals_made=int(stats[get_stat_index("FG", stat_headers)].split("-")[0]),
                        field_goals_att=int(stats[get_stat_index("FG", stat_headers)].split("-")[1]),
                        free_throws_made=int(stats[get_stat_index("FT", stat_headers)].split("-")[0]),
                        free_throws_att=int(stats[get_stat_index("FT", stat_headers)].split("-")[1]),
                        three_pts_made=int(stats[get_stat_index("3PT", stat_headers)].split("-")[0]),
                        three_pts_att=int(stats[get_stat_index("3PT", stat_headers)].split("-")[1]),
                        offensive_rebs=int(stats[get_stat_index("OREB", stat_headers)]),
                        defensive_rebs=int(stats[get_stat_index("DREB", stat_headers)]),
                        rebs=int(stats[get_stat_index("REB", stat_headers)]),
                        assists=int(stats[get_stat_index("AST", stat_headers)]),
                        steals=int(stats[get_stat_index("STL", stat_headers)]),
                        blocks=int(stats[get_stat_index("BLK", stat_headers)]),
                        turnovers=int(stats[get_stat_index("TO", stat_headers)]),
                        fouls=int(stats[get_stat_index("PF", stat_headers)]),
                        net=int(stats[get_stat_index("+/-", stat_headers)]),
                        points=int(stats[get_stat_index("PTS", stat_headers)]),
                    )
                )
    return box_scores