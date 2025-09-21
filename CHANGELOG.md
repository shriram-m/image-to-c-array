# Changelog

All notable changes to the Image to C Array Converter project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-09-19

### Added
- Initial release of Image to C Array Converter
- Support for multiple pixel formats:
  - RGB565 (16-bit, 5-6-5)
  - BGR565 (16-bit, 5-6-5) 
  - ARGB8888 (32-bit, 8-8-8-8)
  - RGBA8888 (32-bit, 8-8-8-8)
  - RGB888 (24-bit, 8-8-8)
  - BGR888 (24-bit, 8-8-8)
- VGLite compatibility with format constants
- Memory alignment attributes for optimal performance
- Command-line interface with argparse
- Comprehensive type hints for better code quality
- Error handling and validation
- Clean C header output with proper formatting
- Documentation and examples

### Features
- Convert PNG, JPEG, and other image formats to C arrays
- Configurable output file paths
- Generated headers include image metadata (width, height, format, etc.)
- Little-endian byte ordering for 16-bit formats
- Support for images with transparency (alpha channel)
- Professional C header format with include guards

### Documentation
- Comprehensive README with usage examples
- Installation instructions
- Format comparison table
- Troubleshooting guide
- Example files and directory structure
- MIT License for open source usage
- Contribution guidelines for community involvement

### Development
- Python package setup with setuptools
- Requirements file for easy dependency management
- Git ignore file for clean repository
- PEP 8 compliant code style
