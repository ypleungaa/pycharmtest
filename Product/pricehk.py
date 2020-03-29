class CrawlItem():
    def __init__(self):
        self.header = ""
        self.price = 0
    def __str__(self):
        return "Name:  %s, Price: %d"%(self.header, self.price)