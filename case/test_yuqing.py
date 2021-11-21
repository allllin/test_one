import pytest

from api.api_yuqing import YuQing


class TestYuQing:
    def setup_class(self):
        self.yuqing = YuQing()

    @pytest.mark.parametrize('page,pagesize,check', [
        (1, 10, True)
    ], ids=["flash_news"])
    def test_flash_news(self, page, pagesize, check):
        r = self.yuqing.flash_news(page, pagesize)
        assert r.json().get('ok') == check

    @pytest.mark.parametrize('article_type,risk_level,check', [
        ("risk_items", [0], 200),
        ("notice", [1], 200),
        ("news", [2], 200),
        ("all", [0, 1], 200)
    ], ids=["article_list001", "article_list002", "article_list003", "article_list004"])
    def test_article_list(self, article_type, risk_level, check):
        r = self.yuqing.article_list(article_type, risk_level)
        assert r.status_code == check

    def test_delete(self):
        a = self.yuqing.create()
        id = a.json().get("id")
        r = self.yuqing.delete(id)
        assert r.status_code == 400

    def test_create(self):
        r = self.yuqing.create()
        assert r.status_code == 400
