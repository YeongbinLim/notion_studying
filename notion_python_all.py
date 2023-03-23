import requests, json

token = 'secret_rvjCuo98mFYnC8EO3Tv1dvOo7KY5X0hA4kvxBm0kkWB'

databaseId = '748d95aefa5c4f86bfefd1bff152f701'

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def readDatabase(databaseId, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"

    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()
    print(res.status_code)
    # print(res.text)

    with open('./db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)


def createPage(databaseId, headers, data):

    createUrl = 'https://api.notion.com/v1/pages'
 
    newPageData = {
        "parent": { "database_id": databaseId },
        "properties": {
        "title": {
            "type": 'title',
            "title": [
            {
                "type": 'text',
                "text": {
                "content": 'Tomatoes',
                },
            },
            ],
        },
        
            "xx": {
                "multi_select": [
                {
                    "name": "xcv"
                }            
                ]
            },
        "Price": {
            "type": 'number',
            "number": 1.59,
        },
        'Last ordered': {
            "type": 'date',
            "date": {
            "start": '2021-05-11',
            },
        },
        },
    }
     
    data = json.dumps(newPageData)
    # print(str(uploadData))

    res = requests.request("POST", createUrl, headers=headers, data=data)

    print(res.status_code)
    print(res.text)        

def updatePage(padeId, headers):
    updateUrl = f"https://api.notion.com/v1/pages/{pageId}"
 
    updateData = {
        "properties": {
            "Value": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Pretty Good"
                        } 
                    }
                ]
            }        
        } 
    }

    data = json.dumps(updateData)

    response = requests.request("PATCH", updateUrl, headers=headers, data=data)

    print(response.status_code)
    print(response.text)

createPage(databaseId, headers)