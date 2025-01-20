import os
import cv2

# read image
class IOImage:
    def __init__(self, path):
        if not path:
            raise ValueError('Path is empty')

        if not os.path.exists(path):
            raise FileNotFoundError('File not found')

        self.path = path

    def read(self):
        return cv2.imread(self.path)

    def write(self, image, path=None):
        if not path:
            path = self.path
        cv2.imwrite(path, image)


    def show(self, image):
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    io = IOImage('../../data/images/image.png')
    input_image = io.read()
    # io.write(input_image, '../../images/image_new.png')
    io.show(input_image)