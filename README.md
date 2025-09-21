# Image to C Array Converter

A Python utility that converts PNG/JPEG images to C header files with pixel data arrays in various formats compatible with VGLite and embedded graphics libraries.

## Features

- **Multiple pixel formats supported**: RGB565, BGR565, ARGB8888, RGBA8888, RGB888, BGR888
- **VGLite compatibility**: Generated headers include VGLite format constants
- **Memory alignment**: Generated arrays include alignment attributes for optimal performance
- **Clean C output**: Well-formatted C headers with proper macros and documentation
- **Type safety**: Comprehensive type hints and error handling

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install Pillow numpy
```

### Install as Package (Optional)

```bash
pip install -e .
```

This allows you to use `image_to_c_array` command from anywhere.

## Usage

### Basic Usage

```bash
python image_to_c_array.py input_image.png
```

This converts `input_image.png` to `input_image.h` using the default BGR565 format.

### Advanced Usage

```bash
python image_to_c_array.py logo.png --format rgb565 --output logo_data.h
```

### Command Line Options

- `input`: Input image file (PNG, JPEG, BMP, etc.)
- `--format, -f`: Pixel format (default: bgr565)
- `--output, -o`: Output header file path (default: input_name.h)
- `--help, -h`: Show help message

## Supported Formats

| Format    | Bits/Pixel | Description                    | VGLite Constant     |
|-----------|------------|--------------------------------|---------------------|
| rgb565    | 16         | RGB565 (5-6-5 bit format)     | `VG_LITE_RGB565`      |
| bgr565    | 16         | BGR565 (5-6-5 bit format)     | `VG_LITE_BGR565`      |
| argb8888  | 32         | ARGB8888 (8-8-8-8 bit format) | `VG_LITE_ARGB8888`    |
| rgba8888  | 32         | RGBA8888 (8-8-8-8 bit format) | `VG_LITE_RGBA8888`    |
| rgb888    | 24         | RGB888 (8-8-8 bit format)     | `VG_LITE_RGB888`      |
| bgr888    | 24         | BGR888 (8-8-8 bit format)     | `VG_LITE_BGR888`      |

## Output Format

The generated C header file includes:

```c
// Auto-generated header with image metadata
#ifndef LOGO_IMG
#define LOGO_IMG

// Memory alignment attribute
#ifndef LOGO_IMG_ATTRIBUTE
#define LOGO_IMG_ATTRIBUTE __attribute__((aligned(128)))
#endif

// Image properties
#define LOGO_IMG_WIDTH             (64)
#define LOGO_IMG_HEIGHT            (64)
#define LOGO_IMG_BYTES_PER_PIXEL   (2)
#define LOGO_IMG_STRIDE            (LOGO_IMG_WIDTH * LOGO_IMG_BYTES_PER_PIXEL)
#define LOGO_IMG_FORMAT            (VG_LITE_BGR565)
#define LOGO_IMG_PIXEL_DATA        ((unsigned char*) logo_img_map)
#define LOGO_IMG_PIXEL_DATA_SIZE   (LOGO_IMG_WIDTH * LOGO_IMG_HEIGHT * LOGO_IMG_BYTES_PER_PIXEL)

// Pixel data array
const LOGO_IMG_ATTRIBUTE uint8_t logo_img_map[] = {
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    // ... pixel data continues
};

#endif /* LOGO_IMG */
```

## Usage in C/C++ Code

```c
#include "logo_data.h"

// Use the image data with VGLite
vg_lite_buffer_t image_buffer;
image_buffer.width = LOGO_IMG_WIDTH;
image_buffer.height = LOGO_IMG_HEIGHT;
image_buffer.stride = LOGO_IMG_STRIDE;
image_buffer.format = LOGO_IMG_FORMAT;
image_buffer.memory = (void*)LOGO_IMG_PIXEL_DATA;
```

## Examples

### Convert PNG to ARGB8888 with custom output
```bash
python image_to_c_array.py photo.png --format argb8888 --output photo_header.h
```

### Convert JPEG to RGB565
```bash
python image_to_c_array.py icon.jpg --format rgb565
```

### Batch conversion script
```bash
#!/bin/bash
for file in *.png; do
    python image_to_c_array.py "$file" --format bgr565
done
```

## Troubleshooting

### Common Issues

**"ModuleNotFoundError: No module named 'PIL'"**
```bash
pip install Pillow
```

**"Input file not found"**
- Check that the file path is correct
- Ensure the image file exists and is readable

**"Unsupported format"**
- Use one of the supported formats: rgb565, bgr565, argb8888, rgba8888, rgb888, bgr888

### Performance Tips

- Use RGB565 or BGR565 for smaller file sizes and faster loading
- Use ARGB8888 or RGBA8888 only when alpha channel is needed
- Consider image dimensions - larger images generate larger C arrays

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

### Development Setup

```bash
git clone https://github.com/shriram-m/image-to-c-array.git
cd image-to-c-array
pip install -e .
pip install -r requirements-dev.txt  # If available
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and changes.

## Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/shriram-m/image-to-c-array/issues) page
2. Create a new issue with detailed information
3. Include your command, expected behavior, and actual behavior

---

Created for embedded graphics development workflows.
