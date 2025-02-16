import scrapy
import json

class FanyiSpider(scrapy.Spider):
    name = "fanyi"
    allowed_domains = ["fanyi.baidu.com"]
    # post请求 在没有参数的情况下,请求将无法正常访问
    # 所以start_uels 没有用
    # 对应的parse方法也没用了
    # start_urls = ["https://fanyi.baidu.com/sug"]

    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = "https://fanyi.baidu.com/sug"
        
        data = {
            "kw": "python"
        }

        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_detail)

    def parse_detail(self, response):
        content = response.text
        obj = json.loads(content)
        print(obj)