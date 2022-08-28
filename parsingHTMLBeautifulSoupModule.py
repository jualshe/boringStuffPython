# web scraping
import bs4
import requests

res = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/')
# res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)

print(soup)
