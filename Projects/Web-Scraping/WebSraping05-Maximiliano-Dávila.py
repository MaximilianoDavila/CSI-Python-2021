import re
import bs4
import requests

website = 'https://xkcd.com'

response = requests.get(website)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup. find_all('img')

urls = [img['src'] for img in img_tags]

for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    if not filename:
        print("Didn't match with teh url: {}". format(url))
        continue
    with open(filename.group(1), 'wb') as f:
        if 'https' not in url:
            url = '{}{}'. format(website, url)
        response = requests.get(url)
        f.write(response.content)