from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class WeatherSummary(BaseModel):
    forecast_72hr: str
    risk_level: str
    rain_mm_expected: float
    temperature_range: str

class CropAdvice(BaseModel):
    crop: str
    immediate_action: str
    next_48_hours: str
    avoid_doing: str

class NearestHelp(BaseModel):
    krishi_kendra: str
    mandi: str

class KisanResponse(BaseModel):
    namaskar: str
    aaj_ka_mausam: WeatherSummary
    aapki_fasal_ke_liye: CropAdvice
    calendar_events_created: List[str]
    nearest_help: NearestHelp
    source: str

class FarmerInput(BaseModel):
    text: Optional[str] = None
    voice_audio_b64: Optional[str] = None
    image_b64: Optional[str] = None
    location_str: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
