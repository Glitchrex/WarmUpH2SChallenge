import time
from typing import Dict, Any, Optional

# A simple in-memory cache to proxy Firebase Realtime Database
# In production, this would use firebase_admin.db
_cache: Dict[str, Dict[str, Any]] = {}

def get_weather_cache(lat_lng: str, date_str: str) -> Optional[Dict[str, Any]]:
    key = f"{lat_lng}_{date_str}"
    entry = _cache.get(key)
    if entry:
        if time.time() - entry["timestamp"] < 3600: # 1 hour TTL
            return entry["data"]
    return None

def set_weather_cache(lat_lng: str, date_str: str, data: Dict[str, Any]) -> None:
    key = f"{lat_lng}_{date_str}"
    _cache[key] = {
        "timestamp": time.time(),
        "data": data
    }
