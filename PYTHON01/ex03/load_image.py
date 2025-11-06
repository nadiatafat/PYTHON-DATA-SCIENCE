from PIL import Image, UnidentifiedImageError
import numpy as np
import matplotlib.pyplot as plt


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the given path, print its shape, and return
    its pixels as a NumPy array.
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


def ft_zoom(img: np.ndarray, center_x: int, center_y: int) -> np.ndarray:
    """
    Zoom into the image around a center point by slicing.
    """
    if not (isinstance(center_x, int) and isinstance(center_y, int)):
        raise ValueError("Zoom center positions need to be integers")

    if not (0 <= center_x < img.shape[1] and 0 <= center_y < img.shape[0]):
        raise ValueError("Zoom center out of bounds")
    x_min = max(center_x - 200, 0)
    x_max = min(center_x + 200, img.shape[1])
    y_min = max(center_y - 200, 0)
    y_max = min(center_y + 200, img.shape[0])

    zoomed = img[y_min:y_max, x_min:x_max, 1:2]

    print("shape is: ", zoomed.shape, "or", np.squeeze(zoomed).shape)
    return zoomed


def ft_display(img: np.ndarray):
    """
    Display an image (numpy array) with matplotlib.
    """
    plt.imshow(img,  cmap='gray')
    plt.xlabel("")
    plt.ylabel("")
    plt.show()


def ft_display_zoomed(animal: str, x: int, y: int) -> np.ndarray:
    """
    Display a zoomed image.
    """
    img = ft_load(animal)
    if img is None:
        return
    print(img)
    zoomed = ft_zoom(img, x, y)
    print(zoomed)
    ft_display(zoomed)
    return zoomed
