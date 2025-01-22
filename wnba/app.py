from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from wnba.routes.router import api_router

app = FastAPI(debug=True)
app.include_router(api_router)

@app.get("/")
def root():
    return HTMLResponse("<h1>Hello World!</h1>")