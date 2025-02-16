import scrapy
from dangdang.items import DangdangItem

class DdSpider(scrapy.Spider):
    name = "dd"
    # 如果要多叶下载，需要修改allowed_domains的范围，一般只写域名
    allowed_domains = ["category.dangdang.com"]
    # 如果.html后面有'\',即'.html\',要把'\'去掉
    start_urls = ["https://category.dangdang.com/cp01.36.04.00.00.00.html"] 

    base_url = "https://category.dangdang.com/pg"
    page = 1

    def parse(self, response):
        # src = //ul[@id='component_59']/li//img/@data-original  # 注意图片的懒加载，不用src
        # nsme = //ul[@id='component_59']/li//img/@alt
        # price = //ul[@id='component_59']/li//p[@class='price']/span[1]/text()

        li_list = response.xpath("//ul[@id='component_59']/li")
        for li in li_list:
            src = li.xpath(".//img/@data-original").extract_first()
            # 第一张图的属性和其他图片的属性不一样（由于懒加载）
            # 第一张图片没有data-original，且src是可以使用的
            if src is None:
                src = li.xpath(".//img/@src").extract_first()

            name = li.xpath(".//img/@alt").extract_first()
            price = li.xpath(".//p[@class='price']/span[1]/text()").extract_first()
            # print(src, name, price)

            book = DangdangItem(src=src, name=name, price=price)
            yield book

        if self.page < 100:
            self.page += 1
            
            url = self.base_url + str(self.page) + "-cp01.36.04.00.00.00.html"

            # 多页爬取
            # scrapy.Request 就是scrapy的get请求
            # url：请求的url
            # callback：请求成功后，调用的函数
            #           注意调用的函数不需要()
            yield scrapy.Request(url=url, callback=self.parse)
