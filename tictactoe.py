import pprint

theBoard = {'top-L': '', 'top-M': '', 'top-R': '', 'mid-L': 'X', 'mid-M': '', 'mid-R': '', 'low-L': '', 'low-M': '',
            'low-R': ''}
pprint.pprint(theBoard)

theBoard['mid-L'] = ''
pprint.pprint(theBoard)
