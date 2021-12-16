import multiprocessing as mp
import cv2
import numpy as np

class Streaming:
    def __init__(self):
        self.q : mp.Queue
        self.p : mp.Process
        self.break_point = True
        self.is_start = False


    def start(self, rtsp, camera_name):
        self.q = mp.Queue(1)
        self.p = mp.Process(target=self.stream, args=(self.q, self.break_point, rtsp, camera_name))
        self.p.daemon = True
        
        # start point 
        self.p.start()
        self.is_start = True

    def end(self):
        self.break_point = False
        self.p.join()
        print('stop processing')

    def restart(self, rtsp, camera_name):
        if self.p.is_alive():
            self.end()
        self.start(rtsp, camera_name)

    def stream(self, q:mp.Queue, break_point, rtsp, camera_name):
        cap = cv2.VideoCapture(rtsp)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        data = dict()

        data['image'] = None
        data['is_alive'] = False
        data['name'] = camera_name

        while break_point:
            ret = cap.grab()
            data['is_alive'] = ret

            if not ret:
                print(f'rtsp server is broken >> rtsp:{ret}')
                random_image = np.random.randint(255, size=(height, width), dtype=np.uint8)
                data['image'] = random_image
                q.put(data)
                cap = cv2.VideoCapture(rtsp)
                print(f'is refresh >> rtsp:{cap.grab()}')

            elif q.full():
                continue

            else:
                print('confirm process')
                _, frame = cap.retrieve()
                data['image'] = frame
                q.put(data)