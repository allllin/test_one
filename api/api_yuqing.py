"""
PageObject:
两大核心：
    1. 面向接口编程：	测试用例
    2. 面向HTML编程：对页面操作细节
六大原则：
    1. 用公共方法（功能点）代表一个页面（类）应当提供的服务（业务层面的，不是操作细节）
    2. 不要对外暴露，内部的操作细节（_转成私有）
    3. 不要再内部操作流程中添加断言
    4. 一个方法返回的是应该另外一个PO
    5. 不需要把所有的控件都写出来
    6. 正确和异常的case分开 return.self 或者return 详情页


api_object:
封装减少冗余代码，同时在后期维护中，若接口发生变化，只需要调整接口封装的代码，提高测试用例的可维护性、可读性。
    1. 将变与不变进行拆分，变的是测试数据，不变的是api
    2. 创建api层将接口进行单独封装，方便组合业务流程和接口测试
    3. 将接口公用的部分抽象出来 比如token , send发送请求 ，将方法写入base_api.py文件，管理api的文件取继承BaseApi
    4. 封装api的时候，依据接口文档将接口需要校验的参数进行参数化 好处：灵活的组装业务，进行业务流程测试，接口测试
"""
import requests


from faker import Faker

from api.base_api import BaseApi


class YuQing(BaseApi):
    _url = "http://123.56.138.96:3012/api/"

    # todo: 查看快讯
    def flash_news(self, page, pagesize):
        data = {
            "method": "post",
            "url": self._url + "ainews-espy/api/opinion/flash-news",
            "headers": {
                "Content-Type": "application/json;charset=UTF-8", "Authorization": self.wework
            },
            "json": {
                "start_time": "2021-10-20T17:14:25",
                "end_time": "2021-10-27T17:14:25",
                "page": page,
                "pagesize": pagesize
            }
        }
        return self.send(data)

    # todo: 查看行业新闻
    def article_list(self, article_type, risk_level):
        data = {
            "method": "post",
            "url": self._url + "ainews-espy/api/opinion/v2/article-list",
            "headers": {
                "Content-Type": "application/json;charset=UTF-8", "Authorization": self.wework
            },
            "json": {
                "sort_by": "pub_time",
                "sort_order": "desc",
                "page": 1,
                "board": "all",
                "classification": "",
                "category_key": "",
                "cp_type": "all",
                "article_type": article_type,
                "risk_level": risk_level,
                "start_time": "2021-10-24T00:00:00",
                "end_time": "2021-10-30T16:23:05"
            }
        }
        return self.send(data)

    # todo: 在公司分组里创建一个分组
    def create(self):
        data = {
            "method": "post",
            "url": self._url + "ainews-user/company-group/create",
            "headers": {
                "Content-Type": "application/json;charset=UTF-8", "Authorization": self.wework
            },
            "json": {
                "name": "阿里77"
            }
        }

        return self.send(data)

    def delete(self, id):
        data = {
            "method": "get",
            "url": self._url + "ainews-user/company-group/delete",
            "params": {"id": id},
            "headers": {
                "Content-Type": "application/json;charset=UTF-8",
                "Authorization": self.wework
            }
        }
        return self.send(data)


if __name__ == '__main__':
    a = YuQing()
    b = a.create().json().get("id")
    print(b)
    print(a.delete(b))
