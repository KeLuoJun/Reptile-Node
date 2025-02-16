import scrapy
from dianyin.items import DianyinItem


class MvSpider(scrapy.Spider):
    name = "mv"
    allowed_domains = ["www.dy2018.com"]
    start_urls = ["https://www.dy2018.com/"]

    # 解析一级页面
    def parse(self, response):
        a_list = response.xpath("//div[@class='co_content222']//li/a")
        for a in a_list:
            name = a.xpath("./@title").extract_first()
            href = a.xpath("./@href").extract_first()

            url = "https://www.dy2018.com" + href

            # print(name, url)
            # 参数meta: 传递参数
            yield scrapy.Request(url=url, callback=self.parse_second, meta={'name': name})

    # 解析二级页面
    def parse_second(self, response):
        src = response.xpath("//div[@id='Zoom']/img[1]/@src").extract_first()

        name = response.meta['name']  # 获取传递过来的参数

        movie = DianyinItem(src=src, name=name)

        yield movie  # 将数据提交给piplines
        
