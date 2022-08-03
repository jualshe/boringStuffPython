import os, shutil
import send2trash

# delete a file -> move to trash
# send2trash.send2trash('/Users/julia/Desktop/sofa1.png')

os.getcwd()
# delete a file
# os.unlink('')

# delete empty folder
# os.rmdir('')

# delete folder and content
# shutil.rmtree('')

# to prevent deleting try to run print first and then unlink
os.chdir('/Users/julia/Desktop')
for filename in os.listdir():
    if filename.endswith('.txt'):
        print(filename)
        send2trash.send2trash(filename)
