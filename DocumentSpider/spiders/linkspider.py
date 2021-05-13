import scrapy
import pymysql


class LinkspiderSpider(scrapy.Spider):
	name = 'linkspider'
	allowed_domains = ['http://10.177.9.37:81/suichuan']
	start_urls = ['http://http://10.177.9.37:81/suichuan/']
	cookies = input("cookie:")
	conn = None
	cursor = None

	def start_requests(self):
		try:
			self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='', db='study8', charset='utf8')
			print('连接成功>')
		except Exception as e:
			print(f'连接失败!!>{e}')
			exit()  # 可以直接结束运行，按需求来设定

		self.cursor = self.conn.cursor()

		try:
			row_count = self.cursor.execute("select docid,biaoti from documents WHERE `chengbanren` = '无' limit 3000;")
			print("SQL 语句查询的行数%d" % row_count)
			
			for line in self.cursor.fetchall():
				url = 'http://10.177.9.37:81/suichuan/document/ifr_docinfo_msg.jsp?NDOCID='+line[0]+'&NDOCSORTID=2&subFrame=doWaiting&NPROCID=19'
				temp = ' JSESSIONID='+self.cookies
				cookies = {i.split('=')[0]: i.split('=')[1] for i in temp.split(';')}
				# url=self.url.format(j)
				# print('begin')
				yield scrapy.Request(url=url,callback=self.parse,cookies=cookies,meta={'docid':line[0]})
				# print(url)

		except Exception as e:
			print(f">>查询失败>>{e}")
			self.conn.rollback()
		# for x in range(1,60,1):
		# 	url='http://10.177.9.37:81/suichuan/document/ifr_list_query.jsp?subFrame=queryReceive&Page={}&CFWDW=&beginDate=&endDate=&CZTC=&CBT=&CWENHAO=&doctype=&gwSDate=&gwEDate=&year=2014&docFrom=&docStatus=3&sort=default&archiveType='.format(x)
		# 	temp = ' JSESSIONID='+self.cookies
		# 	cookies = {i.split('=')[0]: i.split('=')[1] for i in temp.split(';')}
		# 	# url=self.url.format(j)
		# 	yield scrapy.Request(url=url,callback=self.parse,cookies=cookies)
		# 	pass



	def parse(self, response):

		chengbanren=response.xpath("//font[contains(text()[2],'(收文)承办')]/span/@title").get()

		docid = response.meta['docid']

		print(chengbanren,docid)
		
		try:
			self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='', db='study8', charset='utf8')
			# print('连接成功>')
		except Exception as e:
			print(f'连接失败!!>{e}')
			exit()  # 可以直接结束运行，按需求来设定

		self.cursor = self.conn.cursor()

		try:
			sql = "update documents set chengbanren = '{}' where docid = '{}'".format(chengbanren,docid)
			# print(sql)
			row_count = self.cursor.execute(sql)
			# print("SQL 语句更新的行数%d" % row_count)
			self.conn.commit()
		except Exception as e:
			print(f">>更新失败>>数据<{docid}>{e}")
			self.conn.rollback()


