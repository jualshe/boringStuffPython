import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(messages)s')

logging.debug('Start of the program')


def factorial(n):
    logging.debug('start of factorial(%s)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debubg('return value is %s' % (total))
    return total


print(factorial(5))
