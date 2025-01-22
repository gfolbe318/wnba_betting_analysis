from fastapi import APIRouter

boxscore_router: APIRouter = APIRouter(prefix="/boxscores", tags=["boxscores"])

from .import_boxscore_on_date import import_boxscore_on_date