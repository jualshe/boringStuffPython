import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)

print(len(res.text))
print(res.text[:50])

badRes = requests.get('https://automatetheboringstuff.com/files/rj.1111txt')

print(badRes.raise_for_status())
