import requests
from bs4 import BeautifulSoup
def main():
    URL = 'https://sizeer.ro/sale/gen-barbati?clickId=53213'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find('div', class_="b-productList_content")
    items = results.find_all('div', class_="b-itemList_container")
    for item in items:
        title = item.find('a', class_="b-itemList_nameLink")
        price = item.find_all('p', class_="b-itemList_price")
        if None in (title, price):
            continue
        print(title.get_text())
        print(f"Pret actual: {price[1].get_text()}")
        print(f"Fostul pret: {price[0].get_text()}")
        print(" ======== ")
if __name__ == '__main__':
    main()