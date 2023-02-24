import requests, json

def readDatabase(databaseId, headers):
    
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"

    res = requests.post(readUrl, headers=headers)
    print(res.status_code)

    data = res.json()
    with open("./db.json", "w", encoding="utf8") as f:
        json.dump(data, f, ensure_ascii=False)
        
token = "secret_rvjCuo98mFYnC8EO3Tv1dvOo7KY5X0hA4kvxBm0kkWB"

databaseId = "f02f28baffb6415cb362fe9e1d29f5c2"

headers = {
    "Authorization": "Bearer " + token,
    "Notion-Version": "2022-02-22"
}

readDatabase(databaseId, headers)