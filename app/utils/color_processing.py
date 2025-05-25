from PIL import Image 

try:
    from PIL.Image import Quantize as PillowQuantize
except ImportError:
    PillowQuantize = None

def extract_palette(image_path, num_colors=10, resize_width=200):
    """
    Extracts the most common colors from an image using Pillow's quantization.

    Args:
        image_path (str): Path to the image file.
        num_colors (int): The desired number of colors in the palette.
        resize_width (int): Width to resize the image to for faster processing.
                            Set to None to disable resizing.

    Returns:
        list: A list of dictionaries, where each dictionary contains
              {'hex': '#RRGGBB', 'rgb': (R, G, B)} for a color.
              Returns an empty list if an error occurs.
    """
    try:
        img = Image.open(image_path)
        img = img.convert('RGB')

        if resize_width:
            current_width, current_height = img.size
            if current_width > resize_width:
                ratio = resize_width / float(current_width)
                new_height = int(float(current_height) * ratio)
                img = img.resize((resize_width, new_height), Image.Resampling.LANCZOS)

        quantized_img = None
        try:
            method_arg = PillowQuantize.LIBIMAGEQUANT if PillowQuantize and hasattr(PillowQuantize, 'LIBIMAGEQUANT') else 'libimagequant'
            quantized_img = img.quantize(colors=num_colors, method=method_arg, dither=Image.Dither.NONE)
        except ValueError:
            try:
                method_arg = PillowQuantize.MEDIANCUT if PillowQuantize and hasattr(PillowQuantize, 'MEDIANCUT') else 'mediancut'
                quantized_img = img.quantize(colors=num_colors, method=method_arg, dither=Image.Dither.NONE)
            except ValueError:
                try:
                    quantized_img = img.quantize(colors=num_colors, dither=Image.Dither.NONE)
                except Exception as e_default:
                    print(f"DEBUG: Default Pillow quantization also failed: {e_default}")
                    return []
            except Exception as e_other_median:
                 print(f"DEBUG: An unexpected error occurred during MEDIANCUT quantization: {e_other_median}.")
                 return []
        except Exception as e_other_lib:
            print(f"DEBUG: An unexpected error occurred during LIBIMAGEQUANT quantization: {e_other_lib}. Trying MEDIANCUT as fallback.")
            try:
                method_arg = PillowQuantize.MEDIANCUT if PillowQuantize and hasattr(PillowQuantize, 'MEDIANCUT') else 'mediancut'
                quantized_img = img.quantize(colors=num_colors, method=method_arg, dither=Image.Dither.NONE)
            except Exception as e_fallback_median:
                print(f"DEBUG: MEDIANCUT fallback also failed: {e_fallback_median}.")
                return []

        if quantized_img is None:
            return []

        palette_rgb_flat = quantized_img.getpalette()
        if not palette_rgb_flat:
            return []

        dominant_colors_info = quantized_img.getcolors(maxcolors=num_colors * 2)
        if not dominant_colors_info:
            return []

        extracted_colors = []
        for i in range(min(num_colors, len(dominant_colors_info))):
            _count, palette_index = dominant_colors_info[i]
            if (palette_index * 3 + 2) < len(palette_rgb_flat):
                r = palette_rgb_flat[palette_index * 3]
                g = palette_rgb_flat[palette_index * 3 + 1]
                b = palette_rgb_flat[palette_index * 3 + 2]
                color_info = {
                    'hex': f'#{r:02x}{g:02x}{b:02x}',
                    'rgb': (r, g, b)
                }
                extracted_colors.append(color_info)
            else:
                break

        return extracted_colors

    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return []
    except Exception as e:
        print(f"Error processing image {image_path} (outer try-except): {e}")
        return []