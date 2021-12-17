import cv2
import numpy as np

class Args:
    def __init__(self, src):
        self.src = src

        # init frame
        self.cap = cv2.VideoCapture(src)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        _, frame = self.cap.read()
        self.frame = frame

        # init blur
        self.ksize = (5, 5)
        self.sigmaX = 0

        # init canny
        self.threshold1 = 50
        self.threshold2 = 100

    @property
    def ksize(self):
        return self._ksize

    @ksize.setter
    def ksize(self, ksize):
        self._ksize = ksize

    @property
    def sigmaX(self):
        return self._sigmaX

    @sigmaX.setter
    def sigmaX(self, sigmaX):
        self._sigmaX = sigmaX

    @property
    def frame(self):
        return self._frame

    @frame.setter
    def frame(self, frame):
        if frame is None:
            self._frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        else:
            self._frame = frame

    @property
    def threshold1(self):
        return self._threshold1

    @threshold1.setter
    def threshold1(self, threshold1):
        self._threshold1 = threshold1

    @property
    def threshold2(self):
        return self._threshold2

    @threshold2.setter
    def threshold2(self, threshold2):
        self._threshold2 = threshold2

class Line:
    def getLine(self, image, theta, threshold, min_theta, max_theta):
        pass



class Preprocessing(Args):
    
    def get_ROI(self, frame):
        rects = cv2.selectROI('src', frame, False, False)
        return rects

    def gaussianBlur(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray, self.ksize, self.sigmaX)
        return blur
    
    def getLine(self, canny, theta, threshold, min_theta, max_theta):
        if theta != 0:
            theta = np.pi / theta
        else:
            theta = 1e-6
        if min_theta == 0:
            min_theta = 0.0
        else:
            min_theta = np.pi/min_theta
        max_theta = np.pi/max_theta

        if min_theta > max_theta:
            temp = min_theta
            min_theta = max_theta
            max_theta = temp
        lines = cv2.HoughLines(canny, 1, theta, threshold, min_theta=min_theta, max_theta=max_theta)
        return lines

    def getLineP(self, canny, theta, threshold, minLineLength=10):
        if theta != 0:
            theta = np.pi / theta
        else:
            theta = 0.01
        lines = cv2.HoughLinesP(canny, 1, theta, threshold, minLineLength=minLineLength)
        return lines

    @classmethod
    def showLine(cls, frame, lines:list):
        if lines is None:
            return
        
        for l in lines:
            print('detected')
            rho, theta = l[0][0], l[0][1]
            a, b = np.cos(theta), np.sin(theta)
            x0, y0 = a*rho, b*rho

            scale = frame.shape[0] + frame.shape[1]

            x1 = int(x0 + scale * -b)
            x2 = int(x0 - scale * -b)
            y1 = int(y0 + scale * a)
            y2 = int(y0 - scale * a)

            cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.circle(frame, (x0, y0), 3, (255, 0, 0), 5, cv2.FILLED)

    @classmethod
    def showLineP(cls, frame, lines: np.array, want_length=True):
        if lines is None:
            return 0

        def value(want_length):
            y0 = list()
            y1 = list()
            
            for i in lines:
                i = i[0]
                y0.append(i[1])
                y1.append(i[3])

            y0.sort()
            y1.sort()

            y0 = y0[0]
            y1 = y1[len(lines) - 1]
            length = y1 - y0
            length = round(length/frame.shape[0] * 100, 2)
            if want_length:
                return length
            else:
                return y0, y1

        _, y1 = value(False)
        width_half = int(frame.shape[1] / 2)
        # print(f'length : {length} // rate : {round(length/frame.shape[0] * 100, 2)} %')
        cv2.line(frame, (width_half - 10 , y1), (width_half + 10, y1), (0, 0, 255), 2)
        
        return value(want_length)


    def canny(self, gaussian_blur):
        canny = cv2.Canny(gaussian_blur, self.threshold1, self.threshold2)
        return canny
    
    @classmethod
    def show(cls, window_name, frame):
        cv2.imshow(window_name, frame)
    
    def stop(self):
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    pp = Preprocessing('rtsp://admin:qwer1234@10.0.0.226:554/Streaming/Channels/101')
    pp.ksize = (3,3)
    frame = None
    per = 0
    cnt = 1
    for i in range(50):
        ret, frame = pp.cap.read()
    rect = pp.get_ROI(frame)
    while True:

        ret, frame = pp.cap.read()
        x, y, w, h = rect
        if not ret:
            pp = Preprocessing('rtsp://admin:qwer1234@10.0.0.226:554/Streaming/Channels/101')
            continue
        frame = frame[y:y+h, x:x+w]
        # frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
        blur = pp.gaussianBlur(frame)
        
        canny = pp.canny(blur)
        
        # lines = pp.getLine(canny, 90, 70, 80, 95)
        # pp.showLine(blur, lines)
        lines = pp.getLineP(canny, 0, 50, minLineLength=2)
        per += pp.showLineP(frame, lines)
        r_per = round(per / cnt, 2)
        cnt += 1
        cv2.putText(frame, f'{r_per} % ' , (10, 60), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 1)
        pp.show('blur', blur)
        pp.show('canny', canny)
        pp.show('src', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    pp.stop()
