warning: LF will be replaced by CRLF in DocumentSpider/pipelines.py.
The file will have its original line endings in your working directory
[1mdiff --git a/DocumentSpider/pipelines.py b/DocumentSpider/pipelines.py[m
[1mindex a2f36ff..8c9b1a0 100644[m
[1m--- a/DocumentSpider/pipelines.py[m
[1m+++ b/DocumentSpider/pipelines.py[m
[36m@@ -27,32 +27,38 @@[m [mclass DocumentspiderPipeline(object):[m
 [m
     def open_spider(self, spider):[m
         # 进行异常处理，可能会因为我们的疏忽或者数据库的更改造成连接失败，所以，我们要对这部分代码块进行异常捕捉[m
[31m-        try:[m
[31m-            # 连接数据库[m
[31m-            self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='', db='study8',[m
[31m-                                        charset='utf8')[m
[31m-            print('连接成功<<')[m
[31m-        except Exception as e:[m
[31m-            print(f'连接失败!!>>{e}')[m
[31m-            exit()  # 可以直接结束运行，按需求来设定[m
[32m+[m[32m        if spider.name == 'document':[m
[32m+[m[32m            try:[m
[32m+[m[32m                # 连接数据库[m
[32m+[m[32m                self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='', db='study8', charset='utf8')[m
[32m+[m[32m                print('连接成功<<')[m
[32m+[m[32m            except Exception as e:[m
[32m+[m[32m                print(f'连接失败!!>>{e}')[m
[32m+[m[32m                exit()  # 可以直接结束运行，按需求来设定[m
[32m+[m
[32m+[m[32m            pass[m
[32m+[m
 [m
     def process_item(self, item, spider):[m
[31m-        # 创建游标[m
[31m-        self.cursor = self.conn.cursor()[m
[31m-        try:[m
[31m-            # 插入数据[m
[31m-            self.cursor.execute([m
[31m-                'INSERT INTO scrapy_document (bianhao,shijian,danwei,wenhao,biaoti,zhuangtai,leixing,docid,chengbanren) VALUES("{}", "{}","{}", "{}","{}", "{}","{}", "{}","{}")'.format(item['bianhao'], item['shijian'],item['danwei'], item['wenhao'],item['biaoti'], item['zhuangtai'],item['leixing'], item['docid'],'无'))[m
[31m-            print(f"数据<{item['docid']}>数据提交中...")[m
[31m-            # 数据提交到数据库[m
[31m-            self.conn.commit()[m
[31m-        except Exception as e:[m
[31m-            print(f">>存储失败>>数据<{item['docid']}>{e}")[m
[31m-            self.conn.rollback()[m
[31m-        return item[m
[32m+[m[32m        if spider.name == 'document':[m
[32m+[m[32m            # 创建游标[m
[32m+[m[32m            self.cursor = self.conn.cursor()[m
[32m+[m[32m            try:[m
[32m+[m[32m                # 插入数据[m
[32m+[m[32m                self.cursor.execute('INSERT INTO scrapy_document (bianhao,shijian,danwei,wenhao,biaoti,zhuangtai,leixing,docid,chengbanren) VALUES("{}", "{}","{}", "{}","{}", "{}","{}", "{}","{}")'.format(item['bianhao'], item['shijian'],item['danwei'], item['wenhao'],item['biaoti'], item['zhuangtai'],item['leixing'], item['docid'],'无'))[m
[32m+[m[32m                print(f"数据<{item['docid']}>数据提交中...")[m
[32m+[m[32m                # 数据提交到数据库[m
[32m+[m[32m                self.conn.commit()[m
[32m+[m[32m            except Exception as e:[m
[32m+[m[32m                print(f">>存储失败>>数据<{item['docid']}>{e}")[m
[32m+[m[32m                self.conn.rollback()[m
[32m+[m[32m            return item[m
[32m+[m[32m            pass[m
 [m
     def close_spider(self, spider):[m
[31m-        # 先关闭游标[m
[31m-        self.cursor.close()[m
[31m-        # 再关闭连接[m
[31m-        self.conn.close()[m
[32m+[m[32m        if spider.name == 'document':[m
[32m+[m[32m            # 先关闭游标[m
[32m+[m[32m            self.cursor.close()[m
[32m+[m[32m            # 再关闭连接[m
[32m+[m[32m            self.conn.close()[m
[32m+[m[32m            pass[m
