print('how many cats do you have?')
numCats = input()
# because input returns a string value - convert to int
try:
    if int(numCats) >= 4:
        print('that is a lot of cats!')
    elif int(numCats) < 0:
        print('you entered negative number')
    else:
        print('That is not that many cats')
except ValueError:
    print('you did not enter a number')

# # handle errors with try and except Statement
# def div42by(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print('Error: you tried to divide yb zero')
#
#
# print(div42by(12))
# print(div42by(2))
# print(div42by(0))
# print(div42by(1))
