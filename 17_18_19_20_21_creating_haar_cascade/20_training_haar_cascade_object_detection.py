# https://www.youtube.com/watch?v=eay7CgPlCyo&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=20

# After neg dir/images and description files are in workspace dir
# Also need to bring positive (50x50) image in workspace dir
# mkdir data - cascade info goes here
# mkdir info - positive images ho here

# Distorts negative images to contain matching object from postive (Adds your pos image to negative images)
# opencv_createsamples -img (pos_filename) -bg (negative desciption file) -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num (slightly less than # of neg images)
# command run: opencv_createsamples -img xbox5050.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle -0.5 -maxzangle 0.5 -num 1850

# Create vector file (always needed)
# opencv_createsamples -info info/info.lst -num 1850 -w 20 -h 20 -vec positives.vec

# Train cascade - takes some time
# opencv_traincascade -data (output_dir) -vec positives.vec -bg bg.txt -numPos (smaller than num used before) -numNeg (half of the numPos) -numStages 10 -w 20 -h 20
# opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1700 -numNeg 850 -numStages 10 -w 20 -h 20

# To run even when exit ssh session:
# nohup <command_above> &

# Can create cron job to write 1 to drop_cache

# Run create shell script in workspace folder with pos image filename as arg to create samples, vector file and train
