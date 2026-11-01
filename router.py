from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from api import accounts
from core.ai_client import AIClient

router = APIRouter()

class TradeRequest(BaseModel):
    account_id: str
    symbol: str
    side: str
    amount: float

# Load config to pass to AI client (simplified)
import json
with open("config.json", "r") as f:
    cfg = json.load(f)

ai_engine = AIClient(cfg["api_keys"]["openai"])

@router.get("/status")
async def get_status():
    return {"status": "ok", "service": "apextrade-core"}

@router.get("/accounts")
async def get_accounts():
    return accounts.get_all_accounts()

@router.post("/ai/analyze")
async def analyze_data(text: str):
    try:
        result = await ai_engine.analyze_market_data(text)
        return {"analysis": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/execute")
async def execute_order(req: TradeRequest):
    # Simplified execution logic
    # In a real app you would call the specific exchange API here
    return {"status": "executed", "order_id": "12345", "details": req.dict()}