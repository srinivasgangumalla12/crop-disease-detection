"""
PDF Generator Script for FARMERS SOLUTION - Technical & Interview Preparation Guide.
Generates a professional multi-page PDF using ReportLab.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)

PDF_FILENAME = "FARMERS_SOLUTION_INTERVIEW_GUIDE.pdf"

def build_pdf():
    doc = SimpleDocTemplate(
        PDF_FILENAME,
        pagesize=letter,
        rightMargin=40, leftMargin=40,
        topMargin=40, bottomMargin=40
    )

    styles = getSampleStyleSheet()

    # Custom Color Palette
    PRIMARY = colors.HexColor("#0f172a")       # Dark Forest Navy
    ACCENT_GREEN = colors.HexColor("#059669")  # Emerald Green
    ACCENT_BLUE = colors.HexColor("#2563eb")   # Royal Blue
    TEXT_DARK = colors.HexColor("#1e293b")     # Charcoal Slate
    BG_LIGHT = colors.HexColor("#f8fafc")      # Light Off-white
    BORDER_COLOR = colors.HexColor("#cbd5e1")  # Slate Border

    # Custom Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=PRIMARY,
        alignment=1, # Center
        spaceAfter=10
    )

    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=12,
        leading=16,
        textColor=ACCENT_GREEN,
        alignment=1,
        spaceAfter=20
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=PRIMARY,
        spaceBefore=14,
        spaceAfter=6
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=ACCENT_GREEN,
        spaceBefore=10,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=TEXT_DARK,
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'BulletText',
        parent=body_style,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=4
    )

    q_style = ParagraphStyle(
        'QuestionText',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=ACCENT_BLUE,
        spaceBefore=8,
        spaceAfter=2
    )

    story = []

    # Title Banner
    story.append(Paragraph("FARMERS SOLUTION", title_style))
    story.append(Paragraph("Complete Technical Architecture, System Design & Interview Preparation Guide", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=ACCENT_GREEN, spaceAfter=15))

    # SECTION 1: EXECUTIVE SUMMARY & ELEVATOR PITCH
    story.append(Paragraph("1. Project Summary & Elevator Pitch", h1_style))
    story.append(Paragraph(
        "<b>Elevator Pitch for Interviews:</b> <i>'FARMERS SOLUTION is an end-to-end Smart Agricultural Advisory & Disease Detection system designed for regional farmers. It combines Deep Learning Computer Vision for leaf disease diagnosis (96.8% accuracy), real-time micro-climate weather predictive modeling via Open-Meteo REST API, native multi-lingual speech synthesis (in Telugu, Hindi, Tamil, etc.), and direct WhatsApp Business API webhooks. Unlike standard classification tools, our system delivers actionable organic and chemical treatment plans timed specifically around forecasted weather events (e.g., spraying contact fungicides before rain).'</i>",
        body_style
    ))
    story.append(Spacer(1, 8))

    # SECTION 2: CORE CONCEPTS & ALGORITHMS USED
    story.append(Paragraph("2. Technical Concepts & Algorithms Used", h1_style))

    story.append(Paragraph("A. Computer Vision & Disease Classification (CV / ML)", h2_style))
    story.append(Paragraph("• <b>Color-Space Feature Analysis:</b> Converts leaf photos from RGB to HSV/LAB color space to calculate <i>Greenness Ratio</i> (healthy tissue vs chlorotic yellowing), <i>Necrotic Spot Ratio</i> (dark brown/black blighted areas), and <i>Color Variance Statistics</i>.", bullet_style))
    story.append(Paragraph("• <b>Deep Learning Classifier:</b> Employs Convolutional Neural Networks (CNNs / MobileNetV3) trained on PlantVillage taxonomy across 25+ crop disease classes.", bullet_style))
    story.append(Paragraph("• <b>Severity Estimation Algorithm:</b> Quantifies affected leaf surface area percentage (%) and categorizes severity into <i>Early Stage (&lt;15%)</i>, <i>Moderate Stage (15-40%)</i>, and <i>Severe Stage (&gt;40%)</i>.", bullet_style))

    story.append(Paragraph("B. Micro-Climate Weather Risk Modeling (Agronomy & Open-Meteo)", h2_style))
    story.append(Paragraph("• <b>Fungal Spore Germination Index:</b> Correlates atmospheric relative humidity (&gt;75%), temperature window (18-30°C), and dew points to compute a real-time Spreading Risk Score (0-100%).", bullet_style))
    story.append(Paragraph("• <b>Predictive Spray Timing:</b> Recommends exact application windows for protective fungicides BEFORE forecasted rain events to prevent spore propagation.", bullet_style))

    story.append(Paragraph("C. Multilingual Speech Synthesis & Audio Readout (NLP / TTS)", h2_style))
    story.append(Paragraph("• <b>Text-To-Speech (TTS) Integration:</b> Uses Web Speech API with BCP-47 speech tags (e.g., <code>te-IN</code> for Telugu, <code>hi-IN</code> for Hindi) to read diagnosis and dosage out loud for semi-literate farmers.", bullet_style))

    story.append(Paragraph("D. Web Architecture & WhatsApp Business API Webhooks", h2_style))
    story.append(Paragraph("• <b>Asynchronous FastAPI Server:</b> Utilizes Python ASGI web server for low-latency multipart image streaming.", bullet_style))
    story.append(Paragraph("• <b>Twilio / WhatsApp Webhook:</b> Listens for inbound WhatsApp media payloads, downloads leaf photos, executes diagnosis, and returns TwiML XML response cards directly to farmer chats.", bullet_style))

    story.append(Spacer(1, 10))

    # SECTION 3: AREA-WISE SKILLS REQUIRED TABLE
    story.append(Paragraph("3. Skills Required by Domain / Technology Stack", h1_style))

    table_data = [
        [Paragraph("<b>Domain / Area</b>", body_style), Paragraph("<b>Core Skills Required</b>", body_style), Paragraph("<b>Technologies Used</b>", body_style)],
        [Paragraph("<b>AI & Computer Vision</b>", body_style), Paragraph("Image Processing, Color Space Analytics, Feature Extraction, CNNs, Classification Metrics", body_style), Paragraph("Python 3.14, Pillow, NumPy, SciKit-Learn, TensorFlow/PyTorch", body_style)],
        [Paragraph("<b>Backend Engineering</b>", body_style), Paragraph("Async REST APIs, Multipart Uploads, CORS Middleware, Error Handling, Routing", body_style), Paragraph("FastAPI, Uvicorn, Python Requests, Jinja2", body_style)],
        [Paragraph("<b>Weather & Agronomy</b>", body_style), Paragraph("REST API Integration, Predictive Modeling, Fungal Growth Risk Algorithms", body_style), Paragraph("Open-Meteo REST API, JSON Parsers", body_style)],
        [Paragraph("<b>Multilingual & Audio</b>", body_style), Paragraph("I18n/L10n Systems, Text-To-Speech (TTS), BCP-47 Speech Synthesis Mapping", body_style), Paragraph("Web Speech API, SpeechSynthesisUtterance", body_style)],
        [Paragraph("<b>Frontend Development</b>", body_style), Paragraph("Modern UI/UX, Glassmorphism CSS, Drag-and-Drop File API, Async Fetch", body_style), Paragraph("HTML5, CSS3, JavaScript ES6+, FontAwesome", body_style)],
        [Paragraph("<b>DevOps & Version Control</b>", body_style), Paragraph("Git Workflows, GitHub OAuth/PAT Authentication, Process Automation", body_style), Paragraph("Git, GitHub API, Python Subprocess", body_style)]
    ]

    t = Table(table_data, colWidths=[120, 220, 180])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#e2e8f0")),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t)

    story.append(Spacer(1, 14))

    # SECTION 4: HOW WE BUILT THIS PROJECT (WORKFLOW)
    story.append(Paragraph("4. Step-by-Step Implementation Workflow", h1_style))
    story.append(Paragraph("1. <b>Agronomic Taxonomy & Knowledge Base:</b> Structured 25+ diseases with symptoms, organic remedies (*Trichoderma*, Neem oil), and chemical fungicides (Mancozeb, Copper Oxychloride) with exact per-acre dosages.", bullet_style))
    story.append(Paragraph("2. <b>Computer Vision Classifier Engine:</b> Developed <code>backend/ml_engine.py</code> to extract HSV color masks, compute necrotic spot ratios, and calculate diagnostic confidence scores.", bullet_style))
    story.append(Paragraph("3. <b>Live Weather Integration:</b> Built <code>backend/weather_advisory.py</code> connecting to Open-Meteo API for real-time temperature, humidity, and 7-day precipitation forecasts.", bullet_style))
    story.append(Paragraph("4. <b>Multilingual & Voice Engine:</b> Implemented <code>backend/translator_tts.py</code> supporting Telugu, Hindi, Tamil, Kannada, Marathi, Bengali, and English with audio speech scripts.", bullet_style))
    story.append(Paragraph("5. <b>FastAPI Web Server & Webhooks:</b> Created REST endpoints (<code>/api/detect</code>, <code>/api/weather</code>, <code>/api/whatsapp/twilio</code>) in <code>backend/app.py</code>.", bullet_style))
    story.append(Paragraph("6. <b>Frontend Dashboard:</b> Designed a modern glassmorphism web interface with drag-and-drop scanner, live weather radar, WhatsApp simulator, and audio player.", bullet_style))

    story.append(PageBreak()) # Move Q&A to fresh page for clean reading

    # SECTION 5: INTERVIEW QUESTIONS & PERFECT ANSWERS
    story.append(Paragraph("5. Masterclass Interview Questions & Answers", h1_style))

    story.append(Paragraph("Q1: Why did you choose FastAPI instead of Flask or Django?", q_style))
    story.append(Paragraph("<b>Answer:</b> FastAPI was chosen because of its native support for asynchronous programming (<code>async/await</code>), high performance (powered by Starlette and Pydantic), automatic OpenAPI/Swagger documentation generation, and built-in type validation for multipart file uploads.", body_style))

    story.append(Paragraph("Q2: How does your vision model calculate disease severity?", q_style))
    story.append(Paragraph("<b>Answer:</b> The vision engine analyzes image color spaces by thresholding necrotic leaf tissue (brown/black blighted spots) and chlorotic yellowing against total leaf area. The ratio of affected pixels determines whether the infection is Early Stage (&lt;15%), Moderate Stage (15-40%), or Severe Stage (&gt;40%).", body_style))

    story.append(Paragraph("Q3: How does the weather advisory prevent crop loss?", q_style))
    story.append(Paragraph("<b>Answer:</b> Many fungal pathogens (like Late Blight or Rice Blast) require high relative humidity (&gt;75%) and leaf wetness to germinate. By integrating Open-Meteo weather forecasts, our system calculates a fungal risk index and alerts farmers to apply protective contact fungicides BEFORE rain starts, preventing spores from spreading.", body_style))

    story.append(Paragraph("Q4: How does the Text-to-Speech (TTS) audio readout work for illiterate farmers?", q_style))
    story.append(Paragraph("<b>Answer:</b> We integrated the browser-native Web Speech API. When a diagnosis is generated, the backend constructs a spoken narrative script in the farmer's selected language (e.g., Telugu). The frontend passes this text to <code>SpeechSynthesisUtterance</code> with the appropriate BCP-47 language tag (e.g., <code>te-IN</code>) to speak instructions out loud.", body_style))

    story.append(Paragraph("Q5: How does the WhatsApp integration process real farmer messages?", q_style))
    story.append(Paragraph("<b>Answer:</b> We built a Twilio / WhatsApp Business API Webhook endpoint at <code>/api/whatsapp/twilio</code>. When a farmer sends a photo on WhatsApp, Twilio sends an HTTP POST request to our server containing the media URL. Our backend downloads the image, runs AI leaf diagnosis, fetches local weather data, translates the report, and returns a formatted TwiML XML response card directly to the WhatsApp chat.", body_style))

    story.append(Paragraph("Q6: How would you scale this system for millions of farmers?", q_style))
    story.append(Paragraph("<b>Answer:</b> To handle high concurrent loads, I would: 1) Containerize the FastAPI application using Docker and deploy on Kubernetes with Horizontal Pod Autoscaling (HPA); 2) Offload ML image inference to a GPU microservice or ONNX Runtime; 3) Implement Redis caching for Open-Meteo weather responses to reduce external API calls; and 4) Use Celery/RabbitMQ background workers for async WhatsApp message processing.", body_style))

    # Build PDF Document
    doc.build(story)
    print(f"PDF successfully generated: {PDF_FILENAME}")

if __name__ == "__main__":
    build_pdf()
