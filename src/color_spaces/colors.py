import enum
import os
import cv2

from src.io.image import IOImage
from src.utils.common import show_image


class ColorSpaces(enum.Enum):
    BGR = 0
    RGB = 1
    GRAY = 2
    HSV = 3
    LAB = 4
    YCrCb = 5
    XYZ = 6
    LUV = 7
    HLS = 8
    YUV = 9
    Grayscale = 10

class ConvertColorSpace(IOImage):
    def __init__(self, image_path: str):
        super().__init__(image_path)
        self.converted_image = self.image

    def convert_color_space(self, color_space: ColorSpaces):
        if color_space == ColorSpaces.RGB:
            return self.converted_image
        elif color_space == ColorSpaces.BGR:
            self.converted_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
            return self.converted_image
        elif color_space == ColorSpaces.GRAY:
            self.converted_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
            return self.converted_image
        elif color_space == ColorSpaces.HSV:
            self.converted_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2HSV)
            return self.converted_image
        elif color_space == ColorSpaces.LAB:
            self.converted_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2LAB)
            return self.converted_image
        elif color_space == ColorSpaces.YCrCb:
            self.converted_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2YCrCb)
            return self.converted_image
        elif color_space == ColorSpaces.XYZ:
            self.converted_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2XYZ)
            return self.converted_image
        elif color_space == ColorSpaces.LUV:
            self.converted_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2LUV)
            return self.converted_image
        elif color_space == ColorSpaces.HLS:
            self.converted_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2HLS)
            return self.converted_image
        elif color_space == ColorSpaces.YUV:
            self.converted_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2YUV)
            return self.converted_image
        elif color_space == ColorSpaces.Grayscale:
            self.converted_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
            return self.converted_image
        else:
            raise ValueError('Invalid color space')

    def show_colors(self):
        show_image(self.converted_image)

if __name__ == '__main__':
    input_image_path = '../../data/images/image.png'
    convert_color_space = ConvertColorSpace(input_image_path)

    convert_color_space.convert_color_space(ColorSpaces.BGR)
    convert_color_space.show_colors()

    convert_color_space.convert_color_space(ColorSpaces.GRAY)
    convert_color_space.show_colors()

    convert_color_space.convert_color_space(ColorSpaces.HSV)
    convert_color_space.show_colors()