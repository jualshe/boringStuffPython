import os
import shutil

for folderName, subfolders, filenames in os.walk('/Users/julia/Desktop/delicious'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + 'are: ' + str(subfolders))
    print('The filenames in ' + folderName + 'are: ' + str(filenames))
    print()

for subfolder in subfolders:
    print(subfolder)
    # if 'fish' in subfolder:
    #     os.rmdir(subfolder)
    #     os.unlink(subfolder)

for file in filenames:
    if file.endswith('.py'):
        shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))
