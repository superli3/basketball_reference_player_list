__author__ = 'Jeff'

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from player_list.items import PlayerListItem

class BaseSpider(BaseSpider):
    name = "players"
    allowed_domains = ["basketball-reference.com"]
    start_urls = [
        "http://www.basketball-reference.com/players/a/",
        "http://www.basketball-reference.com/players/b/",
        "http://www.basketball-reference.com/players/c/",
        "http://www.basketball-reference.com/players/d/",
        "http://www.basketball-reference.com/players/e/",
        "http://www.basketball-reference.com/players/f/",
        "http://www.basketball-reference.com/players/g/",
        "http://www.basketball-reference.com/players/h/",
        "http://www.basketball-reference.com/players/i/",
        "http://www.basketball-reference.com/players/j/",
        "http://www.basketball-reference.com/players/k/",
        "http://www.basketball-reference.com/players/l/",
        "http://www.basketball-reference.com/players/m/",
        "http://www.basketball-reference.com/players/n/",
        "http://www.basketball-reference.com/players/o/",
        "http://www.basketball-reference.com/players/p/",
        "http://www.basketball-reference.com/players/q/",
        "http://www.basketball-reference.com/players/r/",
        "http://www.basketball-reference.com/players/s/",
        "http://www.basketball-reference.com/players/t/",
        "http://www.basketball-reference.com/players/u/",
        "http://www.basketball-reference.com/players/v/",
        "http://www.basketball-reference.com/players/w/",
        "http://www.basketball-reference.com/players/x/",
        "http://www.basketball-reference.com/players/y/",
        "http://www.basketball-reference.com/players/z/",
        ]
    download_delay = 5

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select('//*[@id="players"]/tbody//tr')
        items = []
        for titles in titles:
            item = PlayerListItem()
            item ["Name"] = titles.select("td[1]//a/text()").extract()
            item ["From"] = titles.select("td[2]/text()").extract()
            item ["To"] = titles.select("td[3]/text()").extract()
            item ["Pos"] = titles.select("td[4]/text()").extract()
            item ["Ht"] = titles.select("td[5]/text()").extract()
            item ["Wt"] = titles.select("td[6]/text()").extract()
            item ["Birth_Date"] = titles.select("td[7]/a/text()").extract()
            item ["College"] = titles.select("td[8]/a/text()").extract()
            item ["player_link"] = titles.select("td[1]//a/@href").extract()
            items.append(item)
        return items
