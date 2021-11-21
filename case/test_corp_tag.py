import pytest

from WeWork.api.api_corp_tag import CorpTap
from WeWork.case.tools.crop_tag import get_corp_tag_id


class TestCorpTap:
    def setup_class(self):
        self.corptap = CorpTap()

    @pytest.mark.parametrize('data,check', [
        [{"group_id": ["et-QOqCQAATtUZKcXdXCv7bKtoGuVZTg"]}, ("errcode", "errmsg")],
        [{"tag_id": ["et-QOqCQAA3DP3yocdyRxIg5SbxOW9ZQ"]}, ("errcode", "errmsg")],
    ], ids=['group_id', 'tag_id'])
    def test_get_corp_tag_list(self, data, check):
        r = self.corptap.get_corp_tag_list(**data)
        # print(self.corptap.parser(r.json()))
        assert set(check).issubset(self.corptap.parser(r.json()))
        # assert r.status_code == 200
        # assert r.json()["errcode"] == check

    @pytest.mark.smoke
    @pytest.mark.parametrize('id,name,check', [
        ["et-QOqCQAA3DP3yocdyRxIg5SbxOW9ZQ", "xxx", 0],
        ["et-QOqCQAA3DP3yocdyRxIg5SbxOW9ZQ", "@#$", 0],
        ["et-QOqCQAA3DP3yocdyRxIg5SbxOW9ZQ", "999", 0],
        ["et-QOqCQAA3DP3yocdyRxIg5SbxOW9ZQ", "SSS", 0],
        ["et-QOqCQAA3DP3yocdyRxIg5SbxOW9ZQ", "老张", 0],
    ], ids=["英文", "字符", "数字", "大写英文", "中文"])
    def test_edit_corp_tag(self, id, name, check):
        r = self.corptap.edit_corp_tag(id, name)
        assert r.status_code == 200
        assert r.json()["errcode"] == check

    @pytest.mark.smoke
    @pytest.mark.parametrize('id,name,check', [
        [{"group_name": "老张标签组"}, "小王八", 0],
        [{"group_id": "et-QOqCQAATtUZKcXdXCv7bKtoGuVZTg"}, "大王八", 0]
    ], ids=["group_name", "group_id"])
    def test_add_corp_tag(self, name, check, id):
        r = self.corptap.add_corp_tag(name, **id)
        assert r.status_code == 200
        assert r.json()["errcode"] == check

    @pytest.mark.parametrize('id_path,check', [
        ["$..[?(@.name=='小王八')]", 0],
        ["$..[?(@.name=='大王八')]", 0]
    ], ids=['group_id', 'tag_id'])
    def test_del_corp_tag(self, id_path, check):
        id = {'tag_id': get_corp_tag_id(id_path)}
        r = self.corptap.del_corp_tag(**id)
        assert r.status_code == 200
        assert r.json()["errcode"] == check

    # @pytest.mark.smoke
    # def test_corp_tag_all(self):
    #     r = self.corptap.add_corp_tag()
    #     id=jsonpath(r.json())
    #     r = self.corptap.get_corp_tag_list(id)
    #     assert r.status_code == 200
    #     r = self.corptap.edit_corp_tag()
    #     assert r.status_code == 200
    #     self.corptap.del_corp_tag()
    #     assert r.status_code == 200
