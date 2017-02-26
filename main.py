import os
# import datetime

# Get images from directory
images = dict((i, '') for i in os.listdir())

# # Get title
# print('Title: ', end='')
# title = input()
#
# # Create filename and file
# now = datetime.datetime.now()
# file_name = str(now.year) + '-' + str('%02d' % now.month) + '-' + str('%02d' % now.day) + '-' + \
#             title.lower().replace(" ", "-") + '.markdown'
# file = open(file_name, "w+")

file_name = 'temp.markdown'
file = open(file_name, "w+")

for key in images.keys():
    print('Image caption for ' + key + ': ', end='')
    images[key] = input()

for key, value in images.items():
    file.write('![' + value + '](/images/' + key + ')\n*' + value + '*')
    file.write('\n\n\n\n')
