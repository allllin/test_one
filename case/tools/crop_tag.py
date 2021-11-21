from jsonpath import jsonpath

from WeWork.api.api_corp_tag import CorpTap


def get_corp_tag_id(path):
    r = CorpTap().get_corp_tag_list()
    try:
        id = jsonpath(r.json(), path)[0]["id"]
        return id
    except:
        pass