import requests
from bs4 import BeautifulSoup

def viooz_country_argentina(max_pages):
	page=1;
	while page <= max_pages:
		url = "http://viooz.ac/country/Argentina/page/" + str(page)
		source_code = requests.get(url)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text)
		page=page+1
		for link in soup.findAll('span', {'class': 'title_list'}):
			title_link = link.find('a').get('href');
			title = link.string
			print title_link
			print "\nTitle:"	
			print title
			movies_info(title_link)
			print "-------------------------------------------------------------------"

def movies_info(info_url):
	source_code = requests.get(info_url)
	plain_text = source_code.text
	soup=BeautifulSoup(plain_text)
	for link in soup.findAll('div',{'class': 'summary summary_film boxed'}):
		print "\nDescription:"
		info = link.string
		print info

viooz_country_argentina(1)
