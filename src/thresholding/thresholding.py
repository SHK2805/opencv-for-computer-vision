import cv2
import numpy as np

from src.blur.image import BlurImage
from src.color_spaces.colors import ConvertColorSpace, ColorSpaces
from src.io.image import IOImage
from src.utils.common import show_image


class Thresholding(IOImage):
    def __init__(self, image_path:str):
        super().__init__(image_path)
        self.image = ConvertColorSpace(image_path)
        if self.image is None:
            raise ValueError("Image not found or unable to read image.")

        self.image = self.image.convert_color_space(ColorSpaces.GRAY)
        self.threshold_image = self.image

    def get_threshold_image(self):
        return self.threshold_image

    def set_threshold_image(self, input_threshold_image):
        self.threshold_image = input_threshold_image

    def simple_threshold(self, thresh_value=127, max_value=255, threshold_type=cv2.THRESH_BINARY):
        """
        Applies simple thresholding to the image.

        Parameters:
        - thresh_value: Threshold value. Pixels above this value are set to max_value.
        - max_value: Maximum value assigned to the pixels that pass the threshold.
        - threshold_type: Type of thresholding to apply (e.g., cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV).

        Returns:
        - thresholded: The thresholded image.
        """
        _, self.threshold_image = cv2.threshold(self.image, thresh_value, max_value, threshold_type)
        return self.threshold_image

    def adaptive_threshold_mean(self, max_value=255, block_size=11, C=2):
        """
        Applies adaptive mean thresholding to the image.

        Parameters:
        - max_value: Maximum value assigned to the pixels that pass the threshold.
        - block_size: Size of the neighborhood area used to calculate the threshold value. Must be an odd number.
        - C: Constant subtracted from the mean to fine-tune the thresholding.

        Returns:
        - thresholded: The thresholded image.
        """
        self.threshold_image = cv2.adaptiveThreshold(self.image, max_value, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,
                                            block_size, C)
        return self.threshold_image

    def adaptive_threshold_gaussian(self, max_value=255, block_size=11, C=2):
        """
        Applies adaptive Gaussian thresholding to the image.

        Parameters:
        - max_value: Maximum value assigned to the pixels that pass the threshold.
        - block_size: Size of the neighborhood area used to calculate the threshold value. Must be an odd number.
        - C: Constant subtracted from the Gaussian-weighted mean to fine-tune the thresholding.

        Returns:
        - thresholded: The thresholded image.
        """
        self.threshold_image = cv2.adaptiveThreshold(self.image, max_value, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,
                                            block_size, C)
        return self.threshold_image

    def otsu_threshold(self):
        """
        Applies Otsu's binarization to the image.

        Parameters:
        - None

        Returns:
        - thresholded: The thresholded image using Otsu's method.
        """
        _, self.threshold_image = cv2.threshold(self.image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return self.threshold_image

    def combined_threshold(self):
        """
        Combines all thresholding techniques into a single image for comparison.

        Parameters:
        - None

        Returns:
        - combined: An image displaying the results of simple, adaptive mean, adaptive Gaussian, and Otsu's thresholding side by side.
        """
        simple_thresh = self.simple_threshold()
        adaptive_mean_thresh = self.adaptive_threshold_mean()
        adaptive_gaussian_thresh = self.adaptive_threshold_gaussian()
        otsu_thresh = self.otsu_threshold()

        top_stack = np.hstack((simple_thresh, adaptive_mean_thresh))
        bottom_stack = np.hstack((adaptive_gaussian_thresh, otsu_thresh))
        combined = np.vstack((top_stack, bottom_stack))
        self.threshold_image = combined
        return self.threshold_image

    def show(self):
        show_image(self.threshold_image)


# Usage example
if __name__ == "__main__":
    image_to_process: str = "../../data/images/image.png"
    threshold = Thresholding(image_to_process)
    blur = BlurImage(image_to_process)
    # threshold.simple_threshold()
    # threshold.adaptive_threshold_mean()
    # threshold.adaptive_threshold_gaussian()
    # threshold.otsu_threshold()
    # threshold.combined_threshold()
    # threshold.show()
    threshold_image = threshold.simple_threshold()
    blur.set_image(threshold_image)
    threshold_image_blur = blur.blur(kernel=(10, 10))
    threshold.set_image(threshold_image_blur)
    threshold_image = threshold.simple_threshold()
    threshold.set_image(threshold_image)
    threshold.show()

