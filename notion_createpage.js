
import { Client } from "@notionhq/client"


let NOTION_KEY='secret_rvjCuo98mFYnC8EO3Tv1dvOo7KY5X0hA4kvxBm0kkWB';
let NOTION_DATABASE_ID='748d95aefa5c4f86bfefd1bff152f701';
const notion = new Client({ auth: NOTION_KEY });



(async () => {
  const response = await notion.pages.create({
    parent: {
      database_id: '748d95aefa5c4f86bfefd1bff152f701',
    },
    properties: {
      title: {
        type: 'title',
        title: [
          {
            type: 'text',
            text: {
              content: 'Tomatoes',
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
      Price: {
        type: 'number',
        number: 1.49,
      },
      'Last ordered': {
        type: 'date',
        date: {
          start: '2021-05-11',
        },
      },
    },
  });
  console.log(response);
})();