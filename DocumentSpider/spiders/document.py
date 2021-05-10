import scrapy
from ..items import DocumentspiderItem
import pymysql
import time


class DocumentSpider(scrapy.Spider):
	name = 'document'
	allowed_domains = ['http://10.177.9.37:81/suichuan']
	start_urls = ['http://http://10.177.9.37:81/suichuan/']

	cookies = 'A176B64962F4CF815E96F497036EF11F'

	def start_requests(self):
		try:
			# 连接数据库
			self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='', db='study8', charset='utf8')
			print('连接成功<<')
		except Exception as e:
			print(f'连接失败!!>>{e}')
			exit()  # 可以直接结束运行，按需求来设定
		pass

		self.cursor = self.conn.cursor()
		try:
			# 插入数据
			self.cursor.execute('select max(shijian) from documents;')
			res = self.cursor.fetchone()
			startdate = res[0][:10]

		except Exception as e:
			print(f">>存储失败>>数据<>{e}")
			self.conn.rollback()
		pass


		enddate = time.strftime("%Y-%m-%d")






		for x in range(1,2,1):
			url='http://10.177.9.37:81/suichuan/document/ifr_list_query.jsp?subFrame=queryReceive&Page={}&CFWDW=&beginDate={}&endDate={}&CZTC=&CBT=&CWENHAO=&doctype=&gwSDate=&gwEDate=&year=&docFrom=&docStatus=3&sort=default&archiveType='.format(x,startdate,enddate)
			temp = ' JSESSIONID='+self.cookies
			cookies = {i.split('=')[0]: i.split('=')[1] for i in temp.split(';')}
			print(url)
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




