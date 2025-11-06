from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    ft_load(path: str) -> np.ndarray
    Load an image from the given path, print its shape
    and return its pixels as a NumPy array.

    Supports JPEG/JPG formats only.
    Handles errors for missing files, unsupported formats
    or other unexpected issues.
    """

    try:
        img = Image.open(path)
    except FileNotFoundError:
        print(f"Error: file not found: {path}")
        return None
    except UnidentifiedImageError:
        print(f"Error: unsupported image format for file: {path}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

    if img.format not in ["JPEG", "JPG"]:
        print(f"Error: image format must be JPEG/JPG, not {img.format}")
        return None

    img = img.convert("RGB")
    arr = np.array(img)
    print("The shape of image is:", arr.shape)
    return arr
