from wnba.models.base import Base
from wnba.models.player import Player
from wnba.models.team import Team
from wnba.models.game import Game
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey

class BoxScore(Base):
    __tablename__ = "BoxScore"
    
    # Internal primary key
    boxscore_id: Mapped[int] = mapped_column(primary_key=True)
    
    # This is the player id within the rapid api ecosystem
    player_id: Mapped[int] = mapped_column(ForeignKey(Player.rapid_api_player_id))
    
    # This is the id of the team that the player was on when this game occurred
    team_id: Mapped[int] = mapped_column(ForeignKey(Team.team_id))
    
    # This is the id of the opponent
    opponent_team_id: Mapped[int] = mapped_column(ForeignKey(Team.team_id))
    
    # This is the id of the game
    game_id: Mapped[int] = mapped_column(ForeignKey(Game.game_id))
    
    # Statistics gathered during a single game
    minutes: Mapped[int] = mapped_column(Integer)
    field_goals_made: Mapped[int] = mapped_column(Integer)
    field_goals_att: Mapped[int] = mapped_column(Integer)
    three_pts_made: Mapped[int] = mapped_column(Integer)
    three_pts_att: Mapped[int] = mapped_column(Integer)
    free_throws_made: Mapped[int] = mapped_column(Integer)
    free_throws_att: Mapped[int] = mapped_column(Integer)
    offensive_rebs: Mapped[int] = mapped_column(Integer)
    defensive_rebs: Mapped[int] = mapped_column(Integer)
    rebs: Mapped[int] = mapped_column(Integer)
    assists: Mapped[int] = mapped_column(Integer)
    steals: Mapped[int] = mapped_column(Integer)
    blocks: Mapped[int] = mapped_column(Integer)
    turnovers: Mapped[int] = mapped_column(Integer)
    fouls: Mapped[int] = mapped_column(Integer)
    net: Mapped[int] = mapped_column(Integer)
    points: Mapped[int] = mapped_column(Integer)
    
    def __init__(
        self,
        player_id: int,
        team_id: int,
        opponent_team_id: int,
        game_id: int,
        minutes: int,
        field_goals_made: int,
        field_goals_att: int,
        free_throws_made: int,
        free_throws_att: int,
        three_pts_made: int,
        three_pts_att: int,
        offensive_rebs: int,
        defensive_rebs: int,
        rebs: int,
        assists: int,
        steals: int,
        blocks: int,
        turnovers: int,
        fouls: int,
        net: int,
        points: int,
    ):
        self.player_id = player_id
        self.team_id = team_id
        self.opponent_team_id = opponent_team_id
        self.game_id = game_id
        self.minutes = minutes
        self.field_goals_made = field_goals_made
        self.field_goals_att = field_goals_att
        self.free_throws_made = free_throws_made
        self.free_throws_att = free_throws_att
        self.three_pts_made = three_pts_made
        self.three_pts_att = three_pts_att
        self.offensive_rebs = offensive_rebs
        self.defensive_rebs = defensive_rebs
        self.rebs = rebs
        self.assists = assists
        self.steals = steals
        self.blocks = blocks
        self.turnovers = turnovers
        self.fouls = fouls
        self.net = net
        self.points = points
