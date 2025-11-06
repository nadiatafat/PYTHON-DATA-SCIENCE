import numpy as np
from load_image import ft_display_pil


def ft_invert(array) -> np.ndarray:
    """
    Invert the colors of the image.
    """
    inverted = 255 - array
    ft_display_pil(inverted)
    return inverted


def ft_red(array) -> np.ndarray:
    """
    Apply a red filter to the image.
    """
    red = array.copy() * np.array([1., 0., 0.], dtype=np.float32)
    red = red.astype(np.uint8)
    ft_display_pil(red)
    return red


def ft_green(array) -> np.ndarray:
    """
    Apply a green filter to the image.
    """
    green = array.copy()
    green[:, :, 0] = array[:, :, 0] - array[:, :, 0]
    green[:, :, 2] = array[:, :, 2] - array[:, :, 2]
    green = green.astype(np.uint8)
    ft_display_pil(green)
    return green


def ft_blue(array) -> np.ndarray:
    """
    Apply a blue filter to the image.
    """
    blue = np.zeros_like(array)
    blue[:, :, 2] = array[:, :, 2]
    blue = blue.astype(np.uint8)
    ft_display_pil(blue)
    return blue


def ft_grey(array) -> np.ndarray:
    """
    Convert the image to grayscale.
    """
    grey = array.copy()[:, :, 1].squeeze()
    grey = grey.astype(np.uint8)
    ft_display_pil(grey)
    return grey
