# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from urllib.request import urlretrieve 

# 需要在settings.py中把pipelines开关打开
class DangdangPipeline:
    # item: dd.py传过来的的DangdangItem

    def __init__(self):
        self.items = []
    # 爬虫开始爬取数据时调用
    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.items.append(dict(item))
        return item
    
    # 爬虫结束爬取数据时调用
    def close_spider(self, spider):
        # 将数据写入到文件中
        with open("../../../../data/book.json", "w", encoding="utf-8") as f:
            json.dump(self.items, f, ensure_ascii=False, indent=4)

# 多管道开启
#   (1) 定义管道类
#   (2) 在settings.py中开启管道
class DangdangDownloadPipeline:
    '''下载图片的pipeline'''
    def process_item(self, item, spider):
        url = 'http:'+ item.get('src')
        filename = '../../../../data/books/' + item.get('name') + '.jpg'
        urlretrieve(url, filename)
        return item
