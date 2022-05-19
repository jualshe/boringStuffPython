# myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
# print(myCat['size'])
# print('My cat has ' + myCat['color'] + ' fur.')

# spam = {12345: ' luggage combination', 42: 'The Answer'}
# print(spam)

# print([1, 2, 3] == [3, 2, 1])
#
# print({1, 2, 3} == {3, 2, 1})

# Dictionaries vs. Lists - disctionaries doesn't have order
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
# print(eggs == ham)
# print('name' in eggs)
# print('name' not in eggs)

# print(eggs.keys())
# print(eggs.values())
# print(eggs.items())

for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for i in eggs.items():
    print(i)

for k, v in eggs.items():
    print(k, v)

print('cat' in eggs.values())

if 'color' in eggs:
    print(eggs['color'])

if 'name' in eggs:
    print(eggs['name'])
