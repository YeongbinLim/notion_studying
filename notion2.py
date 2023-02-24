from notion.client import NotionClient

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
client = NotionClient(token_v2="f9e5296a0aba8da7600927e112d606bde031b41afc4810c6524d16a01a749c06bf29ca50e0bc258a3540b4737d34ff43d5b1bf7689ea05adc9bc82285c2c4604da4926dd462e745ccf60a2d2928c")

# Replace this URL with the URL of the page you want to edit
page = client.get_block("https://www.notion.so/page_create-0436a591c2d84ba9bca1081f196d71ce?pvs=4")

print("The old title is:", page.title)

row = page.children._content_list
print(row)
collect =client.get_collection("17c05e25-a174-488b-b41c-765cebd5782f")
print(collect)
row=collect.add_row()
row.set_property('title', '추가된 아이템')
