"""
Multilingual Translator and Text-To-Speech (TTS) Voice Synthesis Module.
Translates agricultural diagnoses, remedies, and weather alerts into Telugu, Hindi, Tamil, Kannada, Marathi, Bengali, and English.
Provides speech scripts for farmer audio readout.
"""

SUPPORTED_LANGUAGES = {
    "en": {"name": "English", "native": "English", "bcp47": "en-US"},
    "te": {"name": "Telugu", "native": "తెలుగు", "bcp47": "te-IN"},
    "hi": {"name": "Hindi", "native": "हिन्दी", "bcp47": "hi-IN"},
    "ta": {"name": "Tamil", "native": "தமிழ்", "bcp47": "ta-IN"},
    "kn": {"name": "Kannada", "native": "ಕನ್ನಡ", "bcp47": "kn-IN"},
    "mr": {"name": "Marathi", "native": "मराठी", "bcp47": "mr-IN"},
    "bn": {"name": "Bengali", "native": "বাংলা", "bcp47": "bn-IN"}
}

# Regional Agricultural Translations Dictionary
DICTIONARY = {
    "te": {
        "crop": "పంట",
        "disease": "తెగులు / వ్యాధి",
        "severity": "తీవ్రత స్థాయి",
        "confidence": "ఖచ్చితత్వం",
        "symptoms": "లక్షణాలు",
        "organic_remedies": "సేంద్రీయ నివారణ చర్యలు (Organic Cures)",
        "chemical_remedies": "రసాయన మందుల వాడకం (Chemical Fungicides)",
        "preventive_actions": "ముందస్తు జాగ్రత్తలు",
        "weather_advisory": "వాతావరణ హెచ్చరిక & సలహా",
        "whatsapp_greeting": "నమస్కారం రైతు సోదరా! మీ పంట ఫోటో విశ్లేషణ సిద్ధంగా ఉంది.",
        "healthy_msg": "మీ పంట ఆరోగ్యంగా ఉంది! ఏ తెగులు లక్షణాలు కనిపించలేదు.",
        "high_risk": "అధిక ప్రమాదం (వెంటనే మందు పిచికారీ చేయండి)",
        "moderate_risk": "మధ్యస్థ ప్రమాదం (పర్యవేక్షించండి)"
    },
    "hi": {
        "crop": "फ़सल",
        "disease": "रोग / बीमारी",
        "severity": "गंभीरता स्तर",
        "confidence": "सटीकता",
        "symptoms": "लक्षण",
        "organic_remedies": "जैविक रोकथाम (Organic Remedies)",
        "chemical_remedies": "रासायनिक कीटनाशक दवाइयां (Chemical Spray)",
        "preventive_actions": "बचाव के उपाय",
        "weather_advisory": "मौसम सलाह एवं अगली रणनीति",
        "whatsapp_greeting": "नमस्ते किसान भाई! आपकी फसल की फोटो जांच रिपोर्ट तैयार है।",
        "healthy_msg": "आपकी फसल बिल्कुल स्वस्थ है! कोई बीमारी नहीं पाई गई।",
        "high_risk": "उच्च जोखिम (तुरंत छिड़काव करें)",
        "moderate_risk": "मध्यम जोखिम"
    },
    "ta": {
        "crop": "பயிர்",
        "disease": "நோய்",
        "severity": "பாதிப்பு நிலை",
        "confidence": "துல்லியம்",
        "symptoms": "அறிகுறிகள்",
        "organic_remedies": "இயற்கை நிவாரணம் (Organic Remedies)",
        "chemical_remedies": "ரசாயன மருந்து தெளிப்பு (Chemical Remedies)",
        "preventive_actions": "முன்னெச்சரிக்கை நடவடிக்கைகள்",
        "weather_advisory": "வானிலை எச்சரிக்கை மற்றும் ஆலோசனை",
        "whatsapp_greeting": "வணக்கம் விவசாயி நண்பரே! உங்கள் பயிர் புகைப்பட பகுப்பாய்வு தயார்.",
        "healthy_msg": "உங்கள் பயிர் ஆரோக்கியமாக உள்ளது! நோய் எதுவும் கண்டறியப்படவில்லை.",
        "high_risk": "அதிக ஆபத்து",
        "moderate_risk": "மிதமான ஆபத்து"
    },
    "kn": {
        "crop": "ಬೆಳೆ",
        "disease": "ರೋಗ",
        "severity": "ತೀವ್ರತೆಯ ಮಟ್ಟ",
        "confidence": "ನಿಖರತೆ",
        "symptoms": "ಲಕ್ಷಣಗಳು",
        "organic_remedies": "ಸಾವಯವ ನಿವಾರಣೆ (Organic Remedies)",
        "chemical_remedies": "ರಾಸಾಯನಿಕ ಔಷಧ ಸಿಂಪಡಣೆ (Chemical Spray)",
        "preventive_actions": "ಮುನ್ನೆಚ್ಚರಿಕೆ ಕ್ರಮಗಳು",
        "weather_advisory": "ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ ಸಲಹೆ",
        "whatsapp_greeting": "ನಮಸ್ಕಾರ ರೈತ ಬಂಧುವೇ! ನಿಮ್ಮ ಬೆಳೆಯ ಫೋಟೋ ತಪಾಸಣೆ ವರದಿ ಸಿದ್ಧವಾಗಿದೆ.",
        "healthy_msg": "ನಿಮ್ಮ ಬೆಳೆ ಸಂಪೂರ್ಣ ಆರೋಗ್ಯಕರವಾಗಿದೆ!",
        "high_risk": "ಹೆಚ್ಚಿನ ಅಪಾಯ",
        "moderate_risk": "ಮಧ್ಯಮ ಅಪಾಯ"
    },
    "mr": {
        "crop": "पिक",
        "disease": "रोग",
        "severity": "तीव्रता पातळी",
        "confidence": "अचूकता",
        "symptoms": "लक्षणे",
        "organic_remedies": "जैविक उपाय (Organic Remedies)",
        "chemical_remedies": "रासायनिक औषध फवारणी (Chemical Spray)",
        "preventive_actions": "प्रतिबंधात्मक उपाय",
        "weather_advisory": "हवामान अंदाज आणि सल्ला",
        "whatsapp_greeting": "नमस्कार शेतकरी मित्र! तुमच्या पिकाचा फोटो तपासणी अहवाल तयार आहे.",
        "healthy_msg": "तुमचे पीक पूर्णपणे निरोगी आहे!",
        "high_risk": "उच्च धोका",
        "moderate_risk": "मध्यम धोका"
    },
    "bn": {
        "crop": "ফসল",
        "disease": "রোগ",
        "severity": "তীব্রতার মাত্রা",
        "confidence": "সঠিকতা",
        "symptoms": "লক্ষণ",
        "organic_remedies": "জৈব প্রতিকার (Organic Remedies)",
        "chemical_remedies": "রাসায়নিক স্প্রে (Chemical Remedies)",
        "preventive_actions": "সতর্কতামূলক পদক্ষেপ",
        "weather_advisory": "আবহাওয়ার পূর্বাভাস এবং পরামর্শ",
        "whatsapp_greeting": "নমস্কার কৃষক ভাই! আপনার ফসলের ছবি বিশ্লেষণ রিপোর্ট তৈরি।",
        "healthy_msg": "আপনার ফসল সম্পূর্ণ সুস্থ!",
        "high_risk": "উচ্চ ঝুঁকি",
        "moderate_risk": "মাঝারি ঝুঁকি"
    }
}


