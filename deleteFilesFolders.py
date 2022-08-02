import os, shutil
import send2trash

send2trash.send2trash('/Users/julia/Desktop/sofa1.png')

os.getcwd()
# os.unlink('')

# delete empty folder
# os.rmdir('')  

# delete folder and content


# shutil.rmtree('')

os.chdir('/Users/julia/Desktop')
for filename in os.listdir():
    if filename.endswith('.txt'):
        print(filename)
        os.unlink(filename)
