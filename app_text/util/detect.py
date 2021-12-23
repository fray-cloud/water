import logging
import cv2

from paddleocr import PaddleOCR


class Text:
    # paddleocr
    ocr = PaddleOCR(use_gpu=False, lang='en')
    # paddleocr
    def text(self, image, roi):
        x, y, w, h = roi
        roi_image = image[y:h + y, x:w + x]
        roi_image = cv2.resize(roi_image, (0,0), fx=1.6, fy=1.6)
        cv2.imwrite(f'text{roi[3]}.jpg', roi_image)
        result = self.ocr.ocr(roi_image, cls=True)
        
        text_list = list()
        for text in result:
            print(text)
            text_list.append(text[1][0])
        
        JSON = {
            'text_rec': text_list,
        }

        return JSON

        
