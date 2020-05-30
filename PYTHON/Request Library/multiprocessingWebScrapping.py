import os
import bs4
import html5lib
import requests
import multiprocessing

def scrapFunction(url):
	response = requests.get(url)
	soup = bs4.BeautifulSoup(response.content)
	source_element = soup.findAll('img')
	source = source_element[0]['src']
	print(source)

def getPokeImg(url1):
	print(os.getpid())
	scrapFunction(url1)

def getInspImg(url2):
	print(os.getpid())
	scrapFunction(url2)

def main():
	url1 = "https://passiton.com/inspirational-quotes?page=2"
	url2 = "https://www.google.com/search?q=pokemon&sxsrf=ALeKk02CZlcgP2GUKCzdnMqRnY9BodDGGA:1590736146294&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiMl7n3wdjpAhVQ63MBHV91BjUQ_AUoAXoECBsQAw&biw=1920&bih=949"
	p1 = multiprocessing.Process(target = getPokeImg, args = (url1,))
	p2 = multiprocessing.Process(target = getInspImg, args = (url2,))
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	print('Task Completed')

if __name__ == '__main__':
	main()