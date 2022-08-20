import logging

logging.basicConfig(level=logging.DEBUG)
# , format='%(asctime)s - %(levelname)s - %(messages)s')
# write log to a file
# logging.basicConfig(filename='testLogDebug.txt', format='%(asctime)s - %(levelname)s - %(messages)s')
# logging.disable(logging.CRITICAL)

logging.debug('Start of the program')


def factorial(n):
    logging.debug('start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('return value is %s' % (total))
    return total


print(factorial(7))
