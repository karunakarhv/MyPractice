import frontmatter
import os
directory = 'Backup'
for filename in os.listdir(directory):
    data = frontmatter.load(os.path.abspath(directory + '/' + filename))
    print(data['title'])
    os.rename(os.path.abspath(directory + '/' + filename), os.path.abspath(directory + '/' + data['title'] + '.md'))
