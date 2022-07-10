import re

namesRegex = re.compile(r'Agent \w+')
text = 'Agent Alice gave the secret documents to Agent Bob.'
mo = namesRegex.findall(text)
print(mo)
print(namesRegex.sub('REDACTED', text))
