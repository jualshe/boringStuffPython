helloFile = open('/Users/julia/hello.txt')
content = helloFile.read()
print(content)

helloFile = open('/Users/julia/hello.txt')
content2 = helloFile.readlines()
print(content2)
helloFile.close()
