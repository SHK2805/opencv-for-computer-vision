import cv2

from src.io.image import IOImage
from src.utils.common import show_image


class Contour(IOImage):
    def __init__(self, image_path='../../data/images/image.png'):
        super().__init__(image_path)
        self.processed_image = self.get_grey_image()

    def apply_threshold(self, threshold=127, image=None):
        if not image:
            image = self.processed_image
        _, thresh = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
        return thresh

    def get_contours(self, image=None):
        contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def get_contours_area(self, contours):
        return [cv2.contourArea(contour) for contour in contours]

    def draw_contours(self, contours, image=None):
        if not image:
            image = self.processed_image
        return cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2)

    def get_contours_image(self, contours, image=None):
        if not image:
            image = self.processed_image
        return cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2)

if __name__ == '__main__':
    contour = Contour()
    thresh = contour.apply_threshold()
    contours = contour.get_contours(thresh)
    print('Number of contours:', len(contours))
    contour_image = contour.draw_contours(contours)
    show_image(contour_image)