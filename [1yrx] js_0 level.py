# （第1题）入门级js（0难度）：抓取这5页的数字，计算加和并提交结果 base64 
import requests
import base64
from fake_useragent import UserAgent
import time
import numpy as np
import pandas as pd

data=[]
class Yrx():
    def __init__(self) :
#         self.url='http://match.yuanrenxue.com/api/match/12?page={0}&m={1}'
#——————————————————————————————————————————
        self.url='http://match.yuanrenxue.com/api/match/12'
        ua = UserAgent(verify_ssl=False)
        self.headers = {'User-Agent': ua.random}
    def get_html(self):
        for i in range(1,6):
            str_url="yuanrenxue"+str(i)
            encode_url = base64.b64encode(str_url.encode("utf-8")) 
            encode_url =encode_url.decode("utf-8")
#             url=self.url.format(i,encode_url)
#             res=requests.get(url=url, headers=self.headers).json()
#——————————————————————————————————————————
            query = {"page":i ,"m":encode_url}
            res = requests.get(url=self.url,headers=self.headers, params=query).json()
            data.extend(res['data'])
            time.sleep(np.random.randint(1, 4))
    def main(self):
        self.get_html()
        df=pd.DataFrame(data)
        print(df.sum())
if __name__ =='__main__':
    yrx=Yrx()
    yrx.main()
