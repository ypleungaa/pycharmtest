# crawler1 = WebCrawler("price.com.hk")
# crawler1.search("Sony")
# item = crawler1.get_items()
# print(crawler1)  # return search, num of pages, num of items
class WebCrawler():
    def __str__(self):
        return "This is a crawler"
    def search(self, ):
        req = requests.get("https://www.price.com.hk/search.php?g=A&q="+%r)
        soup = BeautifulSoup(req.text)
    def get_items(self):
        item = []
        for p_soup in soup.find_all("div",{"class":"item-inner"}):
            item.append(str(p_soup.find("div", {"class":"line line-01"}).text).strip())

            print(item)