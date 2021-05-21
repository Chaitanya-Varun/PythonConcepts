import bs4 as bs
import urllib.request

# sauce = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
# #print(sauce)#Source code in clumsy way
# soup = bs.BeautifulSoup(sauce,'lxml')
#print(soup)#the source html code

# print(soup.title)
# print(soup.title.string)
# print(soup.title.text)

# print(soup.find_all('p'))
# for paragraph in soup.find_all("p"):
# 	# print(paragraph.string) #Thhis will not print the navigatable strings
# 	print(paragraph.text)#this does all

# print(soup.getText()) # similar to soup.text

# for url in soup.find_all('a'):
# 	print(url.get('href'))

# nav = soup.nav
# # print(nav)

# for url in nav.find_all('a'):
# 	print(url.get('href'))

# table = soup.table
# # print(table)
# table_rows = table.find_all('tr')
# for tr in table_rows:
# 	td = tr.find_all('td')
# 	#print(td)
# 	row = [i.text for i in td]
# 	print(row)


# sauce = urllib.request.urlopen("https://pythonprogramming.net/sitemap.xml").read()
# #print(sauce)#Source code in clumsy way
# soup = bs.BeautifulSoup(sauce,'xml')
# # print(soup)#all urls

# for url in soup.find_all('loc'):
# 	print(url.text)

