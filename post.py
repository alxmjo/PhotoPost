import os
import shutil
import time
import datetime

# Get images from directory
images = dict((i, '') for i in os.listdir())

# Get title
print('Title: ', end='')
title = input()

# Create filename and file
now = datetime.datetime.now()
file_name = str(now.year) + '-' + str('%02d' % now.month) + '-' \
            + str('%02d' % now.day) + '-' + title.lower().replace(" ", "-") \
            + '.markdown'
post = open(file_name, "w+")

# Write header to post
utc_offset = int(time.localtime().tm_gmtoff / 3600)
date = now.strftime("%Y-%m-%dT%H:%M:%S") + '+0' + str(utc_offset) + ':00'
post.write('---\n'
           + 'layout: post' + '\n'
           + 'title: ' + title + '\n'
           + 'date: ' + date + '\n'
           + 'image: ' + '\n'
           + 'summary: ' + '\n'
           + '---' + '\n'
           + '\n')

# Populate dictionary with captions
for key in images.keys():
    if images[key].endswith('.jpg') \
            or images[key].endswith('.JPG') \
            or images[key].endswith('.png') \
            or images[key].endswith('.PNG'):
        print('Image caption for ' + key + ': ', end='')
        images[key] = input()

# Write image links and captions to post
for key, value in images.items():
    post.write('![' + value + '](/images/' + key + ')\n*' + value + '*')
    post.write('\n\n\n\n')

# Close file
post.close()

# Move post to _posts
shutil.move(file_name, '/Users/Alex/Blog/_posts')

# Move images to images
for image in images:
    shutil.move(image, '/Users/Alex/Blog/images')
