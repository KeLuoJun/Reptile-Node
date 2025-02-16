import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from readbook.items import ReadbookItem


class ReadSpider(CrawlSpider):
    name = "read"
    allowed_domains = ["www.dushu.com"]
    start_urls = ["https://www.dushu.com/lianzai/1116_1.html"]

    rules = (
        Rule(LinkExtractor(allow=r"/lianzai/1116_\d+.html"), 
                            callback="parse_item", 
                            follow=True),  # follow=True: 继续爬取匹配规则的链接
    )
    def parse_item(self, response):
        data_list = response.xpath("//div[@class='bookslist']//li")
        for data in data_list:
            src = data.xpath(".//h3/a/@href").extract_first()
            src = "https://www.dushu.com" + src
            name = data.xpath(".//h3/a/text()").extract_first()
            author = data.xpath(".//p/a/text()").extract_first()

            yield scrapy.Request(url=src, callback=self.parse_second, meta={"name": name, "author": author})
        
        # 输出当前页面提取到的所有链接
        links = LinkExtractor(allow=r"/lianzai/1115_\d+.html").extract_links(response)
        self.logger.info(f"Extracted links: {[link.url for link in links]}")

    def parse_second(self, response):
        name = response.meta["name"]
        author = response.meta["author"]
        img_src = response.xpath('//div[@class="book-pic"]//img/@src').extract_first()

        book = ReadbookItem(src=img_src, name=name, author=author)
        yield book
        


