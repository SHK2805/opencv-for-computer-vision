import cv2

from src.io.image import IOImage
from src.utils.common import show_image


class Draw(IOImage):
    def __init__(self, path='../../data/images/image.png'):
        super().__init__(path)

    # line
    def draw_line(self, image=None, start=(0, 0), end=(100, 100), color=(255, 0, 0), thickness=2):
        if image is None:
            image = self.image
        return cv2.line(image, start, end, color, thickness)

    # rectangle
    def draw_rectangle(self, image=None, start=(0, 0), end=(100, 100), color=(0, 255, 0), thickness=2):
        if image is None:
            image = self.image
        return cv2.rectangle(image, start, end, color, thickness)

    # circle
    def draw_circle(self, image=None, center=(100, 100), radius=50, color=(0, 0, 255), thickness=2):
        if image is None:
            image = self.image
        return cv2.circle(image, center, radius, color, thickness)

    # text
    def draw_text(self, image=None, text='Hello World!',
                  org=(50, 50),
                  font=cv2.FONT_HERSHEY_SIMPLEX,
                  font_scale=1,
                  color=(255, 255, 255),
                  thickness=2):
        if image is None:
            image = self.image
        return cv2.putText(image, text, org, font, font_scale, color, thickness)

    def draw_image(self):
        drawn_image = self.draw_line()
        drawn_image = self.draw_rectangle(drawn_image)
        drawn_image = self.draw_circle(drawn_image)
        drawn_image = self.draw_text(drawn_image)
        return drawn_image

if __name__ == '__main__':
    draw = Draw()
    image = draw.read()
    # get the center of the image
    height, width = image.shape[:2]
    center = (width // 2, height // 2)
    center = (center[0] + 45, center[1] + 40)
    # draw a circle from the center
    drawn_image = draw.draw_circle(center=center, radius=100)
    # show the image
    show_image(drawn_image)