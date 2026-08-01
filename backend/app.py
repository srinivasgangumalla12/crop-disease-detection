"""
Main Web Server & REST API Application for Crop Disease Detection & Agricultural Weather Advisory System.
Built with FastAPI.
"""

import os
import io
from fastapi import FastAPI, File, UploadFile, Form, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from backend.ml_engine import analyze_leaf_image, save_farmer_upload
from backend.weather_advisory import fetch_live_weather, generate_weather_advisory, REGION_COORDINATES
from backend.translator_tts import SUPPORTED_LANGUAGES, translate_report
from backend.disease_knowledge import DISEASE_DATABASE

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
UPLOADS_DIR = os.path.join(BASE_DIR, "dataset_uploads")
os.makedirs(UPLOADS_DIR, exist_ok=True)

app = FastAPI(
    title="FARMERS SOLUTION - Crop Disease Detection & Weather Advisory API",
    description="AI Computer Vision Plant Leaf Disease Diagnostics, Live Weather Analytics, and Multilingual Voice Advisory for Farmers.",
    version="2.0.0"
)

# Enable CORS for cross-origin frontend support
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount frontend static files
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")
app.mount("/uploads", StaticFiles(directory=UPLOADS_DIR), name="uploads")


@app.get("/api/sample_image")
async def get_sample_image(name: str = "tomato_late_blight.jpg"):
    """Serves test sample leaf images."""
    samples_dir = os.path.join(BASE_DIR, "backend", "sample_data")
    file_path = os.path.join(samples_dir, name)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=404, detail="Sample image not found.")


@app.get("/", response_class=HTMLResponse)
async def serve_index():
    """Serves the main farmer dashboard UI."""
    index_path = os.path.join(FRONTEND_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return HTMLResponse("<h2>Crop Disease System Backend Running. Frontend folder initializing...</h2>")


@app.get("/api/languages")
async def get_languages():
    """Returns list of supported regional farmer languages."""
    return {"languages": SUPPORTED_LANGUAGES}


@app.get("/api/weather")
async def get_weather(region: str = "Guntur", lat: float = 16.3067, lon: float = 80.4365):
    """Fetches live weather & risk advisory for farmer location."""
    w_data = fetch_live_weather(lat=lat, lon=lon, region_name=region)
    advisory = generate_weather_advisory(w_data)
    return {"weather": w_data, "advisory": advisory}


@app.post("/api/detect")
async def detect_crop_disease(
    file: UploadFile = File(...),
    region: str = Form("Guntur"),
    lang: str = Form("te"),
    lat: float = Form(16.3067),
    lon: float = Form(80.4365)
):
    """
    Main Crop Leaf Disease Diagnosis Endpoint.
    1. Processes uploaded leaf image with AI Vision Engine.
    2. Fetches live weather for farmer's region.
    3. Calculates disease spreading risk and next-step actions.
    4. Translates report into requested regional language (e.g. Telugu, Hindi, Tamil, English).
    5. Returns audio speech script for voice playback.
    """
    contents = await file.read()
    if not contents:
        raise HTTPException(status_code=400, detail="Empty image uploaded.")

    # 1. Vision Engine Analysis
    vision_result = analyze_leaf_image(contents, original_filename=file.filename)
    if not vision_result.get("success"):
        raise HTTPException(status_code=500, detail=vision_result.get("error", "Analysis failed."))

    # 2. Weather & Advisory Engine
    w_data = fetch_live_weather(lat=lat, lon=lon, region_name=region)
    disease_triggers = vision_result.get("weather_risk_triggers", {})
    weather_adv = generate_weather_advisory(w_data, disease_triggers=disease_triggers)

    # 3. Combine Full Agricultural Report
    full_report = {
        "crop": vision_result["crop"],
        "disease_name": vision_result["disease_name"],
        "disease_key": vision_result["disease_key"],
        "category": vision_result["category"],
        "confidence_score": vision_result["confidence_score"],
        "severity_level": vision_result["severity_level"],
        "affected_area_percentage": vision_result["affected_area_percentage"],
        "symptoms": vision_result["symptoms"],
        "organic_remedies": vision_result["organic_remedies"],
        "chemical_remedies": vision_result["chemical_remedies"],
        "preventive_actions": vision_result["preventive_actions"],
        "vision_metrics": vision_result["vision_metrics"],
        "weather_info": w_data,
        "weather_advisory": weather_adv,
        "farmer_region": region
    }

    # 4. Multilingual Translation & Audio Speech Script Generation
    final_output = translate_report(full_report, lang_code=lang)
    return JSONResponse(final_output)


@app.post("/api/dataset/upload")
async def upload_farm_dataset_photo(
    file: UploadFile = File(...),
    crop_name: str = Form("Tomato"),
    disease_tag: str = Form("Early Blight"),
    location: str = Form("Local Farm")
):
    """
    Saves farmer uploaded photos from local farms to enrich the regional training dataset.
    """
    contents = await file.read()
    res = save_farmer_upload(contents, crop_name, disease_tag, location, UPLOADS_DIR)
    return res


@app.get("/api/dataset/list")
async def list_farm_dataset():
    """Lists all contributed local farm leaf photos."""
    files = []
    if os.path.exists(UPLOADS_DIR):
        for f in os.listdir(UPLOADS_DIR):
            if f.endswith((".jpg", ".png", ".jpeg")):
                files.append({
                    "filename": f,
                    "url": f"/uploads/{f}",
                    "size_kb": round(os.path.getsize(os.path.join(UPLOADS_DIR, f)) / 1024, 1)
                })
    return {"total_photos": len(files), "photos": files}


@app.post("/api/whatsapp/webhook")
async def whatsapp_bot_webhook(request: Request):
    """
    Simulates WhatsApp Business API Webhook.
    Receives simulated WhatsApp message/image payload and returns WhatsApp formatted message response card.
    """
    try:
        body = await request.json()
    except Exception:
        body = {}

    sender_phone = body.get("From", "+919876543210")
    incoming_msg = body.get("Body", "Hi").lower()

    # Simulate WhatsApp automated response
    wa_response = {
        "messaging_product": "whatsapp",
        "to": sender_phone,
        "type": "text",
        "text": {
            "body": (
                "🌾 *FARMERS SOLUTION - Crop Disease & Weather Bot* 🌾\n\n"
                "నమస్కారం! Please reply with a leaf photo of your crop to diagnose disease instantly.\n\n"
                "Available Commands:\n"
                "1️⃣ Upload leaf image\n"
                "2️⃣ Type 'WEATHER' for local farm risk report\n"
                "3️⃣ Type 'TELUGU', 'HINDI', or 'ENGLISH' to switch voice language."
            )
        }
    }
    return wa_response
