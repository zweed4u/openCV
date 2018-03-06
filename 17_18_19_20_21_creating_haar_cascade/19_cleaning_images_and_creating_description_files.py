#!/usr/bin/python3
# https://www.youtube.com/watch?v=t0HOVLK30xQ&index=19&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq

# Create a directory for all downloaded images that are outliers and copy broken images to this dir

import os
import cv2
import numpy as np


def find_uglies():
    for file_type in ['neg']:
        for image in os.listdir(file_type):
            for ugly in os.listdir('ugly_broken_imgs'):
                try:
                    current_image_path = '{}/{}'.format(file_type, image)
                    ugly = cv2.imread('ugly_broken_imgs/{}'.format(ugly))
                    question = cv2.imread(current_image_path)

                    # Are these images the same size and are the same bitwise
                    if ugly.shape == question.shape and not (
                            np.bitwise_xor(ugly, question).any()):
                        print('This image is ugly')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))


def create_pos_and_neg():
    for file_type in ['neg']:
        print('Creating {} description file'.format(file_type))
        for image in os.listdir(file_type):
            if file_type == 'neg':
                line = '{}/{}\n'.format(file_type, image)
                with open('bg.txt', 'a') as f:
                    f.write(line)
            # Use if not creating samples - line format: image path, # of objects, beginning coordinates, ending coordinates
            elif file_type == 'pos':
                line = '{}/{} 1 0 0 50 50\n'.format(file_type, image)
                with open('info.dat', 'a') as f:
                    f.write(line)


print('Deleting "ugly" images')
find_uglies()

print('Creating description files for negative images')
create_pos_and_neg()

# Move neg folder and description files to workspace
