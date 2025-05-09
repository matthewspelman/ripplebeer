from PIL import Image
import os

def resize_image(input_path, output_path, size):
    try:
        with Image.open(input_path) as img:
            # Convert to RGBA if not already
            img = img.convert('RGBA')
            # Resize with high-quality resampling
            resized = img.resize(size, Image.Resampling.LANCZOS)
            # Save with transparency
            resized.save(output_path, 'PNG')
            print(f"Successfully created {output_path}")
    except Exception as e:
        print(f"Error processing {output_path}: {str(e)}")

# Sizes needed
sizes = {
    'favicon-16x16.png': (16, 16),
    'favicon-32x32.png': (32, 32),
    'apple-touch-icon.png': (180, 180),
    'android-chrome-192x192.png': (192, 192),
    'android-chrome-512x512.png': (512, 512)
}

# Create all sizes
for filename, size in sizes.items():
    resize_image('ripplebeercoplain.png', filename, size)

print("All favicon files created successfully!") 