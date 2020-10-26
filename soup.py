from requests_html import HTMLSession
from bs4 import BeautifulSoup

session = HTMLSession()
resp = session.get("https://www.desales.edu/directory")
resp.html.render() # forces js to run

soup = BeautifulSoup(resp.html.html, "lxml")

emails = []
ext = []

for td in soup.find_all('td'):
    if "@desales.edu" in td.text:
        emails.append(td.text)
    
print(emails)
print(ext)