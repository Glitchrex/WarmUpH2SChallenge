import asyncio
from typing import Dict, Any

async def get_nearest_help(lat: float, lng: float) -> Dict[str, str]:
    # Mock Google Maps Places API response for nearby KVK and Mandi
    await asyncio.sleep(0.2)
    return {
        "krishi_kendra": "Nearest KVK, 12km (099999999)",
        "mandi": "Main Anaj Mandi, 15km"
    }

async def geocode_location(address: str) -> tuple[float, float]:
    # Mock Geocoding
    await asyncio.sleep(0.1)
    return 28.6139, 77.2090 # New Delhi coordinates
