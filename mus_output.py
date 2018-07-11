import requests
import json

class MusOutPut:
    def output_mus(self,mus_url, name, singer,filePath):
        url = "http://www.guqiankun.com/tools/music/"
        headers = {
            'X-Requested-With': 'XMLHttpRequest'                  #Ajax 异步请求
        }
        data = {
            "input":"{}".format(mus_url),                         #构造post请求的data
            'filter': 'url',
            'type': '_' ,
            'page': '1'
        }

        __response = requests.post(url, data= data,headers = headers)
        __content = __response.text
        jmus = json.loads(__content)                        #解码json
        url = jmus["data"][0]['url']

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
        mus = requests.get(url, headers=headers)

        with open(filePath + '{}-{}'.format(name, singer) + '.mp3', "wb") as f:
            f.write(mus.content)

        print("download {}-{} succeed!".format(name, singer))



