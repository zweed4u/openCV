#!/bin/bash
# arg passed should be filename WITHOUT extension

if [ "$*" == "" ]; then
    echo 'Please specify filename WITHOUT extension'
    exit 1
fi

mkdir $1_data
mkdir $1_info
opencv_createsamples -img $1.jpg -bg bg.txt -info $1_info/info.lst -pngoutput $1_info -maxxangle 0.5 -maxyangle -0.5 -maxzangle 0.5 -num 1850
opencv_createsamples -info $1_info/info.lst -num 1850 -w 20 -h 20 -vec $1_positives.vec
opencv_traincascade -data $1_data -vec $1_positives.vec -bg bg.txt -numPos 1700 -numNeg 850 -numStages 10 -w 20 -h 20
