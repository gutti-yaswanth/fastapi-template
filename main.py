from fastapi import FastAPI
from api.routes.v1.router import router as api_router_v1
from api.routes.v2.router import router as api_router_v2

app = FastAPI(title="Zanzo Service")

@app.get("/")
def main():
    return {"message": "Welcome to Zanzo Backend API"}

app.include_router(api_router_v1)
app.include_router(api_router_v2)