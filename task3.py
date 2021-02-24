# Create a python method that takes a binary numpy array ( w x h x 1 ) and a sequence of box coordinates (x1,y1,x2,y2)
# as input and fills the input array with ones for the regions covered by the boxes in the sequence and zeros
# for everything else. Please provided the fastest possible implementation.*
__all__ = ['draw_boxes']
import numpy as np


def draw_boxes(a: np.ndarray, boxes):
    """Even though there is a loop, this should be faster than opencv, as calling `import cv2` also takes some time"""
    a = np.zeros_like(a, dtype=np.uint8)
    for box in boxes:
        x1, y1, x2, y2 = box
        x_slice = slice(x1, x2)
        y_slice = slice(y1, y2)
        a[x_slice, y_slice] = 1
    return a


def test_draw_boxes():
    w = np.random.rand(4, 6)
    boxes = [
        [0, 1, 2, 3],
        [3, 4, 4, 6]
    ]
    result = draw_boxes(w, boxes=boxes)
    expected_result = np.array(
        [[0, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 1]],
        dtype=np.uint8
    )
    assert (result == expected_result).all()


if __name__ == '__main__':
    test_draw_boxes()
