import subprocess
import os

new_width = '200'
directory_out = 'Result'
os.makedirs(directory_out)
directory_source = 'Source'
files = os.listdir(directory_source)
images = filter(lambda x: x.endswith('.jpg'), files)

img_list = list(images)


for file_name in img_list:
    print(file_name)
    subprocess.run(['sips', '--resampleWidth', new_width, '--out', os.path.join(directory_out, file_name), os.path.join(directory_source, file_name)])

