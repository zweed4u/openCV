#!/usr/bin/python3
# https://www.youtube.com/watch?v=jG3bu0tjFbk&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=17

# Creating haar cascade on linux machine
# Steps in Creation:
# 1. Collect "negative"/"background" images - ensure the desired object is not in them and that you get MANY backgrounds
# 2. Collect/create "positive" images - MANY images with the desired object - can be made based on one image - should have twice as many of these as the negative/background images
# 3. Create a positive vector file by stitching together all positives - done via OpenCV command
# 4. Train cascade - done via openCV command

# ** Negative and positive images need description files
# Negative images (bg.txt - path to each image line by line)
# Positive images (info.txt or pos.txt - path to each image line by line and how many objects and where they are located (file_path.jpg 1 0 0 50 50) - image, num of objects, start coordinates, rectangle coordinates)

# Negative images should be larger than positive images - both types of images should be small! ~100x100 for negatives, ~50x50 for positives

# image-net.org for images

# Environment setup
# make and change dir into workspace dir
# git clone https://github.com/Itseez/opencv.git
# sudo apt-get install build-essential
# sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
# sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
# sudo apt-get install libopencv-dev

# If fetching external positive images:
# Go to image-net and search for object and select a synset that matches desired object for positive images
# Select download tab on synset to view all urls

# But we're going to create samples of our image

# For negatives - search for something without object on image-net ie. "people"