import pprint

cat = {'name': 'Rizhik', 'age': 7, 'color': 'gray'}
print(cat)

allCats = []
allCats.append({'name': 'Rizhik', 'age': 7, 'color': 'ginger'})
allCats.append({'name': 'Chernushka', 'age': 5, 'color': 'bblack'})
allCats.append({'name': 'Coco', 'age': 5, 'color': 'gray'})
allCats.append({'name': '???', 'age': -1, 'color': 'orange'})
pprint.pprint(allCats)
