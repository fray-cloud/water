from .color_histogram_feature_extraction import get_training_value, color_histogram_of_test_image
from .knn_classifier import main

import os

class Color:
    testing_data = 'testing.data'
    PATH = os.path.join(os.path.dirname(__file__), 'source')
    TESTING_PATH = os.path.join(PATH, testing_data)

    def testing(self, image):
        color_histogram_of_test_image(image, self.TESTING_PATH)

    def color(self, image, rois:list):
        roi_images = list()
        for roi in rois:
            x, y, w, h = roi
            roi_image = image[y:h + y, x:w + x]
            roi_images.append(roi_image)

        for img in roi_images:
            self.testing(img)
            prediction = main(get_training_value, self.TESTING_PATH)
            if prediction == 'red':
                red = red + 1
            elif prediction == 'blue':
                blue = blue + 1
            elif prediction == 'green':
                green = green + 1

        JSON = {
            'color': {
                'red': red,
                'blue': blue,
                'green': green
            }
        }

        return JSON


