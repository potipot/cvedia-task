# Create a Python function that returns a Numpy array representing an image with vertical black and white stripes.
# Please be sure to include tests proving your function works correctly for different inputs*
# Note: Only Numpy methods/operations are allowed and for loops are forbidden
# Note: The number of stripes and the image size should be configurable.
__all__ = ['draw_stripes']

import numpy as np
from PIL import Image
from math import floor, ceil


def pad_to_desired_width(x, desired_width):
    width, *_ = x.shape
    pads = (ceil((desired_width-width)/2), floor((desired_width-width)/2))
    return np.pad(x, pads, mode='edge')


def draw_stripes(width, height, n_stripes):
    base_stripes = np.arange(n_stripes) % 2
    repeats = n_stripes * [floor(width / n_stripes)]
    x = base_stripes.repeat(repeats)
    x = pad_to_desired_width(x, desired_width=width)

    x = np.tile(x, (height, 1))
    x = np.uint8(x * 255)

    # to highlight actual stripes (otherwise if last is white it won't be distinguishible)
    x[-1, :] = 0
    x[:, -1] = 0
    return Image.fromarray(x, 'L')


def test_draw_stripes():
    result = np.array(draw_stripes(4, 2, n_stripes=2))
    expected_result = np.array(
        [[0,   0, 255,   0],
         [0,   0,   0,   0]],
        dtype=np.uint8
    )

    result_2 = np.array(draw_stripes(4, 5, n_stripes=1))
    expected_result_2 = np.array(
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],
        dtype=np.uint8
    )
    assert (result == expected_result).all()
    assert (result_2 == expected_result_2).all()


if __name__ == '__main__':
    test_draw_stripes()
