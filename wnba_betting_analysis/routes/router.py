from fastapi.routing import APIRouter
from wnba_betting_analysis.routes.boxscores import boxscore_router

api_router = APIRouter(prefix="/v1")

api_router.include_router(boxscore_router)