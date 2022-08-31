# web scraping
import bs4, requests

res = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/')
# res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

soup.select('#corePrice_feature_div > div > span > span:nth-child(2)')

print(soup)
