from wnba_betting_analysis.models.base import Base
from wnba_betting_analysis.models.team import Team
from wnba_betting_analysis.models.game import Game
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey

class TeamBoxScore(Base):
    __tablename__ = "TeamBoxScore"
    
    # Internal primary key
    team_boxscore_id: Mapped[int] = mapped_column(primary_key=True)
    
    # This is the game id within our ecosystem
    game_id: Mapped[int] = mapped_column(ForeignKey(Game.game_id))
    
    # This is the game id within the rapid api ecosystem
    rapid_api_game_id: Mapped[str] = mapped_column(String)
    
    # This is the team id within our ecosystem
    team_id: Mapped[int] = mapped_column(ForeignKey(Team.team_id))
    
    # This is the opponent's team id within our ecosystem
    opponent_team_id: Mapped[int] = mapped_column(ForeignKey(Team.team_id))
    
    # Statistics from the game which aren't tracked in the player boxscores
    # We can add more if necessary, who knows if these will be valuable
    turnover_pts_conceded: Mapped[int] = mapped_column(Integer)
    fastbreak_pts: Mapped[int] = mapped_column(Integer)
    points_in_paint: Mapped[int] = mapped_column(Integer)
    