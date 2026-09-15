import os
import urllib.request
from PIL import Image
import customtkinter as ctk

# Ensure assets directory exists
ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

def load_icon(name, color="A3A3A3", size=48):
    """
    Downloads an icon from Icons8 if it doesn't exist, and returns a CTkImage.
    `name` should be a valid Icons8 ios-glyphs icon name (e.g., 'settings').
    """
    # Request a 2x size image for high-DPI sharpness
    img_size = size * 2
    filename = f"{name}_{color}_{img_size}.png"
    filepath = os.path.join(ASSETS_DIR, filename)
    
    if not os.path.exists(filepath):
        # Icons8 expects the hex code without the #
        color_code = color.lstrip("#")
        url = f"https://img.icons8.com/ios-glyphs/{img_size}/{color_code}/{name}.png"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                with open(filepath, 'wb') as f:
                    f.write(response.read())
        except Exception as e:
            print(f"Failed to download icon {name}: {e}")
            img = Image.new('RGBA', (img_size, img_size), color=(0,0,0,0))
            img.save(filepath)
            
    img = Image.open(filepath)
    # The logical size is size x size, but it is backed by a 2x higher res image
    return ctk.CTkImage(light_image=img, dark_image=img, size=(size, size))
