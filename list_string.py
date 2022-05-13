import copy

a = ['a',
     'b',
     'c',
     'd']
b = copy.deepcopy(a)
b[1] = 'kaka'

print('soso ' + \
      'ololo')
print(a)
print(b)

# def eggs(someParameter):
#     someParameter.append('Hello')
#
#
# spam = [1, 2, 3]
# eggs(spam)
# print(spam)

# name = 'Sophie'
# print(name[3])
#
# print('So' in name)
# print('XXX' in name)
# for letters in name:
#     print(letters)
