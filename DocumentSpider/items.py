# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DocumentspiderItem(scrapy.Item):

	bianhao = scrapy.Field()
	shijian = scrapy.Field()
	danwei = scrapy.Field()
	wenhao = scrapy.Field()

	biaoti = scrapy.Field()
	zhuangtai = scrapy.Field()
	leixing = scrapy.Field()
	docid = scrapy.Field()
