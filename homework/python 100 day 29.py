import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import  get_project_settings
from _datetime import datetime
import time

def main(a):
    target_board = [a]
    process = CrawlerProcess(get_project_settings())
    for board in target_board:
        process.crawl('ptt29', board=board ,filename='{b}{a}ptt'.format(a=board,b=datetime.now().strftime('%m%d')))
        process.start()

bb=['stock']
for b in bb:
    print(b)
    a = b
    if __name__ == '__main__':
        main(a)

