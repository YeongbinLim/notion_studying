from datetime import datetime
from notion.client import NotionClient
from notion.block import PageBlock, TextBlock, TodoBlock
from notion.block import CollectionViewBlock

_MY_TOKEN = 'f9e5296a0aba8da7600927e112d606bde031b41afc4810c6524d16a01a749c06bf29ca50e0bc258a3540b4737d34ff43d5b1bf7689ea05adc9bc82285c2c4604da4926dd462e745ccf60a2d2928c'
_PAGE_URL = 'https://www.notion.so/page_create-0436a591c2d84ba9bca1081f196d71ce?pvs=4'


def get_schema_todo():
    return {
        # title 항상 존재 해야한다
        "title": {"name": "내용", "type": "title"},
        "complete": {"name": "체크박스", "type": "checkbox"},
        "priority": {"name": "셀릭트박스", "type": "select",
            "options": [
                {
                    "color": "red",
                    "id": "502c7016-ac57-413a-90a6-64afadfb0c44",
                    "value": "사과",
                },
                {
                    "color": "yellow",
                    "id": "59560dab-c776-43d1-9420-27f4011fcaec",
                    "value": "오렌지",
                },
                {
                    "color": "green",
                    "id": "57f431ab-aeb2-48c2-9e40-3a630fb86a5b",
                    "value": "수박",
                }
            ]
        }
    }


if __name__ == '__main__':
    client = NotionClient(token_v2=_MY_TOKEN)
    page = client.get_block(_PAGE_URL)

    child = page.children.add_new(CollectionViewBlock)
    print(child)
    print(page)
    child.collection = client.get_collection(
        client.create_record(
            "collection", parent=child, schema=get_schema_todo())
        )
    child.title = '생성한 테이블2'
    child.views.add_new(view_type="table")

    row = child.collection.add_row()
    # row.set_property('title', '추가된 아이템')
    # row.set_property('체크박스', True)
    # row.set_property('셀릭트박스', '사과')