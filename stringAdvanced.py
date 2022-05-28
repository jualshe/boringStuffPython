# double quotes for text with a quote
print("That's her cat")

# backslash before the single quote
print('That\'s a Bob\'s mother')

print('\nHello!\n\tHow are you?\nI\'m fine')

print(r'That is Carol\'s cat')

print("""Dear Bob,
your cat has been arrested.
Sincerely,
Nate""")

spam = """Dear Bob,
your cat has been arrested.
Sincerely,
Nate"""
print(spam[0])
print(spam[5:21])
print(spam[-4:-1:2])

print('cat' in spam)
print('x' in spam)
