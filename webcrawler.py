import requests
from bs4 import BeautifulSoup

def spider(max_pages):
	pages = 1
	while pages <= max_pages:
		url = 'https://thenewboston.com/forum/search_forums.php?s=&orderby=popular&page='+str(pages)
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text)
		for link in soup.findAll('a',{'class':'title text-semibold'}):
			
		
		