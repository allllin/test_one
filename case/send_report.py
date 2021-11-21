import datetime
import json

import requests


class DingRobot:
    def __init__(self):
        self.allure = "http://lzw:lzw000216@39.105.54.35:9000/job/yuqing/allure/widgets/suites.json"
        self.ding = "https://oapi.dingtalk.com/robot/send?access_token=" \
                    "d329c58edcb83de4ee3b10d6824f369217aa42688a32a17cf298e90d9e1ec5cf"
        self.error = self.get_allure()

    def get_allure(self):
        jenkins_data = requests.get(self.allure).json()
        case_error = jenkins_data["items"][0]["statistic"]["failed"]
        return case_error

    def send_report(self):
        if self.error > 0:
            headers = {"Content-Type": "application/json;charset=utf-8"}
            content = {
                "msgtype": "link",
                "link": {
                    "text": "账号lzw,密码lzw000216",
                    "title": "小林同学" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "picUrl": "",
                    "messageUrl": "http://lzw:lzw000216@39.105.54.35:9000/job/yuqing/allure/"
                }
            }
            requests.post(self.ding, headers=headers, data=json.dumps(content))
        else:
            print('无报错')


if __name__ == '__main__':
    # DingRobot().send_report()
    print(DingRobot().get_allure())
