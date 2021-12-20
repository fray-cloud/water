import numpy as np
import cv2

class Line:

    @staticmethod
    def gaussianBlur(image, gaussian_ksize, gaussian_sigmaX):
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray, gaussian_ksize, gaussian_sigmaX)
        return blur

    @staticmethod
    def canny(gaussian_blur, canny_threashold1, canny_threashold2):
        canny = cv2.Canny(gaussian_blur, canny_threashold1, canny_threashold2)
        return canny

    @staticmethod
    def getLine(canny, theta, hough_threshold, hough_minLineLength):
        if theta != 0:
            theta = np.pi / theta
        else:
            theta = 0.01
        lines = cv2.HoughLinesP(canny, 1, theta, hough_threshold, minLineLength=hough_minLineLength)
        if lines is None:
            return 0

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
        length = round(length/canny.shape[0] * 100, 2)
        return length

    @staticmethod
    def main(image, roi, gaussian_ksize, gaussian_sigmaX, canny_threashold1, canny_threashold2, theta, hough_threshold, hough_minLineLength=10):
        x, y, w, h = roi
        image = image[y:y+h, x:x+w]
        blur = Line.gaussianBlur(image, gaussian_ksize, gaussian_sigmaX)
        canny = Line.canny(blur, canny_threashold1, canny_threashold2)
        length = Line.getLine(canny, theta, hough_threshold, hough_minLineLength)

        JSON = {
            'LENGTH' : length
        }

        return JSON



if __name__ == '__main__':
    import time
    ksize = (5,5)
    sigmaX = 0

    c_th1 = 50
    c_th2 = 100

    theta = 0
    h_th = 50
    min_line_lenght = 2
    
    
    cap = cv2.VideoCapture('rtsp://admin:qwer1234@10.0.0.226:554/Streaming/Channels/101')
    time.sleep(2)
    ret, image = cap.read()
    roi = cv2.selectROI('roi', image, False, False)
    # cv2.destroyWindow('roi')

    while True:

        ret, image = cap.read()
        if not ret:
            cap = cv2.VideoCapture('rtsp://admin:qwer1234@10.0.0.226:554/Streaming/Channels/101')
            continue
        
        value = Line.main(image, roi, ksize, sigmaX, c_th1, c_th2, theta, h_th, min_line_lenght)
        cv2.putText(image, str(value['LENGTH']), (10, 60), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 1)
        
        cv2.imshow('result', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    
    cv2.destroyAllWindows()

    
