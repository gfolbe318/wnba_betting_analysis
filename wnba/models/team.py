from wnba.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class Team(Base):
    __tablename__ = "Team"

    # Internal primary key
    team_id: Mapped[int] = mapped_column(primary_key=True)
    
    # This is the id of the team in the rapid api ecosystem
    rapid_api_team_id: Mapped[str] = mapped_column(String)
    
    # This is the id of the team in the odds api ecosystem
    odds_api_team_id: Mapped[str | None] = mapped_column(String, nullable=True) # Revisit this later
    
    acronym: Mapped[str] = mapped_column(String)
    city: Mapped[str] = mapped_column(String)
    team_name: Mapped[str] = mapped_column(String)
    conference: Mapped[str] = mapped_column(String)
    
    def __init__(
        self,
        rapid_api_team_id: str,
        odds_api_team_id: str | None,
        acronym: str,
        city: str,
        team_name: str,
        conference: str,
    ):
        self.rapid_api_team_id=rapid_api_team_id
        self.odds_api_team_id=odds_api_team_id
        self.acronym=acronym
        self.city=city
        self.team_name=team_name
        self.conference=conference
