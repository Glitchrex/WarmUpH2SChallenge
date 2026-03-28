import os

class Settings:
    PROJECT_ID: str = os.getenv("GOOGLE_CLOUD_PROJECT", "kisan-saathi-project")
    # All other secrets via Secret Manager dynamically
    
settings = Settings()
