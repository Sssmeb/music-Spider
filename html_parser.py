import requests
import json
import random

class HtmlParser():

    def parse(self,root_url):
        ua_list = (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
            "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
        )

        headers = {"User-Agent": random.choice(ua_list)}
        __response = requests.get(root_url, headers= headers)
        __content = __response.text
        jcontent = __content.strip("MusicJsonCallback1865217132890724(").strip(")")
        jmus = json.loads(jcontent)               #解码json格式
        mid = jmus["data"]["song"]["list"][0]['mid']
        name = jmus["data"]["song"]["list"][0]["title"]
        singer = jmus["data"]["song"]["list"][0]["singer"][0]["name"]

        return mid,name,singer
