import numpy as np
import cv2
import math
import logging
import numpy as np

class Line:
    CANNY_THRESHOLD_1 = 130
    CANNY_THRESHOLD_2 = 150
    IMAGE_SIZE = (600, 600)

    #connection
    NOT_CONNECTION = -1
    NAME = '__main__'
    logger = logging.getLogger(__name__)
    logger_file = logging.getLogger('detect_file')
    logger.debug('...starting line recognition')

    def get_line(self, image):
        gray = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, self.CANNY_THRESHOLD_1, self.CANNY_THRESHOLD_2)
        if __name__ == self.NAME:
            cv2.imshow("edges", edges)
        try:
            lines = cv2.HoughLinesP(edges, 1, math.pi/1, 70, None, 2, 1000)
        except:
            return []

        return lines

    def get_length(self, lines, image):
        if lines is None:
            return 0
        temp = 0
        for i in range(len(lines)):

            x1 = lines[i][0][0]
            y1 = lines[i][0][1]
            x2 = lines[i][0][2]
            y2 = lines[i][0][3]

            dot1 = (x1,y1)
            dot2 = (x2,y2)
            length: np.intc = y1 - y2
            if (i != 0) and  lines[i - 1][0][1] - lines[i - 1][0][3] < length:
                if __name__ == self.NAME:
                    cv2.line(image, dot1, dot2, (255,0,0), 2)
                temp = lines[i - 1][0][1] - lines[i - 1][0][3]
            else:
                if __name__ == self.NAME:
                    cv2.line(image, dot1, dot2, (0,225,0), 2)
        if temp != 0:
            length = temp

        return length

    def line(self, image,  roi):
        x, y, w, h = roi

        roi_image = image[y:h + y, x:w + x]
        
        copyed_image = image.copy()
        print(f"shape ** {roi_image.shape}")
        lines = self.get_line(roi_image)
        length = self.get_length(lines, roi_image)
        if __name__ == self.NAME:
            cv2.rectangle(image, (x,y), (w,h), (255,0,0), thickness=2)
            cv2.imshow("image_result", image)

        JSON = {
            "HEIGHT" : int(h),
            "LENGTH": int(length),
            # "AVG": int(mean)
        }
        cv2.imwrite(f'line{roi[3]}.jpg', roi_image)
        self.logger_file.info(f'success line : {length}')

        # line_log.create(
        #     camera_line_log_id = id,
        #     line_length = length,
        #     log_date=datetime.now()
        # )
        return JSON
