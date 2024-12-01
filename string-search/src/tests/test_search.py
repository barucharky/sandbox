
from ..search import Search

def test_get_strings() -> None:
    get_string = Search()
    assert type(get_string.search_string) == str

def test_get_keyword() -> None:
    get_keyword = Search()
    assert type(get_keyword.keyword) == str

def test_search_string() ->None:
    s = Search()
    success = s.do_search(s.search_string, s.keyword)
    assert success == True
