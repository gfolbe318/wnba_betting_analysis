from fastapi import FastAPI

from wnba.routes.router import api_router

app = FastAPI(debug=True)
app.include_router(api_router)
