import cv2
import numpy as np

class Camera:
    def __init__(self, rtsp, camera_name):
        self.rtsp = rtsp
        self.camera_name = camera_name
        # default image
        print(f'starting cam ..[{self.camera_name}] : {self.rtsp}')

        self.start()
        self.get_frame()

    
    def start(self):
        self.cap = cv2.VideoCapture(self.rtsp)
        self.is_alive, self.default_image = self.cap.read()

    def end(self):
        self.cap.release()

    def save(self, path, image):
        cv2.imwrite(path, image)
        return path

    def get_frame(self):
        if not self.is_alive or self.default_image is None:
            # TODO default size setting // 1920, 1080 change
            print(f'rtsp server is wrong someting.. [{self.camera_name}] : {self.rtsp}')
            self.image = np.random.randint(255, size=(1920, 1080), dtype=np.uint8)

            # restart service
            self.end()
            self.start()

        else:
            self.is_alive, self.default_image = self.cap.read()
            self.image = self.default_image

        return self.image



if __name__ == '__main__':
    rtsp = 'rtsp://admin:qwer1234@10.0.0.226:554/Streaming/Channels/101'
    cam = Camera(rtsp, 'cam')

    # 1. default
    # image = cam.get_frame()
    # cv2.imshow('result', image)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    # 2. loop
    while True:
        image = cam.get_frame()
        cv2.imshow('loop', image)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
