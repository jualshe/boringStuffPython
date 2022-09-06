import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print('Status code ' + str(res.status_code))

print(len(res.text))
print(res.text[:500])

# raise the error if present and do nothing if succeeded
print(res.raise_for_status())

# handle the error case without crashing
# badRes = requests.get('https://automatetheboringstuff.com/files/rj.1111txt')
# print(badRes.raise_for_status())

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()

print(playFile)
