import json
import uvicorn
from fastapi import FastAPI
from api.router import api_router
from core.risk_engine import RiskEngine

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

app = FastAPI(title="ApexTrade Core")
app.include_router(api_router, prefix="/api")

# Initialize global state (simplified for example)
cfg = load_config()
risk_manager = RiskEngine(cfg["risk_limits"])

@app.on_event("startup")
async def startup_event():
    print("Starting local aggregation server...")
    # DB init or session warmup would go here

if __name__ == "__main__":
    cfg = load_config()
    uvicorn.run(app, host=cfg["server"]["host"], port=cfg["server"]["port"])