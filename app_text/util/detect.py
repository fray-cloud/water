import logging
import cv2

from paddleocr import PaddleOCR


class Text:
    logger = logging.getLogger(__name__)
    logger_file = logging.getLogger('detect_file')
    logger.debug('...starting text recognition')
    NOT_CONNECTION = -1

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
        cv2.imwrite(f'text{roi[3]}.jpg', roi_image)
        result = self.ocr.ocr(roi_image, cls=True)
        
        text_list = list()
        for line in result:
            print(line)
            text_list.append(line[1][0])
        
        JSON = {
            'text_rec': text_list,
        }
        self.logger_file.info(f'success text : {text_list}')

        return JSON

        
