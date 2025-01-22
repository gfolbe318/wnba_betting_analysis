from wnba_betting_analysis.models.base import Base
from wnba_betting_analysis.models.team import Team
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey, Integer

class Game(Base):
    __tablename__ = "Game"
    
    # Internal primary key
    game_id: Mapped[int] = mapped_column(primary_key=True)
    
    # This is the id of the game within the rapid api ecosystem
    rapid_api_game_id: Mapped[str] = mapped_column(String)
    
    # This is the id of the game within the odds api ecosystem
    odds_api_game_id: Mapped[str | None] = mapped_column(String, nullable=True) # Revisit this later
        
    # YYYY-MM-DD
    date: Mapped[str] = mapped_column(String)
    
    home_team_id: Mapped[int] = mapped_column(ForeignKey(Team.team_id))
    away_team_id: Mapped[int] = mapped_column(ForeignKey(Team.team_id))
    
    winning_team_id: Mapped[int] = mapped_column(Integer)
    losing_team_id: Mapped[int] = mapped_column(Integer)
    
    def __init__(
        self,
        rapid_api_game_id: str,
        odds_api_game_id: str | None,
        date: str,
        home_team_id: int,
        away_team_id: int,
        winning_team_id: int,
        losing_team_id: int,        
    ):
        self.rapid_api_game_id = rapid_api_game_id
        self.odds_api_game_id = odds_api_game_id
        self.date = date
        self.home_team_id = home_team_id
        self.away_team_id = away_team_id
        self.winning_team_id = winning_team_id
        self.losing_team_id = losing_team_id