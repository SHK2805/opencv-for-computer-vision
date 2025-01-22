import os
import cv2
import numpy as np

from src.utils.common import show_image
from src.io.image import IOImage

class EdgeDetection(IOImage):
    def __init__(self, path='../../data/images/image.png'):
        super().__init__(path)
        self.edges = self.detect_edges()

    def detect_edges(self, min_val=100, max_val=200):
        return cv2.Canny(self.image, min_val, max_val)

    def dilate_edges(self,image=None, kernel_size=3, iterations=1):
        if image is None:
            image = self.edges
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        return cv2.dilate(image, kernel, iterations=iterations)

    def erode_edges(self, image=None, kernel_size=3, iterations=1):
        if image is None:
            image = self.edges
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        return cv2.erode(image, kernel, iterations=iterations)

    def show_edges(self):
        show_image(self.edges)

if __name__ == '__main__':
    edge_detection = EdgeDetection()
    # edge_detection.show()
    # edge_detection.show_edges()
    # dilate
    dilated_edges = edge_detection.dilate_edges()
    # show_image(dilated_edges)
    # erode
    eroded_edges = edge_detection.erode_edges(dilated_edges)
    # show_image(eroded_edges)
    # show images side by side
    show_image(np.hstack((dilated_edges, eroded_edges)))