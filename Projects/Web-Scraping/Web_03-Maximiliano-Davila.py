from pkg_resources import safe_name
import requests
import bs4
res = requests.get('https://www.sanignacio.pr/sobre-csi/historia-del-colegio')
res.raise_for_status
Sanignaciopr = bs4.BeautifulSoup(res.text, 'html.parser')
elems = Sanignaciopr.select('p')
print(type(Sanignaciopr))
print(len(elems))
print(str(elems))
print(elems[2].getText() + " " + elems[3].getText())


