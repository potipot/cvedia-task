# Create a Python function that takes as an input a NumPy array with the shape width x height representing a depth
# image where each value represents the distance in meters from a sensor as floating-point numbers and outputs
# a grayscale image representing the normalized depth where a black pixel is the closest point and a white pixel
# is the farthest one. Please also include a test method that validates the logic on a randomly initialized NumPy array.
__all__ = ['distance_to_depth_image']

import numpy as np
from PIL import Image


def normalize(x: np.ndarray):
    maxval = x.max()
    minval = x.min()
    return np.uint8((x-minval)/maxval*255)


def distance_to_depth_image(x: np.ndarray):
    x = normalize(x)
    return Image.fromarray(x, 'L')


def test_distance_to_depth_image():
    width = 600
    height = 400
    x = np.random.rand(width, height)
    result = distance_to_depth_image(x)
    assert isinstance(result, Image.Image)


if __name__ == '__main__':
    test_distance_to_depth_image()

