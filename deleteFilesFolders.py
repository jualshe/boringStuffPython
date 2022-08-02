import os

os.getcwd()
# os.unlink('')

# delete empty folder
# os.rmdir('')

# delete folder and content
import shutil

# shutil.rmtree('')

os.chdir('/Users/julia/Desktop')
for filename in os.listdir():
    if filename.endswith('.txt'):
        print(filename)
        os.unlink(filename)
