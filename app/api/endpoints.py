from fastapi import APIRouter, HTTPException, Depends
import asyncio
from typing import Any

from app.models.schemas import FarmerInput, KisanResponse
from app.services.weather import get_weather
from app.services.maps import get_nearest_help, geocode_location
from app.services.translate import detect_language, auto_translate
from app.services.gemini import generate_advisory

router = APIRouter()

@router.post("/advisory", response_model=KisanResponse)
async def get_advisory(request: FarmerInput):
    # 1. Determine location
    lat = request.lat
    lng = request.lng
    
    if lat is None or lng is None:
        if request.location_str:
            lat, lng = await geocode_location(request.location_str)
        else:
            raise HTTPException(status_code=400, detail="Must provide lat/lng or location_str")

    text_input = request.text or "Voice input provided"
    
    # 2. Fire external API calls in parallel based on efficient orchestration rules
    weather_task = get_weather(lat, lng)
    maps_task = get_nearest_help(lat, lng)
    lang_task = detect_language(text_input)
    
    weather_data, places_data, lang_code = await asyncio.gather(
        weather_task, maps_task, lang_task
    )
    
    # 3. Use core brain (Gemini) to generate actionable advisory
    advisory_dict = await generate_advisory(text_input, weather_data, places_data)
    
    # Returning structured according to KisanResponse schema
    return KisanResponse(**advisory_dict)
