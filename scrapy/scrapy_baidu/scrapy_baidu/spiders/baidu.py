import scrapy


class BaiduSpider(scrapy.Spider):
    name = "baidu"     # 运行爬虫文件时使用的名字
    allowed_domains = ["www.baidu.com"]  # 爬虫允许的域名，在爬取的时候，如果不是此域名之下的url，会被过滤掉
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        # 验证反爬，能打印出来，说明没有被反爬
        # 若有反爬，首先关闭settings.py中的ROBOTSTXT_OBEY
        print("=======================================================")
        response.text  # 响应的是字符串
        response.body  # 响应的是二进制文件
        input_button = response.xpath("//input[@id='su']/@value")[0]  # xpath方法的返回值类型是selector列表
        input_button.extract()        # 提取的是selector对象的是data
        input_button.extract_first()  # 提取的是selector列表中的第一个数据

