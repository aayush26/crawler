import requests
from bs4 import BeautifulSoup
from math import *

f = open("level_1.txt", "w")
g = open("log_1.txt","w")
urls = []
urls_2 = []

letter = "0-9"
flag = 1
while( letter <= "z"):
	url = "http://jobsearch.naukri.com/top-jobs-by-designations-"+letter+"#desig"+letter
	source = requests.get(url)
	text = source.text  			#regex for div "<div\b[^>]*>"
	#print text_2
	soup = BeautifulSoup(text)
	#print soup.body
	try:
		i = soup.find('div',{'class':'tabCont colspan_four'})
		# print i
		# print j
		# k = i.find("a").get("title")
		j = i.find("div")
		for l in j.find_all("a"):
			# print l
			k = l.get("href")
			# print k
			urls.append(k)
			f.write(k)
			f.write("\n")
		print url
		if(flag==1):
			letter = "`"
			flag = 0
	except:
		g.write(url)
	letter = chr(ord(letter)+1)	
# print urls[0]

# page_no = 1
# cnt = 1	
# once_flag = 1
# # while(page_no<=cnt):
# url_2 = urls[0]+"-"+str(3)
# print url_2
# source_2 = requests.get(url_2)
# text_2 = source_2.text
# # print text_2[:25000]
# soup_2 = BeautifulSoup(text_2)
# # if(once_flag==1):
# # 	cnt = soup_2.find('span',{'class':'cnt'}).text.split(" ")
# # 	cnt = ceil(float(cnt[2])/50)
# # print soup_2
# i_2 = soup_2.find('div',{'class':'srp_container fl  '})
# # print i_2
# for j_2 in i_2.find_all("div",{'class':'row  '}):
# 	# print j_2
# 	k_2 = j_2.find("a").get("href")
# 	f.write(k_2)
# 	f.write("\n")
# 	urls_2.append(k_2)
# 	# print k_2
# # page_no=page_no+1
# # once_flag = 0

# print len(urls_2)