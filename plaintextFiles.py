helloFile = open('/Users/julia/hello.txt')
content = helloFile.read()
helloFile.close()

print(content)
