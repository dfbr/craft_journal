#!/usr/bin/env python3
"""
Generate favicon files from logo.png
Requires: Pillow (PIL)
Install: pip install Pillow
"""

from PIL import Image
import os

# Configuration
SOURCE_IMAGE = "assets/images/logo.png"
OUTPUT_DIR = "assets/images"

# Favicon sizes to generate
FAVICON_SIZES = {
    "favicon-16x16.png": (16, 16),
    "favicon-32x32.png": (32, 32),
    "apple-touch-icon.png": (180, 180),
    "favicon-192x192.png": (192, 192),
    "favicon-512x512.png": (512, 512),
}

def resize_image(input_path, output_path, size):
    """Resize image to specified size with high-quality resampling."""
    try:
        with Image.open(input_path) as img:
            # Convert to RGBA if not already
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Resize with high-quality Lanczos resampling
            resized = img.resize(size, Image.Resampling.LANCZOS)
            
            # Save as PNG
            resized.save(output_path, 'PNG', optimize=True)
            print(f"✓ Created: {output_path} ({size[0]}x{size[1]})")
            
    except Exception as e:
        print(f"✗ Error creating {output_path}: {e}")

def create_ico(input_path, output_path, sizes=[(16, 16), (32, 32), (48, 48)]):
    """Create multi-size ICO file."""
    try:
        with Image.open(input_path) as img:
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Create list of images at different sizes
            icons = []
            for size in sizes:
                resized = img.resize(size, Image.Resampling.LANCZOS)
                icons.append(resized)
            
            # Save as ICO with multiple sizes
            icons[0].save(
                output_path,
                format='ICO',
                sizes=[(icon.width, icon.height) for icon in icons],
                append_images=icons[1:]
            )
            print(f"✓ Created: {output_path} (multi-size ICO)")
            
    except Exception as e:
        print(f"✗ Error creating ICO: {e}")

def main():
    print("Favicon Generator")
    print("=" * 50)
    
    # Check if source file exists
    if not os.path.exists(SOURCE_IMAGE):
        print(f"✗ Error: Source image not found: {SOURCE_IMAGE}")
        print("  Please ensure logo.png exists in assets/images/")
        return
    
    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    print(f"\nSource: {SOURCE_IMAGE}")
    print(f"Output: {OUTPUT_DIR}/\n")
    
    # Generate PNG favicons
    for filename, size in FAVICON_SIZES.items():
        output_path = os.path.join(OUTPUT_DIR, filename)
        resize_image(SOURCE_IMAGE, output_path, size)
    
    # Generate ICO file
    ico_path = os.path.join(OUTPUT_DIR, "favicon.ico")
    create_ico(SOURCE_IMAGE, ico_path)
    
    print("\n" + "=" * 50)
    print("✓ Favicon generation complete!")
    print("\nGenerated files:")
    print("  - favicon.ico (16x16, 32x32, 48x48)")
    print("  - favicon-16x16.png")
    print("  - favicon-32x32.png")
    print("  - apple-touch-icon.png (180x180)")
    print("  - favicon-192x192.png (Android)")
    print("  - favicon-512x512.png (Android/PWA)")
    print("\nAll files are in: " + OUTPUT_DIR)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nAborted by user")
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
