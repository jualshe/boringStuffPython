spam = ['hello', 'hi', 'howgy', 'heyas', 'hi']

print(spam[1])
print(spam.index('hi'))

spam.append('kaka')
spam.append('kaka')
spam.append('kaka')

spam.remove('kaka')
spam.insert(0, 'good afternoon')

del spam[5]

spam.sort()
spam.sort(reverse=True)
print(spam)

l = ['a', 'z', 'A', 'Z']
l.sort(key=str.lower)

print(l)
