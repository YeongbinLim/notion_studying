from notion.client import NotionClient

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
client = NotionClient(token_v2="f9e5296a0aba8da7600927e112d606bde031b41afc4810c6524d16a01a749c06bf29ca50e0bc258a3540b4737d34ff43d5b1bf7689ea05adc9bc82285c2c4604da4926dd462e745ccf60a2d2928c")

# Replace this URL with the URL of the page you want to edit
page = client.get_block("https://www.notion.so/page_create-0436a591c2d84ba9bca1081f196d71ce?pvs=4")
# page = client.get_block("57572125-e2ce-489d-b34a-65293eff7a04")
print("The old title is:", page.title)

row = page.children._content_list
print(row)
collect =client.get_collection("17c05e25-a174-488b-b41c-765cebd5782f")
print(collect)

row=collect.add_row()
row.set_property('title','notion-py 사용하기')
row.set_property('제품군','SYS')
row.set_property('담당자','임영빈')
# row.set_property('등록일',"2023년 2월 20일" )
row.set_property('난이도',40)
row.set_property('status',"진행 중")
# row.set_property('완료예상일',"2023년 2월 27일")
row.set_property('분류',"SYSTEM")
row.set_property('효과', 500)
