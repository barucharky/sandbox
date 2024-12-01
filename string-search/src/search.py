
from pydantic import BaseModel

class Search(BaseModel):
    search_string: str = "You may search for a word like dog within this string"
    keyword: str = "dog"

    def do_search(
            self,
            search_string: str,
            keyword: str
    ) -> bool:
        index = search_string.find(keyword)

        if type(index) == int:
            print(index)
            return True
        
        return False
    

s = Search()
print(s.search_string)
print(s.keyword)

s.do_search(s.search_string, s.keyword)