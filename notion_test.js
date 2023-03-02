
import { Client } from "@notionhq/client"
let NOTION_KEY='secret_rvjCuo98mFYnC8EO3Tv1dvOo7KY5X0hA4kvxBm0kkWB';
let NOTION_DATABASE_ID='748d95aefa5c4f86bfefd1bff152f701';
const notion = new Client({ auth: NOTION_KEY })

const databaseId = NOTION_DATABASE_ID

async function addItem(text1,text2) {
  try {
    const response = await notion.pages.create({
      parent: { database_id: databaseId },
      properties: {
        title: {
          title:[
            {
              "text": {
                "content": text1
              }
            }                            
          ]
        },
        
        "Date": {
          "date": {
          "start": "2022-06-06"
            }
          },
        "xx": {
          "multi_select": {
              "options": [
                {
                  name: "xcv"
                }
              ]
            }
          },
        
      },
    })
    console.log(response)
    console.log("Success! Entry added.")
  } catch (error) {
    console.error(error.body)
  }
}
addItem("TEScccT")


// curl --location --request PATCH 'https://api.notion.com/v1/databases/668d797c-76fa-4934-9b05-ad288df2d136' \
// --header 'Authorization: Bearer '"$NOTION_API_KEY"'' \
// --header 'Content-Type: application/json' \
// --header 'Notion-Version: 2022-06-28' \
// --data '{
//     "title": [
//         {
//             "text": {
//                 "content": "Today'\''s grocery list"
//             }
//         }
//     ],
//     "description": [
//         {
//             "text": {
//                 "content": "Grocery list for just kale 🥬"
//             }
//         }
//     ],
//     "properties": {
//         "+1": null,
//         "Photo": {
//             "url": {}
//         },
//         "Store availability": {
//             "multi_select": {
//                 "options": [
//                     {
//                         "name": "Duc Loi Market"
//                     },
//                     {
//                         "name": "Rainbow Grocery"
//                     },
//                     {
//                         "name": "Gus'\''s Community Market"
//                     },
//                     {
//                         "name": "The Good Life Grocery",
//                         "color": "orange"
//                     }
//                 ]
//             }
//         }
//     }       
// }'