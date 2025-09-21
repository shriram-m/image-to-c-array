#!/usr/bin/env python3
"""
Image to C Array Converter

A Python utility to convert PNG/JPEG images to C header files with pixel data arrays
in various formats (RGB565, BGR565, ARGB8888, etc.) compatible with VGLite and 
embedded graphics libraries.

Author: Shriram M
Created: 2025
License: MIT License

This tool is particularly useful for embedded graphics development where you need
to include image data directly in your C/C++ code as byte arrays.

Usage:
    python image_to_c_array.py input_image.png [options]

Options:
    --format FORMAT     Output format: rgb565, bgr565, argb8888, rgba8888, rgb888, bgr888
    --output OUTPUT     Output file path (default: input_name.h)
    --help              Show this help message

Example:
    python image_to_c_array.py logo.png --format bgr565 --output logo_data.h
"""

import argparse
import os
import sys
from typing import List, Tuple, Dict, Any
from PIL import Image
import numpy as np

# Format configurations
FORMATS: Dict[str, Dict[str, Any]] = {
    'rgb565': {
        'bytes_per_pixel': 2,
        'vg_lite_format': 'VG_LITE_RGB565',
        'description': 'RGB565 (16-bit, 5-6-5)'
    },
    'bgr565': {
        'bytes_per_pixel': 2,
        'vg_lite_format': 'VG_LITE_BGR565',
        'description': 'BGR565 (16-bit, 5-6-5)'
    },
    'argb8888': {
        'bytes_per_pixel': 4,
        'vg_lite_format': 'VG_LITE_ARGB8888',
        'description': 'ARGB8888 (32-bit, 8-8-8-8)'
    },
    'rgba8888': {
        'bytes_per_pixel': 4,
        'vg_lite_format': 'VG_LITE_RGBA8888',
        'description': 'RGBA8888 (32-bit, 8-8-8-8)'
    },
    'rgb888': {
        'bytes_per_pixel': 3,
        'vg_lite_format': 'VG_LITE_RGB888',
        'description': 'RGB888 (24-bit, 8-8-8)'
    },
    'bgr888': {
        'bytes_per_pixel': 3,
        'vg_lite_format': 'VG_LITE_BGR888',
        'description': 'BGR888 (24-bit, 8-8-8)'
    }
}


def rgb_to_rgb565(r: int, g: int, b: int) -> int:
    """Convert RGB888 values to RGB565 format.
    
    Args:
        r: Red component (0-255)
        g: Green component (0-255)
        b: Blue component (0-255)
        
    Returns:
        RGB565 value as 16-bit integer
    """
    r5 = (r >> 3) & 0x1F  # 5 bits for red
    g6 = (g >> 2) & 0x3F  # 6 bits for green  
    b5 = (b >> 3) & 0x1F  # 5 bits for blue
    rgb565 = (r5 << 11) | (g6 << 5) | b5
    return rgb565


def rgb_to_bgr565(r: int, g: int, b: int) -> int:
    """Convert RGB888 values to BGR565 format.
    
    Args:
        r: Red component (0-255)
        g: Green component (0-255) 
        b: Blue component (0-255)
        
    Returns:
        BGR565 value as 16-bit integer
    """
    r5 = (r >> 3) & 0x1F
    g6 = (g >> 2) & 0x3F
    b5 = (b >> 3) & 0x1F
    bgr565 = (b5 << 11) | (g6 << 5) | r5
    return bgr565


def convert_image_to_format(image: Image.Image, format_name: str) -> List[int]:
    """Convert PIL image to specified format bytes.
    
    Args:
        image: PIL Image object
        format_name: Target pixel format ('rgb565', 'bgr565', etc.)
        
    Returns:
        List of byte values representing the converted image data
        
    Raises:
        ValueError: If format_name is not supported
    """
    if format_name not in FORMATS:
        raise ValueError(f"Unsupported format: {format_name}")
    
    width, height = image.size
    
    # Convert to RGBA to handle all cases
    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    
    pixels = np.array(image)
    byte_data = []
    
    if format_name == 'rgb565':
        for row in pixels:
            for pixel in row:
                r, g, b, a = pixel
                # Ensure we're working with integers for bit operations
                r, g, b, a = int(r), int(g), int(b), int(a)
                rgb565_val = rgb_to_rgb565(r, g, b)
                # Store as little endian (low byte first) - this is the standard format
                byte_data.append(rgb565_val & 0xFF)
                byte_data.append((rgb565_val >> 8) & 0xFF)
    
    elif format_name == 'bgr565':
        for row in pixels:
            for pixel in row:
                r, g, b, a = pixel
                # Ensure we're working with integers for bit operations
                r, g, b, a = int(r), int(g), int(b), int(a)
                bgr565_val = rgb_to_bgr565(r, g, b)
                # Store as little endian (low byte first) - this is the standard format
                byte_data.append(bgr565_val & 0xFF)
                byte_data.append((bgr565_val >> 8) & 0xFF)
    
    elif format_name == 'argb8888':
        for row in pixels:
            for pixel in row:
                r, g, b, a = pixel
                # Ensure we're working with integers
                r, g, b, a = int(r), int(g), int(b), int(a)
                # ARGB format: Alpha, Red, Green, Blue
                byte_data.extend([a, r, g, b])
    
    elif format_name == 'rgba8888':
        for row in pixels:
            for pixel in row:
                r, g, b, a = pixel
                # Ensure we're working with integers
                r, g, b, a = int(r), int(g), int(b), int(a)
                # RGBA format: Red, Green, Blue, Alpha
                byte_data.extend([r, g, b, a])
    
    elif format_name == 'rgb888':
        for row in pixels:
            for pixel in row:
                r, g, b, a = pixel
                # Ensure we're working with integers
                r, g, b, a = int(r), int(g), int(b), int(a)
                # RGB format: Red, Green, Blue
                byte_data.extend([r, g, b])
    
    elif format_name == 'bgr888':
        for row in pixels:
            for pixel in row:
                r, g, b, a = pixel
                # Ensure we're working with integers
                r, g, b, a = int(r), int(g), int(b), int(a)
                # BGR format: Blue, Green, Red
                byte_data.extend([b, g, r])
    
    return byte_data

