import os
import cv2
import numpy as np
from tqdm import tqdm

if __name__ != '__main__':
    from django.conf import settings

import time

def color_histogram_of_test_image(test_src_image, path):

    # load the image
    image = test_src_image

    chans = cv2.split(image)
    colors = ('b', 'g', 'r')
    features = []
    feature_data = ''
    counter = 0
    for (chan, color) in zip(chans, colors):
        counter = counter + 1

        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        features.extend(hist)

        # find the peak pixel values for R, G, and B
        elem = np.argmax(hist)

        if counter == 1:
            blue = str(elem)
        elif counter == 2:
            green = str(elem)
        elif counter == 3:
            red = str(elem)
            feature_data = red + ',' + green + ',' + blue
            # print(feature_data)

    with open(path, 'w') as myfile:
        myfile.write(feature_data)


def color_histogram_of_training_image(img_name):

    # detect image color by using image file name to label training data
    if 'red' in img_name:
        data_source = 'red'
    elif 'green' in img_name:
        data_source = 'green'
    elif 'blue' in img_name:
        data_source = 'blue'
    elif 'black' in img_name:
        data_source = 'black'

    # load the image
    image = cv2.imread(img_name)

    chans = cv2.split(image)
    colors = ('b', 'g', 'r')
    features = []
    feature_data = dict()
    counter = 0
    for (chan, color) in zip(chans, colors):
        counter = counter + 1

        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        features.extend(hist)

        # find the peak pixel values for R, G, and B
        elem = np.argmax(hist)

        if counter == 1:
            blue = str(elem)
        elif counter == 2:
            green = str(elem)
        elif counter == 3:
            red = str(elem)
            
            feature_data['red'] = red
            feature_data['green'] = green
            feature_data['blue'] = blue

        
    return feature_data
            # train_color = TrainColor(color=data_source, color_image=model, color_r=red, color_g=green, color_b=blue)
            # train_color.save()
            
    #         feature_data = red + ',' + green + ',' + blue

    # with open(path, 'a') as myfile:
    #     myfile.write(feature_data + ',' + data_source + '\n')


def image_save_path():
    
    if __name__ == '__main__':
        path = os.path.join('media', 'dataset', 'color')
    else:
        path = os.path.join(settings.MEDIA_ROOT, 'dataset', 'color')
    color_list = ['red', 'green', 'blue', 'black']

    
    path_dict = dict()

    for clr in color_list:
        path_list = list()
        for f in os.listdir(os.path.join(path, clr)):
            color_path = os.path.join(path, clr, f)
            path_list.append(color_path)
            #print(f'path[{clr}] : {color_path} \n')
        #print(clr, path_list)
        path_dict[clr] = path_list
    return path_dict

def get_training_value():
    train_dict = dict()
    path_dict = image_save_path()
    for key, values in path_dict.items():
        train_list = list()
        for path in values:
            train_data = color_histogram_of_training_image(path)
            train_list.append(train_data)
        train_dict[key] = train_list
    return train_dict


# def training():
#     # clear model
#     try:
#         ColorDataSet.objects.all().delete()
#         TrainColor.objects.all().delete()

#         path = os.path.join(settings.MEDIA_ROOT, 'dataset', 'color')

#         color_list = ['red', 'green', 'blue', 'black']
#         index = 0
        
#         for clr in color_list:
#             #test
#             pb = tqdm(total=len(os.listdir(os.path.join(path, clr))), ncols=100, ascii=True)
#             for f in os.listdir(os.path.join(path, clr)):
#                 color_path = os.path.join(path, clr, f)
#                 color_dateset = ColorDataSet(id=index, color=clr, color_image=color_path)
#                 color_dateset.save()
#                 color_histogram_of_training_image(color_path, color_dateset)
#                 #test
#                 if clr == 'red':
#                     pb.set_description(f'{CMD_Colors.printing(clr, CMD_Colors.RED)}')
#                 if clr == 'green':
#                     pb.set_description(f'{CMD_Colors.printing(clr, CMD_Colors.GREEN)}')
#                 if clr == 'blue':
#                     pb.set_description(f'{CMD_Colors.printing(clr, CMD_Colors.BLUE)}')
#                 if clr == 'black':
#                     pb.set_description(f'{CMD_Colors.printing(clr, CMD_Colors.WHITE)}')
#                 pb.update()
#                 index = index + 1
#             pb.close()
#     except:
#         pass


if __name__ == '__main__':
    dic = get_training_value()
    print(dic)
    