def translate_report(report_data: dict, lang_code: str = "te") -> dict:
    """
    Translates diagnosis report and remedy suggestions into farmer's language.
    """
    if lang_code not in SUPPORTED_LANGUAGES or lang_code == "en":
        # Default English
        translated = dict(report_data)
        translated["audio_speech_text"] = generate_speech_script(report_data, "en")
        translated["selected_lang"] = SUPPORTED_LANGUAGES.get(lang_code, SUPPORTED_LANGUAGES["en"])
        return translated

    lang_dict = DICTIONARY.get(lang_code, {})
    crop_name = report_data.get("crop", "Crop")
    disease_name = report_data.get("disease_name", "Leaf Spot")

    # Create localized copy
    localized = dict(report_data)
    localized["labels"] = lang_dict
    localized["selected_lang"] = SUPPORTED_LANGUAGES[lang_code]

    # Generate native speech script for audio readout
    localized["audio_speech_text"] = generate_speech_script(report_data, lang_code)

    return localized


def generate_speech_script(report_data: dict, lang_code: str) -> str:
    """
    Generates a clear spoken narrative for the Text-to-Speech engine so the app TELLS the farmer.
    """
    crop = report_data.get("crop", "Crop")
    disease = report_data.get("disease_name", "Disease")
    severity = report_data.get("severity_level", "Moderate")
    organic_remedies = report_data.get("organic_remedies", [])
    chemical_remedies = report_data.get("chemical_remedies", [])
    weather_info = report_data.get("weather_advisory", {}).get("action_steps", [])

    org_text = organic_remedies[0] if organic_remedies else "Maintain field sanitation."
    chem_text = chemical_remedies[0] if chemical_remedies else "Consult local agricultural extension officer."
    weather_text = weather_info[0] if weather_info else "Check weather forecast daily."

    if lang_code == "te":
        if "Healthy" in disease or "Healthy" in severity:
            return f"నమస్కారం! మీ {crop} పంట ఆకు ఫోటోను విశ్లేషించాము. మీ పంట ఎంతో ఆరోగ్యంగా ఉంది. ఏ తెగులు లక్షణాలు కనిపించలేదు. ధన్యవాదాలు!"
        return (
            f"నమస్కారం రైతు సోదరా! మీ {crop} పంటలో {disease} తెగులు గుర్తించబడింది. "
            f"దీని తీవ్రత {severity}. "
            f"సేంద్రీయ నివారణ: {org_text}. "
            f"రసాయన నివారణ: {chem_text}. "
            f"వాతావరణ సలహా: {weather_text}."
        )
    elif lang_code == "hi":
        if "Healthy" in disease or "Healthy" in severity:
            return f"नमस्ते किसान भाई! आपकी {crop} की फसल बिल्कुल स्वस्थ है। कोई बीमारी नहीं पाई गई है।"
        return (
            f"नमस्ते किसान भाई! आपकी {crop} फसल में {disease} बीमारी पाई गई है। "
            f"इसकी गंभीरता {severity} है। "
            f"जैविक उपाय: {org_text}। "
            f"रासायनिक उपाय: {chem_text}। "
            f"मौसम की सलाह: {weather_text}।"
        )
    elif lang_code == "ta":
        return (
            f"வணக்கம்! உங்கள் {crop} பயிரில் {disease} கண்டறியப்பட்டுள்ளது. "
            f"இயற்கை தீர்வு: {org_text}. "
            f"மருந்து தெளிப்பு: {chem_text}."
        )
    elif lang_code == "kn":
        return (
            f"ನಮಸ್ಕಾರ! ನಿಮ್ಮ {crop} ಬೆಳೆಯಲ್ಲಿ {disease} ರೋಗ ಕಂಡುಬಂದಿದೆ. "
            f"ಸಾಕಷ್ಟು ನಿವಾರಣೆ: {org_text}. "
            f"ಔಷಧ ಸಿಂಪಡಣೆ: {chem_text}."
        )
    elif lang_code == "mr":
        return (
            f"नमस्कार! तुमच्या {crop} पिकावर {disease} रोगाचा प्रादुर्भाव झाला आहे. "
            f"उपाय: {org_text}. "
            f"फवारणी: {chem_text}."
        )
    elif lang_code == "bn":
        return (
            f"নমস্কার! আপনার {crop} ফসলে {disease} রোগ সনাক্ত হয়েছে। "
            f"জৈব প্রতিকার: {org_text}। "
            f"রাসায়নিক স্প্রে: {chem_text}।"
        )
    else: # English
        if "Healthy" in disease or "Healthy" in severity:
            return f"Hello farmer! Your {crop} leaf sample has been analyzed. The plant is healthy with no detected diseases!"
        return (
            f"Hello farmer! Diagnosis for your {crop} plant indicates {disease}. "
            f"Severity level is {severity}. "
            f"Recommended organic solution: {org_text}. "
            f"Recommended chemical spray: {chem_text}. "
            f"Weather action step: {weather_text}."
        )
