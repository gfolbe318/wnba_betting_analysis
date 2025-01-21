from wnba.models.base import Base
from wnba.models.team import Team

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey

class Player(Base):
    __tablename__ = "Player"
    
    # Internal primary key
    player_id: Mapped[int] = mapped_column(primary_key=True)
    
    # This is the id of the player within the rapid api ecosystem
    rapid_api_player_id: Mapped[str] = mapped_column(String)
    
    # This is the id of the player within the odds api ecosystem
    odds_api_player_id: Mapped[str | None] = mapped_column(String, nullable=True) # Revisit this later
    
    name_first: Mapped[str] = mapped_column(String)
    name_last: Mapped[str] = mapped_column(String)
    
    position: Mapped[str] = mapped_column(String)
    current_team_id: Mapped[str] = mapped_column(ForeignKey(Team.team_id))
    
    def __init__(
        self,
        rapid_api_player_id: str,
        odds_api_player_id: str | None,
        name_first: str,
        name_last: str,
        position: str,
        current_team_id: str
    ): 
        self.rapid_api_player_id = rapid_api_player_id
        self.odds_api_player_id = odds_api_player_id
        self.name_first = name_first
        self.name_last = name_last
        self.position = position
        self.current_team_id = current_team_id