# Favicon Placeholder Files

This directory should contain your custom favicon files:

- `favicon.ico` - 32x32 favicon for browsers
- `favicon-16x16.png` - 16x16 PNG favicon
- `favicon-32x32.png` - 32x32 PNG favicon
- `apple-touch-icon.png` - 180x180 icon for Apple devices

## How to Generate Your Favicons

1. **Using Favicon.io** (https://favicon.io/):
   - Create a favicon from text, image, or emoji
   - Download the generated package
   - Replace the placeholder files in this directory

2. **Using RealFaviconGenerator** (https://realfavicongenerator.net/):
   - Upload your image (at least 260x260px)
   - Customize for different platforms
   - Download and extract to this directory

3. **Manual Creation**:
   - Design your icon in your favorite graphics editor
   - Export as PNG at 512x512px
   - Use an online converter to create .ico and various sizes

## Current Status
✓ **Complete** - Favicons have been generated from logo.png and the site is configured to use them.

## Generated Files

The following favicon files have been generated and are ready to use:

- `favicon.ico` - Multi-size ICO (16x16, 32x32, 48x48) for legacy browser support
- `favicon-16x16.png` - 16x16 PNG favicon for modern browsers
- `favicon-32x32.png` - 32x32 PNG favicon for modern browsers
- `apple-touch-icon.png` - 180x180 icon for Apple devices (iOS/iPadOS)
- `favicon-192x192.png` - 192x192 icon for Android devices
- `favicon-512x512.png` - 512x512 icon for Android/PWA high-resolution displays

## Regenerating Favicons

If you need to regenerate the favicons (e.g., after updating logo.png):

```bash
python3 generate_favicons.py
```

This will regenerate all favicon files from `assets/images/logo.png`.
