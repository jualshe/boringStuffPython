# spam = 'Hello world!'
# print(spam.upper())
# print(spam)
# #
# spam = spam.upper()
# print(spam)
# print('\n\n' + spam.lower())

# print('Enter your answer - yes?')
# answer = input()
# # print(answer)
# # answer.lower() == 'yes'
# if answer.lower() == 'yes':
#     print('Playing again')
#
# spam = 'hello world!'
# print(spam.isupper())
# # print(spam.islower())
#
# print('This Is Title Case'.istitle())
#
# print('Hi!'.startswith('H'))
#
# print(','.join(['cats', 'llamas','copybaras']))
# ko='JULI'
# print(' kaka\n'.join(ko))
#
# print('My name is Juju'.split())

name='Hello'
name1 = name.rjust(10)
name2= name1.ljust(20, '*')
print(name2)

print(len(name2))

nameJ='Julia'
nameJ= nameJ.center(20,'=')
print(nameJ)

print('    x    '.split())

print('SpamSpamEggSpamBaconSpam'.strip('ampS'))

spam = 'Hello there!'
spam = spam.replace('e', 'Z')
print(spam)

# import pyperclip
# pyperclip.copy('Hello!!!!!!')
# pyperclip.paste()