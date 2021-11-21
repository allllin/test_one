"""
了解企业微信
1. 调通企业微信接口
2. 使用pytest编写几个测试用例
问题：代码冗余 可读性 可维护性差
"""

import requests
# todo: 编写接口测试用例
from jsonpath import jsonpath


def test_gettoken():
    # corpid = "ww9d7346c103e1fee0"
    # corpsecret = "NhSVPKpb-LXqe8FgepvNa0VOMVeuK7a7l-vvFhgrSYE"
    # r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?"
    #                  "corpid=ww9d7346c103e1fee0&corpsecret=NhSVPKpb-LXqe8FgepvNa0VOMVeuK7a7l-vvFhgrSYE")
    # print(r.json())
    data = {
        "method": "get",
        "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        "params": {
            "corpid": "ww9d7346c103e1fee0",
            "corpsecret": "NhSVPKpb-LXqe8FgepvNa0VOMVeuK7a7l-vvFhgrSYE"
        }
    }
    r = requests.request(**data)
    # print(json.dumps(r.json(), indent=2, ensure_ascii=False))
    token = r.json()["access_token"]
    assert r.status_code == 200
    return token


class TestCorpTag:
    def test_get_corp_tag_list(self):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            "params": {"access_token": test_gettoken()},
            "json": {"group_id": ["et-QOqCQAAFlHsl-5IhobqE27ZWbRR4w"], }
        }
        r = requests.request(**data)
        # print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        print(jsonpath(r.json(), "$..[?({})]".format("@.name=='sccc'"))[0])
        print(jsonpath(r.json(), "$..{}".format('name'))[0])
        # print(jsonpath(r.json(), "$..[?(@.name=='sofa')]")[0]['id'])
        # print(jsonpath(r.json(), "$..[?(@.name=='demo3')]")[0])

    @staticmethod
    def jsonpath(json_data, name):
        return jsonpath(json_data, "$..[?({})]".format(name))[0]
