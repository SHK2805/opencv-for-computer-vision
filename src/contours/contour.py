import cv2

from src.io.image import IOImage


class Contour(IOImage):
    def __init__(self, image):
        super().__init__(image)

    def find_contours(self):
        """
        Find contours in the image.
        """
        contours, _ = cv2.findContours(self.image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return contours