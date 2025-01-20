import os
import cv2

from src.utils.common import show_image


# read image
class IOImage:
    def __init__(self, path):
        if not path:
            raise ValueError('Path is empty')

        if not os.path.exists(path):
            raise FileNotFoundError(f"File {path} not found")

        self.path = path
        self.image = self.read()

    def get_image(self):
        return self.image

    def set_image(self, image):
        self.image = image

    def read(self):
        return cv2.imread(self.path)

    def write(self, image, path=None):
        if not path:
            path = self.path
        cv2.imwrite(path, image)

    def resize_image(self, width=None, height=None, image = None, interpolation=cv2.INTER_AREA):
        if not image:
            image = self.read()
        if width and height:
            return cv2.resize(image, (width, height), interpolation=interpolation)
        elif width:
            return cv2.resize(image, (width, image.shape[0]), interpolation=interpolation)
        elif height:
            return cv2.resize(image, (image.shape[1], height), interpolation=interpolation)
        else:
            return image

    def get_image_shape(self, image = None):
        if not image:
            image = self.read()
        return image.shape

    def get_image_dim(self, image = None):
        shape = self.get_image_shape(image)
        height = shape[0]
        width = shape[1]
        channels = shape[2]
        return height, width, channels


    def show(self):
        show_image(self.image)

if __name__ == '__main__':
    io = IOImage('../../data/images/image.png')
    # io.write(input_image, '../../images/image_new.png')
    io.show()