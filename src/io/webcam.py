import os
import cv2

class IOWebcam:
    def __init__(self, camera=0):
        self.camera = camera
        self.video = self.read()

    def read(self):
        return cv2.VideoCapture(self.camera)

    def write(self, video, path=None):
        if not path:
            raise ValueError('Path is empty')
        cv2.imwrite(path, video)

    def show(self, video = None):
        if not video:
            video = self.video
        while True:
            # Capture frame-by-frame
            ret, frame = video.read()
            # if there are no more frames to read then break
            if not ret:
                break
            cv2.imshow(f"Cam: {self.camera}", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        video.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    io = IOWebcam()
    input_video = io.read()
    io.show(input_video)