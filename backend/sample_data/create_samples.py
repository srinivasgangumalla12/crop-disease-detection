"""
Sample Leaf Photo Generator for Testing Crop Disease Scanner.
Generates sample leaf images: Tomato Late Blight, Tomato Early Blight, Tomato Yellow Leaf Curl, Rice Blast, and Healthy Leaf.
"""

import os
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

SAMPLES_DIR = os.path.dirname(os.path.abspath(__file__))


def create_healthy_leaf():
    """Generates a vibrant healthy green leaf image."""
    img = Image.new("RGB", (400, 400), (245, 248, 240))
    draw = ImageDraw.Draw(img)
    
    # Leaf outline (oval/pointed shape)
    draw.ellipse([80, 50, 320, 350], fill=(34, 139, 34), outline=(20, 90, 20), width=4)
    # Leaf vein structure
    draw.line([200, 50, 200, 350], fill=(144, 238, 144), width=5)
    for y in range(80, 320, 30):
        draw.line([200, y, 120, y - 30], fill=(144, 238, 144), width=3)
        draw.line([200, y, 280, y - 30], fill=(144, 238, 144), width=3)
        
    img = img.filter(ImageFilter.GaussianBlur(1))
    img.save(os.path.join(SAMPLES_DIR, "tomato_healthy.jpg"))


def create_late_blight_leaf():
    """Generates a leaf with dark brown water-soaked Late Blight lesions."""
    img = Image.new("RGB", (400, 400), (240, 242, 235))
    draw = ImageDraw.Draw(img)
    
    # Darker yellowish-green leaf
    draw.ellipse([80, 50, 320, 350], fill=(46, 117, 46), outline=(20, 80, 20), width=4)
    draw.line([200, 50, 200, 350], fill=(120, 200, 120), width=4)
    
    # Large dark brown water-soaked late blight patches
    draw.ellipse([100, 100, 220, 210], fill=(60, 40, 25), outline=(40, 25, 15))
    draw.ellipse([180, 180, 300, 290], fill=(50, 30, 20), outline=(35, 20, 10))
    draw.ellipse([130, 240, 210, 320], fill=(55, 35, 22), outline=(38, 22, 12))
    
    # White cottony downy mildew spots on edges
    draw.ellipse([110, 120, 140, 150], fill=(230, 235, 225))
    draw.ellipse([210, 210, 240, 235], fill=(225, 230, 220))
    
    img = img.filter(ImageFilter.GaussianBlur(1.5))
    img.save(os.path.join(SAMPLES_DIR, "tomato_late_blight.jpg"))


def create_early_blight_leaf():
    """Generates a leaf with concentric target-board spots and yellow halos."""
    img = Image.new("RGB", (400, 400), (240, 242, 235))
    draw = ImageDraw.Draw(img)
    
    # Leaf background
    draw.ellipse([80, 50, 320, 350], fill=(50, 130, 50), outline=(25, 80, 25), width=4)
    draw.line([200, 50, 200, 350], fill=(130, 210, 130), width=4)
    
    # Target spots with yellow halos
    # Spot 1
    draw.ellipse([110, 110, 190, 190], fill=(220, 200, 50)) # Yellow halo
    draw.ellipse([125, 125, 175, 175], fill=(90, 50, 25)) # Brown spot center
    draw.ellipse([140, 140, 160, 160], fill=(40, 25, 15)) # Dark core
    
    # Spot 2
    draw.ellipse([200, 180, 280, 260], fill=(225, 205, 55))
    draw.ellipse([215, 195, 265, 245], fill=(85, 45, 20))
    
    img = img.filter(ImageFilter.GaussianBlur(1.2))
    img.save(os.path.join(SAMPLES_DIR, "tomato_early_blight.jpg"))


def create_yellow_curl_leaf():
    """Generates a leaf with yellowing margins and curling structure."""
    img = Image.new("RGB", (400, 400), (245, 245, 240))
    draw = ImageDraw.Draw(img)
    
    # Yellowish leaf
    draw.ellipse([90, 60, 310, 340], fill=(210, 200, 40), outline=(150, 130, 20), width=4)
    draw.ellipse([130, 90, 270, 310], fill=(90, 160, 40))
    
    img = img.filter(ImageFilter.GaussianBlur(1))
    img.save(os.path.join(SAMPLES_DIR, "tomato_yellow_leaf_curl.jpg"))


def create_rice_blast_leaf():
    """Generates a paddy rice leaf with spindle-shaped blast spots."""
    img = Image.new("RGB", (400, 400), (245, 245, 240))
    draw = ImageDraw.Draw(img)
    
    # Slender paddy leaf blade
    draw.polygon([(170, 20), (230, 20), (240, 380), (160, 380)], fill=(40, 140, 40), outline=(20, 80, 20))
    draw.line([200, 20, 200, 380], fill=(120, 210, 120), width=3)
    
    # Spindle / Eye shaped blast spots
    draw.ellipse([175, 100, 225, 150], fill=(160, 60, 30)) # Brown border
    draw.ellipse([185, 110, 215, 140], fill=(200, 200, 190)) # Gray center
    
    draw.ellipse([180, 220, 230, 270], fill=(150, 55, 25))
    draw.ellipse([190, 230, 220, 260], fill=(195, 195, 185))
    
    img.save(os.path.join(SAMPLES_DIR, "rice_blast.jpg"))


if __name__ == "__main__":
    create_healthy_leaf()
    create_late_blight_leaf()
    create_early_blight_leaf()
    create_yellow_curl_leaf()
    create_rice_blast_leaf()
    print("Sample leaf photos generated successfully in backend/sample_data!")
