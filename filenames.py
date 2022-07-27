# using strings to represent a filepath
import os

a = '/Users/julia/dev/images/beach.jpg'

print(a)

print(os.path.join('folder1', 'folder2', 'file.png'))
print(os.getcwd())
print(os.path.abspath('beach.jpg'))
print(os.path.abspath('../../beach.jpg'))

print(os.path.isabs('/Users/julia/dev/beach.jpg'))
print(os.path.isabs('../../beach.jpg'))

print(os.path.relpath('/Users/julia/dev/images/beach.jpg', '/Users/julia'))

print(os.path.dirname('/Users/julia/dev/images/beach.jpg'))
print(os.path.basename('/Users/julia/dev/images/beach.jpg'))
print(os.path.basename('/Users/julia/dev/images'))

print(os.path.exists('/Users/julia/dev/images/folderN/beach.jpg'))

print(os.path.isfile('/Users/julia/dev/images/beach.jpg'))
print(os.path.isdir('/Users/julia/dev/images/beach.jpg'))

print(os.path.getsize('/Users/julia/dev/images/beach.jpg'))
print(os.listdir('/Users/julia/dev/GitHub'))

os.makedirs('/Users/julia/fun/test/python/newfolderfromPycharm')
