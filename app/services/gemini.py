import json
from typing import Dict, Any

async def generate_advisory(farmer_input: str, weather_data: Dict[str, Any], places_data: Dict[str, str]) -> Dict[str, Any]:
    # Mock Gemini response respecting the exact required response contract
    # In production, this uses Vertex AI Gemini 1.5 Pro to generate the JSON
    
    return {
        "namaskar": "Kisan bhai",
        "aaj_ka_mausam": {
            "forecast_72hr": "Light rain expected over the next two days.",
            "risk_level": "caution",
            "rain_mm_expected": 15.5,
            "temperature_range": "22°C to 30°C"
        },
        "aapki_fasal_ke_liye": {
            "crop": "gehun",
            "immediate_action": "Avoid spraying pesticides today.",
            "next_48_hours": "Prepare for minor waterlogging.",
            "avoid_doing": "Do not irrigate."
        },
        "calendar_events_created": [
            "Check field drainage (Tomorrow)"
        ],
        "nearest_help": places_data,
        "source": "Mocked IMD forecast dated today / Search grounding"
    }