def generate_c_header(image_path: str, format_name: str, output_path: str) -> None:
    """Generate C header file with image data.
    
    Args:
        image_path: Path to input image file
        format_name: Target pixel format 
        output_path: Path for output C header file
        
    Raises:
        SystemExit: If image processing fails
    """
    try:
        # Load and process image
        image = Image.open(image_path)
        width, height = image.size
        
        # Get format info
        format_info = FORMATS[format_name]
        bytes_per_pixel = format_info['bytes_per_pixel']
        vg_lite_format = format_info['vg_lite_format']
        
        # Convert image to byte data
        byte_data = convert_image_to_format(image, format_name)
        
        # Generate macro prefix from filename
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        macro_prefix = base_name.upper().replace('-', '_').replace(' ', '_')
        array_name = base_name.lower().replace('-', '_').replace(' ', '_')
        
        # Generate C header content
        header_content = f"""/*
 * Auto-generated C header file for image: {os.path.basename(image_path)}
 * Format: {format_info['description']}
 * Dimensions: {width}x{height} pixels
 * Generated by image_to_c_array.py
 */

#ifndef {macro_prefix}_IMG
#define {macro_prefix}_IMG

#ifndef {macro_prefix}_IMG_ATTRIBUTE
#define {macro_prefix}_IMG_ATTRIBUTE         __attribute__((aligned(128)))
#endif /* {macro_prefix}_IMG_ATTRIBUTE */

#define {macro_prefix}_IMG_WIDTH             ({width})
#define {macro_prefix}_IMG_HEIGHT            ({height})
#define {macro_prefix}_IMG_BYTES_PER_PIXEL   ({bytes_per_pixel})
#define {macro_prefix}_IMG_STRIDE            ({macro_prefix}_IMG_WIDTH * {macro_prefix}_IMG_BYTES_PER_PIXEL)
#define {macro_prefix}_IMG_FORMAT            ({vg_lite_format})
#define {macro_prefix}_IMG_PIXEL_DATA        ((unsigned char*) {array_name}_img_map)
#define {macro_prefix}_IMG_PIXEL_DATA_SIZE   ({macro_prefix}_IMG_WIDTH * {macro_prefix}_IMG_HEIGHT * {macro_prefix}_IMG_BYTES_PER_PIXEL)

const {macro_prefix}_IMG_ATTRIBUTE uint8_t {array_name}_img_map[] =
{{"""
        num_bytes_in_row = 16
        num_bytes_in_row = width * bytes_per_pixel
        # Add pixel data in rows of 'num_bytes_in_row' bytes for readability
        for i in range(0, len(byte_data), num_bytes_in_row):
            line_data = byte_data[i:i+num_bytes_in_row]
            hex_values = [f"0x{byte:02X}" for byte in line_data]
            
            if i == 0:
                header_content += f"\n    {', '.join(hex_values)}"
            else:
                header_content += f",\n    {', '.join(hex_values)}"
        
        header_content += f"""
}};

#endif /* {macro_prefix}_IMG */
"""

        # Write to file
        with open(output_path, 'w') as f:
            f.write(header_content)
        
        print(f"✓ Successfully converted '{image_path}' to '{output_path}'")
        print(f"  Format: {format_info['description']}")
        print(f"  Dimensions: {width}x{height}")
        print(f"  Bytes per pixel: {bytes_per_pixel}")
        print(f"  Total data size: {len(byte_data)} bytes")
        
    except Exception as e:
        print(f"✗ Error processing '{image_path}': {str(e)}")
        sys.exit(1)

def main() -> None:
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description='Convert images to C header files with pixel data arrays',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Available formats:
{chr(10).join([f"  {fmt}: {info['description']}" for fmt, info in FORMATS.items()])}

Examples:
  python image_to_c_array.py logo.png --format bgr565
  python image_to_c_array.py icon.png --format argb8888 --output my_icon.h
        """
    )
    
    parser.add_argument('input', help='Input image file (PNG, JPEG, etc.)')
    parser.add_argument('--format', '-f', 
                       choices=list(FORMATS.keys()), 
                       default='bgr565',
                       help='Output pixel format (default: bgr565)')
    parser.add_argument('--output', '-o', 
                       help='Output header file path (default: input_name.h)')
    
    args = parser.parse_args()
    
    # Validate input file
    if not os.path.isfile(args.input):
        print(f"✗ Error: Input file '{args.input}' not found")
        sys.exit(1)
    
    # Determine output path
    if args.output:
        output_path = args.output
    else:
        base_name = os.path.splitext(args.input)[0]
        output_path = f"{base_name}.h"
    
    # Generate C header
    generate_c_header(args.input, args.format, output_path)

if __name__ == '__main__':
    main()
