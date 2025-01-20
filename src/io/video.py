import os
import cv2

class IOVideo:
    def __init__(self, path):
        if not path:
            raise ValueError('Path is empty')

        if not os.path.exists(path):
            raise FileNotFoundError('File not found')

        self.path = path
        self.video = self.read()

    def read(self):
        return cv2.VideoCapture(self.path)

    def write(self, video, path=None):
        if not path:
            path = self.path
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
            cv2.imshow("Video", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        video.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    io = IOVideo('../../data/videos/video.mp4')
    input_video = io.read()
    # io.write(input_video, '../../videos/video_new.mp4')
    io.show(input_video)