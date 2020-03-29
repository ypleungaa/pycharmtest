# crawler1 = WebCrawler("price.com.hk")
# crawler1.search("Sony")
# item = crawler1.get_items()
# print(crawler1)  # return search, num of pages, num of items
import external_data
from Product.pricehk import CrawlItem
import requests
import time
from bs4 import BeautifulSoup
class WebCrawler():
    def __init__(self, domain):
        if domain == "price.com.hk":
          self.baseURL = external_data.URL_PRICEDOTCOM
        self.domain = domain
        self.keyword = ""
        self.item_list = []

    def __str__(self):
        return """
        Domain: %s
        keyword: %s
        No.items %d
        """%(self.domain, self.keyword, len(self.item_list))

    def search(self, keyword):
        self.keyword = keyword
        item_list = []
        page_num = 1

        while True:
            searchURL = self.baseURL + keyword + "&page=" + str(page_num)
            r = requests.get(searchURL)
            soup = BeautifulSoup(r.text, "html.parser")
            find_result = soup.find_all("div", {"class": "item-inner"})
            if len(find_result) == 0:
                break
            for p_soup in find_result:
                p_item = CrawlItem()
                p_item.header = str(p_soup.find("div", {"class":"line line-01"}).text).strip()
                if p_soup.find("span", {"class":"text-price-number"}):
                    p_item.price = int(str(p_soup.find("span", {"class":"text-price-number"}).text).replace(" ","").replace(",","").strip())
                else:
                    p_item.price = -1
                item_list.append(p_item)
            page_num +=1
            time.sleep(0.5)
        self.item_list = item_list
        self.total_page = page_num - 1


    def get_items(self):
        return self.item_list