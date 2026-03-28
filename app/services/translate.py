import asyncio

async def auto_translate(text: str, target_language: str = "hi") -> str:
    # Mock Google Translate API
    await asyncio.sleep(0.1)
    # Just return text as is for this mock
    return f"[Translated to {target_language}]: {text}"

async def detect_language(text: str) -> str:
    # Mock language detection
    await asyncio.sleep(0.1)
    return "hi" # Default to Hindi
