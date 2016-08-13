# Instructions:
# Create a new directory
# Copy this program inside it and Run it.
# To Run: Type in cmd
# python library_cornell_ebook.py
# All other requirements as you mentioned will be followed automatically

from reportlab.pdfgen import canvas
import glob
import requests
from bs4 import BeautifulSoup
import os

year = []
issue = ["January","April","July","October"]

def years(start, end):
	for i in range(start, end+1):
		year.append(i)

years(1844,1852)
# print year

urls = []

def getImage(link, pageNo):
	sc = requests.get(link)
	pt = sc.text
	soup = BeautifulSoup(pt)
	for retry in range(50):
		try:
			i = soup.find('img',{'alt':'Page image'})
			# print i
			j = "http://ebooks.library.cornell.edu"+i.get("src")
			print j
			os.system('wget -O %s.gif %s' %(pageNo, j))
			pdfname = str(pageNo)+".pdf"
			gifname = str(pageNo)+".gif"
			c = canvas.Canvas(pdfname)
			for fn in glob.glob(gifname):
				dim=c.drawImage(fn,0,0)
				c.setPageSize(dim)
				c.showPage()
			c.save()
			os.system('rm -rf *.gif')
			pageNo = pageNo+1
			m = soup.find('img',{'alt':'Next Page'})
			if m==None:
				break
			else:
				m = m.parent.get("href")
			# print m
			if m==link:
				break
			else:
				getImage(m, pageNo)
			break
		except:
			status = "Retry: "+str(retry)
			print status
			print "\n"
			pass

for i in range(58,76):
	url = "http://ebooks.library.cornell.edu/cgi/t/text/text-idx?c=nora;cc=nora;view=toc;subview=short;idno=nora00"+str(i)+"-1"
	urls.append(url)
	url = "http://ebooks.library.cornell.edu/cgi/t/text/text-idx?c=nora;cc=nora;view=toc;subview=short;idno=nora00"+str(i)+"-2"
	urls.append(url)

# print urls

year_count = 0
flag = 0
yc = 0
ic = 0
for i in range(len(urls)):
	if year_count%4==0:
		if flag:
			os.chdir("..")
		os.system('mkdir %s' %year[yc])
		os.chdir('%s' %year[yc])
		yc=yc+1
		flag=1
	os.system('mkdir %s' %issue[ic%4])
	os.chdir('%s' %issue[ic%4])
	ic=ic+1
	pageNo=1
	sc = requests.get(urls[i])
	pt = sc.text
	soup = BeautifulSoup(pt)
	# print pt
	try:
		i = soup.find('a',{'class':'articletitle'})
		# print i
		j = i.get("href")
		# print j
		getImage(j, pageNo)
	except:
		pass
	os.chdir("..")
	year_count = year_count + 1
