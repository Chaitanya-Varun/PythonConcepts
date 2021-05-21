from multiprocessing import Pool #for pooling the tasks
import bs4 as bs#For scraping the web page properly
import requests #When try to move from one website other helps in creating requests
import string #we will be writing the weblinks in strings
import random #for starting up with random links

def random_starting_url():
	starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))
	url = ''.join(['http://',starting,'.com'])
	return url
url = random_starting_url()
# print(url)

def handle_local_links(url,link):
	if(link.startswith('/')):
		return ''.join([url,link])
	else:
		return link

def get_links(url):
	try:
		resp = requests.get(url)
		soup = bs.BeautifulSoup(resp.text,"lxml")
		body = soup.body
		links = [link.get('href') for link in body.find_all('a')]
		links = [handle_local_links(url,link) for link in links]
		links = [str(link.encode("ascii")) for link in links]
		return links
	except TypeError as e:
		print(e)
		print("No links in the taken URL")
		return []
	except IndexError as e:
		print(e)
		print("No useful links")
		return []
	except AttributeError as e:
		print(e)
		print("invalid links")
		return []		
	except Exception as e:
		print(str(e))
		return []



def main():
	initial_num =100
	p = Pool(processes=initial_num)
	parse_us = [random_starting_url() for _ in range(initial_num)]
	# while True:
	# 	data = p.map(get_links,[link for link in parse_us])
	# 	data=[url for url_list in data for url in url_list]
	# 	parse_us=data
	data = p.map(get_links,[link for link in parse_us])
	data=[url for url_list in data for url in url_list]
	parse_us=data
	p.close()

	with open('urls.txt','w') as f:
		f.write(str(data))


if __name__=='__main__':
	main()