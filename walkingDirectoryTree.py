import os

for folderName, subfolder, filenames in os.walk('/Users/julia/Desktop/delicious'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + 'are: ' + str(subfolder))
    print('The filenames in ' + folderName + 'are: ' + str(filenames))
    print()
