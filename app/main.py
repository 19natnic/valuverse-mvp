from fastapi import FastAPI
from pydantic import BaseModel
from app.services.valuation import land_to_sqm, compute_central_and_range

app = FastAPI(title="Valuverse MVP")

class QuickInput(BaseModel):
    property_type: str            # "condo" | "house" | "land"
    built_area_sqm: float = 0.0
    land_rai: int = 0
    land_ngan: int = 0
    land_wah: int = 0

@app.get("/")
def root():
    return {"status": "ok", "app": "Valuverse MVP"}

@app.post("/valuations/quick")
def quick_valuation(payload: QuickInput):
    if payload.property_type == "land":
        area = land_to_sqm(payload.land_rai, payload.land_ngan, payload.land_wah)
        base = 40000.0
    else:
        area = payload.built_area_sqm
        base = 95000.0 if payload.property_type == "condo" else 45000.0

    central, low, high = compute_central_and_range(base, area)
    return {
        "property_type": payload.property_type,
        "area_sqm": area,
        "base_price_per_sqm": base,
        "est_value": round(central, 2),
        "low_value": round(low, 2),
        "high_value": round(high, 2),
        "confidence": "Medium"   # mock ไว้ก่อน, วันถัดไปค่อยคำนวณจริง
    }
