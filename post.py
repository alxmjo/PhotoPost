import os
import shutil
import time
import datetime

# Get images from directory
images = dict((i, '') for i in os.listdir()
              if os.path.splitext(i)[1] == '.jpg'
              or os.path.splitext(i)[1] == '.JPG'
              or os.path.splitext(i)[1] == '.png'
              or os.path.splitext(i)[1] == '.PNG')

# Get title
print('Permalink: ', end='')
permalink = input()

# Create filename and file
now = datetime.datetime.now()
file_name = str(now.year) + '-' + str('%02d' % now.month) + '-' \
            + str('%02d' % now.day) + '-' + permalink \
            + '.markdown'
post = open(file_name, "w+")

# Write header to post
utc_offset = int(time.localtime().tm_gmtoff / 3600)
date = now.strftime("%Y-%m-%dT%H:%M:%S") + '+0' + str(utc_offset) + ':00'
post.write('---\n'
           + 'layout: post' + '\n'
           + 'date: ' + date + '\n'
           + 'permalink: ' + permalink + '\n'
           + '\n'
           + 'title: ""               # Empty quotes if this is a short.' + '\n'
           + 'image:                  # /images/filename.jpg' + '\n'
           + 'summary:                # A sentence or two about the post.' + '\n'
           + 'category:               # "Category Name" (only one)' + '\n'
           + 'tags:                   # newsletter' + '\n'
           + 'sharing:                # Text to be shared on each network.' + '\n'
           + '  twitter:' + '\n'
           + '---' + '\n'
           + '\n')

# Populate dictionary with captions
for key in images.keys():
    print('Image caption for ' + key + ': ', end='')
    images[key] = input()

# Write image links and captions to post in sorted order
for key, value in sorted(images.items()):
    post.write('![' + value + '](/images/' + key + ')\n*' + value + '*')
    post.write('\n\n\n\n')

# Close file
post.close()

# Get post destination
print('Post location (i.e. /Users/Alex/Blog/_posts): ', end='')
post_loc = input()

# Move post to _posts
shutil.move(file_name, post_loc)
print('Post ' + file_name + ' moved to ' + post_loc)

# Get images destination
print('Post location (i.e. /Users/Alex/Blog/images): ', end='')
image_loc = input()

# Move images to images
for image in images:
    shutil.move(image, image_loc)
print('Images moved to ' + image_loc)
