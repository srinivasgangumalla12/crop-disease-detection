# 🌾 FARMERS SOLUTION - Smart Crop Disease Detection & Agricultural Weather Advisory System

> An end-to-end AI Computer Vision, Live Weather Advisory & Multilingual Voice Assistant System tailored for regional farmers.

![License](https://img.shields.io/badge/License-MIT-green.svg)
![Python](https://img.shields.io/badge/Python-3.14-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-2.0-009688.svg)

---

## 🌟 Key Features

1. **📸 AI Computer Vision Crop Disease Diagnosis**:
   - Classifies 25+ plant leaf diseases across major crops (Tomato, Potato, Rice/Paddy, Corn/Maize, Cotton, Apple, Wheat).
   - Computes disease confidence %, severity level (Early, Moderate, Severe), and affected leaf area %.
   - Provides step-by-step Organic Remedies, Chemical Fungicides with exact dosage (g/liter or ml/acre), and preventive cultural practices.

2. **🔊 Multilingual Native Voice Assistant ("Tells the Farmer")**:
   - Supports 7 regional languages: **Telugu (తెలుగు)**, **Hindi (हिन्दी)**, **English**, **Tamil (தமிழ்)**, **Kannada (ಕನ್ನಡ)**, **Marathi (मराठी)**, **Bengali (বাংলা)**.
   - Built-in Voice Audio Readout synthesized in the farmer's native tongue so illiterate/semi-literate farmers can listen to diagnosis and instructions.

3. **🌤️ Live Open-Meteo Weather Integration & Next-Step Radar**:
   - Fetches live temperature, relative humidity, precipitation, and wind speed for regional farm locations (Guntur, Vijayawada, Warangal, Hyderabad, Ludhiana, Pune, etc.).
   - Computes **Fungal Spreading Risk Score** based on micro-climate parameters.
   - Delivers actionable next-step advice: protective spraying windows before rain, holding irrigation to prevent root rot, pruning canopy.

4. **💬 Interactive WhatsApp Bot Simulator & Webhook**:
   - Simulated WhatsApp Business interface for farmers.
   - REST API Webhook endpoint ready for Twilio/WhatsApp Meta Cloud API integration.

5. **🌾 Local Farm Dataset Contribution Hub**:
   - Crowd-sourcing module allowing farmers to upload personal leaf photos from local farms to enrich regional training datasets.

---

## 🚀 Quick Start Guide (VS Code)

### 1. Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### 2. Run Application Server
```bash
python run.py
```

### 3. Open Web Dashboard
Navigate to `http://localhost:8000` in your web browser.

---

## 🐙 Deploy to GitHub Repository

Deploy your project to your GitHub account (`srinivasgangumalla12/crop-disease-detection`):

```bash
python deploy_github.py
```

---

## 📁 Project Structure

```
crop_disease_detector/
├── backend/
│   ├── app.py                # FastAPI HTTP REST API Server
│   ├── ml_engine.py          # AI Computer Vision Leaf Classifier
│   ├── disease_knowledge.py  # Remedies, Fungicides & Disease Knowledge Base
│   ├── weather_advisory.py   # Open-Meteo REST API & Micro-climate Risk Engine
│   ├── translator_tts.py     # Multilingual Translation & Voice Speech Synthesizer
│   └── sample_data/          # Generated test sample leaf images
├── frontend/
│   ├── index.html            # Main Farmer Dashboard UI
│   ├── css/styles.css        # Vibrant Glassmorphism Responsive Styling
│   └── js/app.js             # Interactive Frontend & Speech Logic
├── dataset_uploads/          # Local farm photos repository
├── run.py                    # Server Launcher Script
├── deploy_github.py          # Automated GitHub deployment script
├── requirements.txt
└── README.md
```
