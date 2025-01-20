import os
import cv2

from src.io.image import IOImage

def divide_image_into_patches():
    image = IOImage('../../data/images/image.png')
    img = image.read()
    image_copy = img.copy()
    imgheight = img.shape[0]
    imgwidth = img.shape[1]
    M = 128 # convert to 128x128 patches i.e. M = 128,
    N = 128 # convert to 128x128 patches i.e. M = 128
    x1 = 0
    y1 = 0

    for y in range(0, imgheight, M):
        for x in range(0, imgwidth, N):
            if (imgheight - y) < M or (imgwidth - x) < N:
                break

            y1 = y + M
            x1 = x + N

            # check whether the patch width or height exceeds the image width or height
            if x1 >= imgwidth and y1 >= imgheight:
                x1 = imgwidth - 1
                y1 = imgheight - 1
                # Crop into patches of size MxN
                tiles = image_copy[y:y + M, x:x + N]
                # Save each patch into file directory
                cv2.imwrite('saved_patches/' + 'tile' + str(x) + '_' + str(y) + '.jpg', tiles)
                cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
            elif y1 >= imgheight:  # when patch height exceeds the image height
                y1 = imgheight - 1
                # Crop into patches of size MxN
                tiles = image_copy[y:y + M, x:x + N]
                # Save each patch into file directory
                cv2.imwrite('saved_patches/' + 'tile' + str(x) + '_' + str(y) + '.jpg', tiles)
                cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
            elif x1 >= imgwidth:  # when patch width exceeds the image width
                x1 = imgwidth - 1
                # Crop into patches of size MxN
                tiles = image_copy[y:y + M, x:x + N]
                # Save each patch into file directory
                cv2.imwrite('saved_patches/' + 'tile' + str(x) + '_' + str(y) + '.jpg', tiles)
                cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
            else:
                # Crop into patches of size MxN
                tiles = image_copy[y:y + M, x:x + N]
                # Save each patch into file directory
                cv2.imwrite('saved_patches/' + 'tile' + str(x) + '_' + str(y) + '.jpg', tiles)
                cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
    image.show(img)


# resize image
def resize_image():
    image = IOImage('../../data/images/image.png')
    height, width, channels = image.get_image_dim()
    resized_image = image.resize_image(width=int(width/2), height=int(height/2))
    image.show(resized_image)

def crop_image():
    image_obj = IOImage('../../data/images/image.png')
    image = image_obj.read()
    print(image.shape)
    # cropped = img[start_row:end_row, start_col:end_col]
    cropped_image = image[200:380, 200:380]
    image_obj.show(cropped_image)


if __name__ == '__main__':
    divide_image_into_patches()


