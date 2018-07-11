import html_parser
import mus_output
import requests
import os

class SpiderMain(object):
    def __init__(self):
        self.parser = html_parser.HtmlParser()
        self.outputer = mus_output.MusOutPut()
        self.filePath = ("/spider-work/mus-spider/music/")

    def file(self):
        filePath = self.filePath
        if not os.path.exists(filePath):            #递归创建目录树
            os.makedirs(filePath)

    def craw(self, root_url):
        try:
            self.file()
            mid,name,singer = self.parser.parse(root_url)
            #print(mid,name,singer)
            mus_url = "https://y.qq.com/n/yqq/song/{}.html".format(mid)
            #print(mus_url)
            self.outputer.output_mus(mus_url, name, singer,self.filePath)


        except Exception as e:
            print("cannot find the song……")

if __name__ == '__main__':
    keyWord = input("please input the keyWord:")
    root_url =("https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=70181797221190725&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w={}&jsonpCallback=MusicJsonCallback1865217132890724&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0").format(keyWord)
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
