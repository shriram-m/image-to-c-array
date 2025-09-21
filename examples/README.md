# Examples

This directory contains example usage of the image to C array converter tool.

## Running Examples

To run the examples, navigate to the examples directory and use the converter:

```bash
cd examples
python ../image_to_c_array.py sample_icon.png --format bgr565
python ../image_to_c_array.py sample_icon.jpg --format bgr888 --output sample_icon_bgr888.h
```

## Example Files

- `sample_icon.png` - A small 32x32 icon in PNG format for testing
- `sample_icon.jpg` - A small 32x32 icon in JPG format for testing
- `sample_icon.h` - Generated C header from the `sample_icon.png` icon (BGR565 format)
- `sample_icon_bgr888.h` - Generated C header from the `sample_icon.jpg` icon (BGR888 format)
- `README.md` - This file

## Creating Your Own Examples

1. Add your image files to this directory
2. Run the converter with different formats:
   ```bash
   python ../image_to_c_array.py your_image.png --format rgb565
   python ../image_to_c_array.py your_image.png --format argb8888
   ```
3. The generated `.h` files will contain the pixel data arrays

## Format Comparison

Try converting the same image with different formats to see the size differences:

```bash
# Small file size (16-bit)
python ../image_to_c_array.py sample_icon.png --format rgb565 --output icon_rgb565.h

# Medium file size (24-bit) 
python ../image_to_c_array.py sample_icon.png --format rgb888 --output icon_rgb888.h

# Large file size (32-bit with alpha)
python ../image_to_c_array.py sample_icon.png --format argb8888 --output icon_argb8888.h
```

Compare the file sizes and choose the appropriate format for your embedded application.
