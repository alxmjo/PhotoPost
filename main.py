import os
import datetime

# Get images from directory
images = dict((i, '') for i in os.listdir())

# Get title
print('Title: ', end='')
title = input()

# Create filename and file
now = datetime.datetime.now()
print('Offset: ' + str(now.gmtime() - now.localtime()))
file_name = str(now.year) + '-' + title.lower().replace(" ", "-") + '.markdown'
file = open(file_name, "w+")

for key in images.keys():
    print('Image caption for ' + key + ': ', end='')
    images[key] = input()

# for key, value in images.items():



print(images)