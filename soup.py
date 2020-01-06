import requests
from bs4 import BeautifulSoup

#company = soup.find("a", string="Listed Companies")
#specific = company.find("a", string="NBK")

Companies = ["NBK", "KAMCO", "MABANEE", "ZAIN"]
print("Companies")
for index, company in enumerate(Companies):
	print(str(index + 1), company)
choice = input("Kindly choose a company from the list above to display current stock price:")

if choice == "1":
	result = requests.get("https://english.mubasher.info/markets/BK/stocks/NBK/profile")
	src = result.content
	soup = BeautifulSoup(src, 'lxml')
	stock = soup.find(class_="market-summary__last-price").get_text()
	print(stock)
elif choice == "2":
	result = requests.get("https://english.mubasher.info/markets/BK/stocks/KAMCO/profile")
	src = result.content
	soup = BeautifulSoup(src, 'lxml')
	stock = soup.find(class_="market-summary__last-price").get_text()
	print(stock)
elif choice == "3":
	result = requests.get("https://english.mubasher.info/markets/BK/stocks/MABANEE/profile")
	src = result.content
	soup = BeautifulSoup(src, 'lxml')
	stock = soup.find(class_="market-summary__last-price").get_text()
	print(stock)
elif choice == "4":
	result = requests.get("https://english.mubasher.info/markets/BK/stocks/ZAIN/profile")
	src = result.content
	soup = BeautifulSoup(src, 'lxml')
	stock = soup.find(class_="market-summary__last-price").get_text()
	print(stock)