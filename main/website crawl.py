import scrapy
class BossjobSpider(scrapy.Spider):
    name = ""
    allowed_domains = []
    current_page = 1
    max_page = 10
    start_url ={
        "https://www.zhipin.com/c101020100-p100101/?ka=sel-city-101020100"

    }
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS":{
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
            'Referer': 'https://www.zhipin.com/',
        }
    }