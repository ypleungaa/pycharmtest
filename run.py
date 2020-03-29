import requests
from bs4 import BeautifulSoup
# test
from external_data.crawler2 import WebCrawler
if __name__ == "__main__":
    # r = requests.get("https://www.price.com.hk/category.php?c=100008")
    # soup = BeautifulSoup(r.text)
    # item = []
    # for p_soup in soup.find_all("div",{"class":"item-inner"}):
    #     item.append(str(p_soup.find("div", {"class":"line line-01"}).text).strip())
    #
    #     print(item)
    crawler1 = WebCrawler("price.com.hk")
    crawler1.search("Dyson")
    item_list = crawler1.get_items()
    print(crawler1)# return search, num of pages, num of items
    for i in item_list:
        print(i)
