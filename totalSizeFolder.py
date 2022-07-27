# finding total size of all the files in a folder
import os

totalSize = 0

for filename in os.listdir('/Users/julia/Downloads'):
    if not os.path.isfile(os.path.join('/Users/julia/Downloads', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('/Users/julia/Downloads', filename))

print(totalSize)
