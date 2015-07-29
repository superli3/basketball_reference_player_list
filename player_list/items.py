# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field

class PlayerListItem(Item):
    Name = Field()
    From = Field()
    To = Field()
    Pos = Field()
    Ht = Field()
    Wt = Field()
    Birth_Date = Field()
    College = Field()
    player_link = Field()
    pass
