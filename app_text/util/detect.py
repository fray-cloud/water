import logging
import cv2

from paddleocr import PaddleOCR


class Text:
    # paddleocr
    ocr = PaddleOCR(use_gpu=False, lang='en')
    
    # def text(self, image, roi, id):
    #     x, y, w, h = roi
    #     roi_image = image[y:h, x:w]
    #     cv2.imwrite('text.jpg', roi_image)
    #     # cv2.imwrite('text.jpg', roi_image)
    #     plate_list = find_text(roi_image)
    #     all_list = []
        
    #     for er_plate in plate_list:
            
    #         text_list = main(er_plate)
            
    #         for digit in text_list:
    #             all_list.append(str(digit))
        
    #     JSON = {
    #         'text_rec': all_list,
    #     }
    #     self.logger_file.info(f'success text : {all_list}')
    #     text_log = TextLog.objects
    #     text_log.create(
    #         camera_text_log_id = id,
    #         text = ",".join(all_list)
    #     )
    #     return JSON

    # paddleocr
    def text(self, image, roi):
        x, y, w, h = roi
        roi_image = image[y:h + y, x:w + x]
        roi_image = cv2.resize(roi_image, (0,0), fx=1.3, fy=1.3)
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

        
