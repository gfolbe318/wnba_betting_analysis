from pathlib import Path
import json


def get_index_stat_header(header: str, headers_list: list[str]) -> int:
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


def process_player_data_given_boxscore(
    statistic_headers: list[str], 
    statistics_list: list[str]
) -> dict[str, str]:
    """Transforms a box score into a dictionary with identified column names

    Args:
        statistic_headers (list[str]): The list of headers used for the stats
        statistics_list (list[str]): The actual statistics recorded

    Returns:
        dict[str, str]: A dictionary with key/value pairs of statistic/value
    """
    
    return {
        "MIN": statistics_list[get_index_stat_header("MIN", statistic_headers)],
        "FGM": statistics_list[get_index_stat_header("FG", statistic_headers)].split("-")[0],
        "FGA": statistics_list[get_index_stat_header("FG", statistic_headers)].split("-")[1],
        "3PM": statistics_list[get_index_stat_header("3PT", statistic_headers)].split("-")[0],
        "3PA": statistics_list[get_index_stat_header("3PT", statistic_headers)].split("-")[1],
        "FTM": statistics_list[get_index_stat_header("FT", statistic_headers)].split("-")[0],
        "FTA": statistics_list[get_index_stat_header("FT", statistic_headers)].split("-")[1],
        "ORB": statistics_list[get_index_stat_header("OREB", statistic_headers)],
        "DRB": statistics_list[get_index_stat_header("DREB", statistic_headers)],
        "REB": statistics_list[get_index_stat_header("REB", statistic_headers)],
        "AST": statistics_list[get_index_stat_header("AST", statistic_headers)],
        "STL": statistics_list[get_index_stat_header("STL", statistic_headers)],
        "BLK": statistics_list[get_index_stat_header("BLK", statistic_headers)],
        "TOV": statistics_list[get_index_stat_header("TO", statistic_headers)],
        "FLS": statistics_list[get_index_stat_header("PF", statistic_headers)],
        "NET": statistics_list[get_index_stat_header("+/-", statistic_headers)],
        "PTS": statistics_list[get_index_stat_header("PTS", statistic_headers)],
    }
    
if __name__ == "__main__":

    data_path = Path(__file__).parent.parent.joinpath("resources", "sample_game_data.json").absolute()
    json_data = json.load(data_path.open("r"))
    
    home_players = json_data["players"][0]["statistics"][0]
    away_players = json_data["players"][0]["statistics"][0]
    
    stat_headers = json_data["players"][0]["statistics"][0]["names"]
    
    for player in home_players["athletes"]:
        print(process_player_data_given_boxscore(stat_headers, player['stats']))