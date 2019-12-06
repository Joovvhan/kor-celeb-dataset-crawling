# -*- coding: utf-8 -*-

from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler

keywords = []

with open('kor_female_idol_list.txt', encoding='UTF-8') as f:
    lines = f.readlines()
    keywords = [line.strip() for line in lines]

for keyword in keywords:

    save_path = 'D:/Korean Celeb Data/' + keyword

    google_crawler = GoogleImageCrawler(
        feeder_threads=1,
        parser_threads=1,
        downloader_threads=4,
        storage={'root_dir': save_path + '/google'})

    filters = dict(type = "face")

    google_crawler.crawl(keyword=keyword, filters=filters, offset=0, max_num=1000,
                         min_size=(200,200), max_size=None, file_idx_offset=0)

    bing_crawler = BingImageCrawler(downloader_threads=4,
                                    storage={'root_dir': save_path + '/bing'})
    bing_crawler.crawl(keyword=keyword, filters=None, offset=0, max_num=1000)

    baidu_crawler = BaiduImageCrawler(storage={'root_dir': save_path + '/baidu'})
    baidu_crawler.crawl(keyword=keyword, offset=0, max_num=1000,
                        min_size=(200,200), max_size=None)