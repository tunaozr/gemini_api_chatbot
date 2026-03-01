import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

def load_settings():
    """settings.json dosyasını okur, yoksa varsayılan ayarları döner."""
    default_settings = {
        "bot_name": "Asistan",
        "model_name": "gemini-2.5-flash",
        "temperature": 1.0,
        "system_instruction": "Sen yardımcı bir asistansın."
    }
    
    if os.path.exists("settings.json"):
        with open("settings.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return default_settings

def get_gemini_model():
    load_dotenv()
    settings = load_settings() # Ayarları oku
    
    api_key = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=api_key)
    
    # Modeli ayarlarla birlikte kuruyoruz
    model = genai.GenerativeModel(
        model_name=settings["model_name"],
        generation_config={"temperature": settings["temperature"]},
        system_instruction=settings["system_instruction"] # Botun kişiliği buraya!
    )
    return model, settings["bot_name"]