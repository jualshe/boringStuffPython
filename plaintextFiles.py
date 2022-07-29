helloFile = open('/Users/julia/hello.txt')
content = helloFile.read()
print(content)

helloFile = open('/Users/julia/hello.txt')

content2 = helloFile.readlines()
print(content2)
helloFile.close()

# write to a file replacing the content
helloFile = open('/Users/julia/hello2.txt', 'w')
helloFile.write('Hello!!!!!!')
helloFile.write('\nHello!!!!!!')
helloFile.close()

baconFile = open('bacon.txt', 'w')
baconFile.write('Bacon is not a vegetable!')
baconFile.close()

import os

print(os.getcwd())

# write to a file adding the content
baconFile = open('bacon.txt', 'a')
baconFile.write('\n\n\nA lot of people find bacon delicious.')
baconFile.close()

import shelve

shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Chipa', 'Zipka', 'Fat-tail']
shelfFile.close()

print(shelfFile)
