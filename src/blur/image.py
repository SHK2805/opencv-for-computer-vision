import os
import cv2

from src.io.image import IOImage
from src.utils.common import show_image


class BlurImage(IOImage):
    def __init__(self, path):
        super().__init__(path)
        self.blurred_image = self.read()

    def blur(self, kernel=(5, 5)):
        self.blurred_image = cv2.blur(self.image, kernel)
        return self.blurred_image

    def median_blur(self, kernel=5):
        self.blurred_image = cv2.medianBlur(self.image, kernel)
        return self.blurred_image

    def bilateral_filter(self, d=9, sigma_color=75, sigma_space=75):
        self.blurred_image = cv2.bilateralFilter(self.image, d, sigma_color, sigma_space)
        return self.blurred_image

    def gaussian_blur(self, kernel=(15, 15), sig_max=0):
        self.blurred_image = cv2.GaussianBlur(self.image, kernel, sig_max)
        return self.blurred_image

    def show(self):
        show_image(self.blurred_image)

    def show_all(self):
        top_grid = cv2.hconcat([self.image, self.blur()])
        bottom_grid = cv2.hconcat([self.median_blur(), self.bilateral_filter()])
        grid = cv2.vconcat([top_grid, bottom_grid])
        show_image(grid)


def remove_noise(image_path):
    blur1 = BlurImage(image_path)
    blur1.show_all()



if __name__ == '__main__':
    blur = BlurImage('../../data/images/image.png')
    # image = blur.blur()
    # image = blur.median_blur()
    # image = blur.bilateral_filter()
    # image = blur.gaussian_blur()
    # blur.show()
    # blur.show_all()
    remove_noise('../../data/images/salt_and_pepper_noise.jpg')
