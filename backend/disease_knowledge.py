"""
Disease Knowledge Base for Regional Crop Disease Detection & Agricultural Advisory System.
Contains comprehensive PlantVillage taxonomy and regional crop disease remedies, remedies (organic & chemical),
dosage guidance, and weather risk correlations.
"""

DISEASE_DATABASE = {
    "Tomato___Late_blight": {
        "crop": "Tomato",
        "disease_name": "Late Blight (Phytophthora infestans)",
        "category": "Fungal / Oomycete",
        "severity_levels": {
            "early": "Water-soaked dark lesions on leaf tips or margins.",
            "moderate": "Large dark brown patches on leaves and stems with white mold underneath.",
            "severe": "Entire plant foliar collapse, rotting fruits, total yield threat."
        },
        "symptoms": [
            "Irregular water-soaked spots on leaves that rapidly enlarge into dark brown/purple lesions.",
            "White cottony fungal growth on underside of leaves under humid conditions.",
            "Dark brown firm rot on tomato fruits."
        ],
        "organic_remedies": [
            "Spray Bio-fungicide Trichoderma viride or Pseudomonas fluorescens @ 5g/liter.",
            "Apply 5% Neem Seed Kernel Extract (NSKE) or diluted copper soap every 7 days.",
            "Prune infected bottom leaves to increase airflow and remove leaf debris from field."
        ],
        "chemical_remedies": [
            "Spray Mancozeb 75% WP @ 2.5g/liter of water at first symptom appearance.",
            "For severe outbreak, spray Metalaxyl 8% + Mancozeb 64% WP @ 2g/liter.",
            "Alternate with Copper Oxychloride 50% WP @ 3g/liter."
        ],
        "preventive_actions": [
            "Avoid overhead irrigation; use drip irrigation to keep leaf canopy dry.",
            "Maintain 60cm row spacing to allow solar penetration and air circulation.",
            "Rotate tomato crop with non-solanaceous crops like maize, legumes, or pulses."
        ],
        "weather_risk_triggers": {
            "min_humidity": 75,
            "min_temp": 15,
            "max_temp": 26,
            "rain_sensitive": True,
            "warning": "High humidity (>75%) & moderate temps (18-24°C) favor explosive Late Blight spore multiplication."
        }
    },
    "Tomato___Early_blight": {
        "crop": "Tomato",
        "disease_name": "Early Blight (Alternaria solani)",
        "category": "Fungal",
        "severity_levels": {
            "early": "Small brown concentric ring spots on lower leaves.",
            "moderate": "Target-board leaf spots with yellow halo surrounding the lesion.",
            "severe": "Defoliation of lower leaves exposing fruits to sunscald."
        },
        "symptoms": [
            "Concentric rings ('target-board' pattern) inside dark brown spots.",
            "Yellowing around brown leaf spots starting on older lower leaves.",
            "Dark sunken spots near the fruit stem base."
        ],
        "organic_remedies": [
            "Spray Neem oil 3000 ppm @ 5ml/liter with mild soap solution.",
            "Apply bio-agent Bacillus subtilis @ 10g/liter on foliage.",
            "Mulch soil with straw to prevent fungal spores from splashing onto lower leaves."
        ],
        "chemical_remedies": [
            "Spray Chlorothalonil 75% WP @ 2g/liter of water.",
            "Apply Azoxystrobin 23% SC @ 1ml/liter for quick curative action.",
            "Folicur (Tebuconazole 25.9% EC) @ 1.5ml/liter."
        ],
        "preventive_actions": [
            "Remove lower infected leaves up to 30 cm from ground level.",
            "Ensure proper soil potash & nitrogen balance; avoid excess nitrogen fertilizer.",
            "Sanitize field debris after harvest."
        ],
        "weather_risk_triggers": {
            "min_humidity": 70,
            "min_temp": 20,
            "max_temp": 32,
            "rain_sensitive": True,
            "warning": "Frequent dew drops or light showers paired with warm temperatures promote Early Blight spores."
        }
    },
    "Tomato___Yellow_Leaf_Curl_Virus": {
        "crop": "Tomato",
        "disease_name": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "category": "Viral (Transmitted by Whitefly Bemisia tabaci)",
        "severity_levels": {
            "early": "Slight upward curling and yellowing of young top leaf margins.",
            "moderate": "Severe leaf stunting, cupping, and interveinal chlorosis.",
            "severe": "Stunted bushy plant architecture with flower drop and no fruit set."
        },
        "symptoms": [
            "Upward curling, puckering, and yellowing of leaf margins.",
            "Stunted growth with thick leathery small leaves.",
            "Flower abortion leading to zero or deformed fruit development."
        ],
        "organic_remedies": [
            "Install Yellow Sticky Traps @ 20 traps/acre to catch vector whiteflies.",
            "Spray Neem Oil 10,000 ppm @ 3ml/liter or Fish Oil Rosin Soap @ 25g/liter.",
            "Cover young seedlings with 40-mesh insect-proof net nursery bed."
        ],
        "chemical_remedies": [
            "Spray Imidacloprid 17.8% SL @ 0.5ml/liter to control vector whiteflies.",
            "Apply Thiamethoxam 25% WG @ 0.3g/liter on lower leaf surfaces.",
            "Acetamiprid 20% SP @ 0.2g/liter."
        ],
        "preventive_actions": [
            "Remove and destroy infected virus reservoir plants immediately.",
            "Plant barrier crops like Maize, Bajra, or Sorghum around tomato field boundaries.",
            "Use TYLCV resistant hybrid tomato varieties (e.g. Arka Rakshak, Arka Samrat)."
        ],
        "weather_risk_triggers": {
            "min_humidity": 40,
            "min_temp": 25,
            "max_temp": 38,
            "rain_sensitive": False,
            "warning": "Hot, dry weather favors high whitefly vector population movement and rapid virus spread."
        }
    },
    "Tomato___Bacterial_spot": {
        "crop": "Tomato",
        "disease_name": "Bacterial Spot (Xanthomonas perforans)",
        "category": "Bacterial",
        "severity_levels": {
            "early": "Tiny water-soaked greasy dark spots on young leaves.",
            "moderate": "Brown angular leaf spots with yellow halos and fruit scab spots.",
            "severe": "Widespread leaf blighting and scabby unmarketable fruits."
        },
        "symptoms": [
            "Small water-soaked dark angular spots (<3mm) on foliage.",
            "Lesions turn brown, dry out, and drop out leaving shot-hole appearance.",
            "Raised black scabby spots on green fruits."
        ],
        "organic_remedies": [
            "Spray Streptomyces griseus bio-agent or copper hydroxide bio-formulations.",
            "Apply compost tea sprays to build phyllosphere microbial competition.",
            "Soak seeds in 50°C hot water for 25 minutes prior to sowing."
        ],
        "chemical_remedies": [
            "Spray Copper Oxychloride 50% WP @ 2.5g/liter + Streptocycline @ 0.1g/liter.",
            "Apply Kasugamycin 3% SL @ 2ml/liter."
        ],
        "preventive_actions": [
            "Use certified disease-free seeds.",
            "Avoid handling wet plants during weeding or harvesting.",
            "Disinfect farm implements with 10% bleach solution."
        ],
        "weather_risk_triggers": {
            "min_humidity": 80,
            "min_temp": 24,
            "max_temp": 35,
            "rain_sensitive": True,
            "warning": "Wind-driven rains and high humidity accelerate bacterial spread across crop rows."
        }
    },
    "Tomato___Healthy": {
        "crop": "Tomato",
        "disease_name": "Healthy Tomato Leaf",
        "category": "None (Healthy)",
        "severity_levels": {
            "early": "N/A", "moderate": "N/A", "severe": "N/A"
        },
        "symptoms": ["Leaf shows vibrant deep green color, smooth vein structure, and no visible lesions or discoloration."],
        "organic_remedies": ["Maintain regular organic compost (FYM/Vermi-compost) application @ 5 tons/acre."],
        "chemical_remedies": ["No pesticide application needed. Apply balanced N-P-K (19-19-19) micronutrient foliar spray @ 5g/liter."],
        "preventive_actions": [
            "Continue drip irrigation and periodic weeding.",
            "Monitor weekly with yellow sticky traps for early pest detection."
        ],
        "weather_risk_triggers": {
            "min_humidity": 0, "min_temp": 0, "max_temp": 50, "rain_sensitive": False,
            "warning": "Plant is healthy! Ensure good cultural practices to keep it protected."
        }
    },
    "Potato___Early_blight": {
        "crop": "Potato",
        "disease_name": "Potato Early Blight (Alternaria solani)",
        "category": "Fungal",
        "severity_levels": {
            "early": "Small brown spots on foliage.",
            "moderate": "Target-like dark rings with yellow leaf margins.",
            "severe": "Premature senescing of potato vines."
        },
        "symptoms": [
            "Dark brown to black concentric ring spots on older leaves.",
            "Leaves turn yellow and dry up, falling prematurely.",
            "Dark brown corky lesions on potato tubers."
        ],
        "organic_remedies": [
            "Foliar spray of Trichoderma harzianum @ 5g/liter.",
            "Apply 5% Neem seed kernel extract."
        ],
        "chemical_remedies": [
            "Spray Mancozeb 75% WP @ 2g/liter.",
            "Propiconazole 25% EC @ 1ml/liter."
        ],
        "preventive_actions": [
            "Plant certified seed tubers.",
            "Maintain balanced nitrogen fertilization to avoid plant stress."
        ],
        "weather_risk_triggers": {
            "min_humidity": 70, "min_temp": 20, "max_temp": 30, "rain_sensitive": True,
            "warning": "Warm temperatures paired with alternating wet and dry periods accelerate spore release."
        }
    },
    "Potato___Late_blight": {
        "crop": "Potato",
        "disease_name": "Potato Late Blight (Phytophthora infestans)",
        "category": "Fungal / Oomycete",
        "severity_levels": {
            "early": "Pale green or water-soaked spots near leaf tips.",
            "moderate": "Rapidly spreading dark brown lesions with white downy growth underneath.",
            "severe": "Complete vine rot with foul odor and tuber infection."
        },
        "symptoms": [
            "Water-soaked dark green/brown spots spreading rapidly across leaf surface.",
            "White cottony fungal bloom on undersides in morning dew.",
            "Reddish-brown dry rot inside potato tubers."
        ],
        "organic_remedies": [
            "Bordeaux mixture 1% spray preventive before cold wet spells.",
            "Copper hydroxide bio-fungicide @ 2.5g/liter."
        ],
        "chemical_remedies": [
            "Spray Cymoxanil 8% + Mancozeb 64% WP @ 2g/liter.",
            "Dimethomorph 50% WP @ 1g/liter."
        ],
        "preventive_actions": [
            "Earthing up potato ridges cleanly to shield tubers from falling spores.",
            "Destroy infected potato haulms 10 days before harvesting."
        ],
        "weather_risk_triggers": {
            "min_humidity": 85, "min_temp": 12, "max_temp": 22, "rain_sensitive": True,
            "warning": "CRITICAL RISK: Cool (12-20°C) rainy weather with >85% humidity causes epidemic crop loss."
        }
    },
    "Potato___Healthy": {
        "crop": "Potato",
        "disease_name": "Healthy Potato Leaf",
        "category": "None (Healthy)",
        "severity_levels": {"early": "N/A", "moderate": "N/A", "severe": "N/A"},
        "symptoms": ["Lush green potato leaf foliage without spots or blotches."],
        "organic_remedies": ["Apply Bio-fertilizers Azotobacter and PSB."],
        "chemical_remedies": ["No chemical treatment required."],
        "preventive_actions": ["Keep field weed-free and earthing up maintained."],
        "weather_risk_triggers": {"min_humidity": 0, "min_temp": 0, "max_temp": 50, "rain_sensitive": False, "warning": "Crop is in excellent healthy condition!"}
    },
    "Rice___Blast": {
        "crop": "Rice / Paddy",
        "disease_name": "Rice Blast (Magnaporthe oryzae)",
        "category": "Fungal",
        "severity_levels": {
            "early": "Small spindle-shaped spots on paddy leaves.",
            "moderate": "Diamond-shaped lesions with ash-gray center and brown border.",
            "severe": "Neck rot and panicle breakage ('rotten neck blast'), complete grain empty."
        },
        "symptoms": [
            "Spindle-shaped or eye-shaped lesions with grey center and reddish-brown margin.",
            "Blackening of neck node causing panicles to fall over.",
            "Chaffy unfilled paddy grains."
        ],
        "organic_remedies": [
            "Spray Pseudomonas fluorescens @ 10g/liter of water.",
            "Apply Panchagavya 3% or Cow urine 10% foliar spray."
        ],
        "chemical_remedies": [
            "Spray Tricyclazole 75% WP @ 0.6g/liter (Baan / Beam).",
            "Isoprothiolane 40% EC @ 1.5ml/liter.",
            "Kasugamycin 3% SL @ 2ml/liter."
        ],
        "preventive_actions": [
            "Avoid excess Nitrogen fertilizer application; apply split N doses.",
            "Maintain standing water in field during tillering.",
            "Use blast-resistant paddy varieties like Swarna, MTU 1010, or BPT 5204."
        ],
        "weather_risk_triggers": {
            "min_humidity": 85, "min_temp": 20, "max_temp": 28, "rain_sensitive": True,
            "warning": "Overcast days with high relative humidity and night dew favor rapid Blast spore germination."
        }
    },
    "Rice___Brown_Spot": {
        "crop": "Rice / Paddy",
        "disease_name": "Rice Brown Spot (Bipolaris oryzae)",
        "category": "Fungal (Associated with Soil Nutrient Deficiency)",
        "severity_levels": {
            "early": "Small circular sesame-seed brown spots on leaves.",
            "moderate": "Numerous brown spots coalescing on leaf blades and glumes.",
            "severe": "Seedling blight and poor grain filling."
        },
        "symptoms": [
            "Oval brown spots like sesame seeds with yellow halo.",
            "Dark brown spots on paddy husk and grain kernels."
        ],
        "organic_remedies": [
            "Seed treatment with Trichoderma viride @ 10g/kg seed.",
            "Foliar application of Vermicompost wash @ 10%."
        ],
        "chemical_remedies": [
            "Spray Mancozeb 75% WP @ 2.5g/liter or Propiconazole 25% EC @ 1ml/liter."
        ],
        "preventive_actions": [
            "Correct Potash (K) and Zinc (Zn) deficiencies in soil.",
            "Apply Zinc Sulfate @ 10kg/acre at puddling stage."
        ],
        "weather_risk_triggers": {
            "min_humidity": 75, "min_temp": 25, "max_temp": 35, "rain_sensitive": True,
            "warning": "Drought stress followed by heavy moisture encourages Brown Spot on weak nutrient-deficient crops."
        }
    },
    "Cotton___Bacterial_Blight": {
        "crop": "Cotton",
        "disease_name": "Cotton Bacterial Blight / Black Arm (Xanthomonas citri pv. malvacearum)",
        "category": "Bacterial",
        "severity_levels": {
            "early": "Angular dark green water-soaked spots on leaf undersides.",
            "moderate": "Blackening along leaf veins ('angular leaf spot') and stem lesions ('black arm').",
            "severe": "Boll rot and fiber staining."
        },
        "symptoms": [
            "Angular brown spots bounded by leaf veins.",
            "Black lesions on branches causing stem breakage (Black Arm).",
            "Water-soaked oily spots on cotton bolls."
        ],
        "organic_remedies": [
            "Spray Cow dung extract 5% supernatant liquid.",
            "Apply Neem seed oil @ 3%."
        ],
        "chemical_remedies": [
            "Spray Copper Oxychloride 50% WP @ 3g/liter + Streptocycline @ 0.1g/liter."
        ],
        "preventive_actions": [
            "Acid delinting of cotton seeds with sulphuric acid.",
            "Destroy crop residues after harvest."
        ],
        "weather_risk_triggers": {
            "min_humidity": 80, "min_temp": 28, "max_temp": 38, "rain_sensitive": True,
            "warning": "Warm wet windy weather spreads bacteria rapidly through rain splashes."
        }
    },
    "Corn_(Maize)___Common_rust": {
        "crop": "Corn / Maize",
        "disease_name": "Maize Common Rust (Puccinia sorghi)",
        "category": "Fungal",
        "severity_levels": {
            "early": "Small yellowish flecks on leaf surfaces.",
            "moderate": "Powdery reddish-brown pustules on upper and lower leaf surfaces.",
            "severe": "Pustules turn black, causing leaf death and reduced cob filling."
        },
        "symptoms": [
            "Elongated cinnamon-brown pustules that rupture the leaf epidermis.",
            "Golden powdery rust spores rubbing off on fingers."
        ],
        "organic_remedies": [
            "Foliar spray of Bio-fungicide Ampelomyces quisqualis @ 5g/liter."
        ],
        "chemical_remedies": [
            "Spray Mancozeb 75% WP @ 2.5g/liter or Hexaconazole 5% EC @ 2ml/liter."
        ],
        "preventive_actions": [
            "Plant rust-resistant maize hybrids.",
            "Avoid late season planting."
        ],
        "weather_risk_triggers": {
            "min_humidity": 70, "min_temp": 16, "max_temp": 25, "rain_sensitive": False,
            "warning": "Cool moist weather with high humidity promotes rust fungal pustule development."
        }
    },
    "Apple___Apple_scab": {
        "crop": "Apple",
        "disease_name": "Apple Scab (Venturia inaequalis)",
        "category": "Fungal",
        "severity_levels": {
            "early": "Olive green velvet spots on leaves.",
            "moderate": "Dark brown velvety lesions on fruit and leaves.",
            "severe": "Cracked distorted scabby fruits unfit for sale."
        },
        "symptoms": ["Olive green to dark brown scabby lesions on leaves and fruit peel."],
        "organic_remedies": ["Spray Lime Sulfur @ 2% before bud burst."],
        "chemical_remedies": ["Spray Captan 50% WP @ 2.5g/liter or Difenoconazole 25% EC @ 0.5ml/liter."],
        "preventive_actions": ["Rake and burn fallen orchard leaves in autumn."],
        "weather_risk_triggers": {"min_humidity": 80, "min_temp": 10, "max_temp": 24, "rain_sensitive": True, "warning": "Frequent spring rains trigger ascospore discharge."}
    }
}

