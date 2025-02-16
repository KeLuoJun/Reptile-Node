# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from scrapy.utils.project import get_project_settings  # 加载项目配置文件
import pymysql

class ReadbookPipeline:
    def open_spider(self, spider):
        self.items = []
    def process_item(self, item, spider):
        self.items.append(dict(item))
        return item
    
    def close_spider(self, spider):
        with open("../../../../data/readbook.json", 'w', encoding='utf-8') as f:
            json.dump(self.items, f, ensure_ascii=False, indent=4)


class MysqlPipeline:
    def open_spider(self, spider):
        settings = get_project_settings()
        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.user = settings['DB_USER']
        self.password = settings['DB_PASSWORD']
        self.name = settings['DB_NAME']
        self.charset = settings['DB_CHARSET']

        self.connect()

    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.name,
            charset=self.charset
        )
        self.cursor = self.conn.cursor()


    def process_item(self, item, spider):
        sql = 'insert into book(name, src, author) values("{}", "{}", "{}")' \
                .format(item['name'], item['src'], item['author'])
        self.cursor.execute(sql)  # 执行sql语句
        self.conn.commit()        # 提交sql语句

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()