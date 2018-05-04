import scrapy
import re

class IonicSpider(scrapy.Spider):
    name = "ionic_spider"
    start_urls = ['https://en.wikipedia.org/wiki/Ionic_(mobile_app_framework)']
    line_count = -1
    with open('input_format.txt') as f:
        lines = [line.strip() for line in f]

    def parse(self, response):
        IonicSpider.line_count += 1

        while(True):
            if 'next' in IonicSpider.lines[IonicSpider.line_count]:
                IonicSpider.line_count += 1
                break
            else:
                selector = IonicSpider.lines[IonicSpider.line_count]
                IonicSpider.line_count += 1

                content = response.xpath(selector).extract_first()
                content = content.replace('\n',' ')
                content = re.sub('<[^>]*>', '', content) # remove tags from the extracted text
                content = re.sub('[\[].*?[\]]', '', content) # remove square brackets and text contained in them
                
                # uncomment the lines below to see output in the console
                # yield {
                #     "content" : content,
                # }
                print("Content : \n",content,"\n")

        if 'exit' in IonicSpider.lines[IonicSpider.line_count]:
            pass
        else:
            yield scrapy.Request(
                response.urljoin(IonicSpider.lines[IonicSpider.line_count]),
                callback=self.parse
                )
