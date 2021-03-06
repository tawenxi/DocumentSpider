import scrapy
from ..items import DocumentspiderItem


class DocumentSpider(scrapy.Spider):
	name = 'document'
	allowed_domains = ['http://10.177.9.37:81/suichuan']
	start_urls = ['http://http://10.177.9.37:81/suichuan/']
    

	def start_requests(self):
		url='http://10.177.9.37:81/suichuan/document/ifr_list_query.jsp?subFrame=queryReceive&Page=1&CFWDW=&beginDate=&endDate=&CZTC=&CBT=&CWENHAO=&doctype=&gwSDate=&gwEDate=&year=2021&docFrom=&docStatus=3&sort=default&archiveType='
		temp = ' JSESSIONID=A963FAF878CC8CA5491B0A9161C7B785'
		cookies = {i.split('=')[0]: i.split('=')[1] for i in temp.split('; ')}
        # url=self.url.format(j)
		yield scrapy.Request(url=url,callback=self.parse,cookies=cookies)


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