# Fallback for unknown / general leaf diseases
DEFAULT_DISEASE_INFO = {
    "crop": "General Crop",
    "disease_name": "Foliar Leaf Spot / Nutritional Chlorosis",
    "category": "General Fungal / Nutrient Stress",
    "severity_levels": {
        "early": "Mild spotting or discoloration observed on leaf.",
        "moderate": "Noticeable leaf damage with localized necrosis.",
        "severe": "Significant foliar stress requiring immediate intervention."
    },
    "symptoms": [
        "Unusual leaf spots, yellowing, or structural curling observed on sample photo.",
        "Discoloration along leaf margins or veins."
    ],
    "organic_remedies": [
        "Spray 5% Neem Seed Kernel Extract (NSKE) or Neem Oil @ 5ml/liter.",
        "Apply bio-fertilizer Trichoderma viride or Pseudomonas @ 5g/liter."
    ],
    "chemical_remedies": [
        "Broad spectrum fungicide: Spray Mancozeb 75% WP @ 2g/liter of water.",
        "Micronutrient spray: Apply NPK 19-19-19 + Zinc + Iron foliar spray @ 5g/liter."
    ],
    "preventive_actions": [
        "Ensure proper soil drainage and avoid overwatering.",
        "Prune lower infected leaves to maintain ventilation."
    ],
    "weather_risk_triggers": {
        "min_humidity": 70, "min_temp": 15, "max_temp": 35, "rain_sensitive": True,
        "warning": "Keep monitoring soil moisture and atmospheric humidity."
    }
}


def get_disease_details(disease_key: str) -> dict:
    """Retrieve disease remedies and details by disease key."""
    return DISEASE_DATABASE.get(disease_key, DEFAULT_DISEASE_INFO)
