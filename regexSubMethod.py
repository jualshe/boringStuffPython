import re

namesRegex = re.compile(r'Agent \w+')
text = 'Agent Alice gave the secret documents to Agent Bob and Agent C.'
mo = namesRegex.findall(text)
print(mo)
print(namesRegex.sub('REDACTED', text))

# using \1, \2 etc in sub()
namesRegex = re.compile(r'Agent (\w)\w*')
text = 'Agent Alice gave the secret documents to Agent Bob and Agent C.'
mo = namesRegex.findall(text)
print(mo)

mo = namesRegex.sub(r'Agent \1****', text)
print(mo)
