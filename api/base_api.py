import json
import re

import requests

# todo 第一层：分析接口测试-剥离重复的动作-封装到BaseApi中（比如gettoken,send）
# todo 第二层：将接口封装成一个个独立的方法，进行参数化处理，方便后期测试进行调用
# todo 第三层：创建api对应的测试文件，设计我们的测试用例
# todo 第四层：执行测试用例（数据驱动&关键字驱动）使用pytest框架中的功能进行数据驱动
"""
第二层技术点 参数化设计（参数非常多30+）
第三层技术点 用例设计，用例流程设计，jsonpath,断言设计
第四层技术点 执行方式，数据的来源，数据的保存，数据的重复使用
"""


class BaseApi:
    def __init__(self):
        self.wework = self.gettoken()

    def send(self, kwargs):
        r = requests.request(**kwargs)
        print(json.dumps(r.json(), indent=1, ensure_ascii=False))
        return r


    def gettoken(self):
        # todo:获取 access_token
        name = "lsj1"
        password = "123123"
        data = {
            "method": "post",
            "headers":{
                "Content-Type": "application/json;charset=UTF-8"
            },
            "url": "http://123.56.138.96:3012/api/ainews-user/user/login",
            "json": {
                "name": name,
                "password": password
            }
        }
        token = self.send(data).json()['access_token']
        return token

    def parser(self, data):
        """
        checkout: 处理data 返回str
        checkouts_list: 切割str 返回字段list
        :param data: 接口返回 转换成json
        :return: set集合
        """
        checkout = re.sub("{|}|\'|\"|\\[|\\]| ", "", json.dumps(data, ensure_ascii=False))
        checkouts_list = re.split(":|,", checkout)
        return set(checkouts_list)



if __name__ == '__main__':
    print(BaseApi().gettoken())



# if __name__ == "__main__":
#     data = {
#         "header":
#             {
#                 "autograph": "MD5",
#                 "retCode": "000000",
#                 "retMsg": "处理成功"
#             },
#         "body":
#             {
#                 "serviceFee": "",
#                 "payerVirAcctNo": "720967000052",
#                 "transMsg": "交易处理中",
#                 "detailList":
#                     [
#                         {
#                             "transMsg": "交易处理中！",
#                             "amount": "1.99",
#                             "subOutSeqNo": "elh11600842021",
#                             "payeeVirAcctName": "王小锤",
#                             "yurref": "TBATE2009230000002",
#                             "transStatus": "1",
#                             "payeeVirAcctNo": "6222981475606661",
#                             "transSucDate": ""
#                         },
#                     ],
#                 "outSeqNo": "wb1600842021",
#                 "yurref": "TBATE2009230000001",
#                 "transStatus": "1",
#                 "payeeAccType": "2"
#             }
#     }
# print(BaseApi().parser(data))
