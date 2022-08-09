"""
*****************
*               *
*               *
*               *
*               *
*****************
"""


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to a string of lenght 1')
    print(symbol * width)
    if (width < 2) or (height < 2):
        raise Exception('width and height must be greater or equal than 2')

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


import traceback

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('Traceback info was written error_log.txt')

boxPrint('*', 15, 5)
boxPrint('~', 25, 5)
boxPrint('~', 25, 1)
boxPrint('**', 15, 5)

import os

print(os.getcwd())
