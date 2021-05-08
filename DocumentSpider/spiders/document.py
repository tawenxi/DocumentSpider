import scrapy
from ..items import DocumentspiderItem


class DocumentSpider(scrapy.Spider):
	name = 'document'
	allowed_domains = ['http://10.177.9.37:81/suichuan']
	start_urls = ['http://http://10.177.9.37:81/suichuan/']

	cookies = '730A844B266314BFE86F588DBD39BE3B'

	def start_requests(self):
		for x in range(1,2,1):
			url='http://10.177.9.37:81/suichuan/document/ifr_list_query.jsp?subFrame=queryReceive&Page={}&CFWDW=&beginDate=&endDate=&CZTC=&CBT=&CWENHAO=&doctype=&gwSDate=&gwEDate=&year=2014&docFrom=&docStatus=3&sort=default&archiveType='.format(x)
			temp = ' JSESSIONID='+self.cookies
			cookies = {i.split('=')[0]: i.split('=')[1] for i in temp.split(';')}
			# url=self.url.format(j)
			yield scrapy.Request(url=url,callback=self.parse,cookies=cookies)
			pass
		


	def parse(self, response):

		# with open('itcast.html', 'wb') as f:
		# 	f.write(response.body)
		# print(response.body)
		
		node_list=response.xpath('//tr[@class="underline1"]')


		print(len(node_list))
		for node in node_list:
			items=DocumentspiderItem()
			items['bianhao']=node.xpath('./td/span[@class="rowSndisplay"]/@title').get()
			items['shijian']=node.xpath('./td/span[@class="rowDate"]/@title').get()
			items['danwei']=node.xpath('./td/span[@class="rowEntity"]/@title').get()
			items['wenhao']=node.xpath('./td/span[@class="rowWenHao"]/@title').get()
			# print(items)
			items['biaoti']=node.xpath('./td/a/span[@class="rowTitle"]/@title').get()
			items['zhuangtai']=node.xpath('./td/span[@id="f6"]/text()').get()
			items['leixing']=node.xpath('./td/span[@id="f7"]/text()').get()



			docid_str=node.xpath('./td[@class="idx_item2a"]/a/@href').get()
			docid_str=docid_str[(docid_str.index("&NDOCID=")+8):docid_str.index("&NDOCSORTID")]

			items['docid']=docid_str
			print(items)
			yield items




