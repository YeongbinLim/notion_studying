import { Client } from "@notionhq/client"

let NOTION_KEY='secret_rvjCuo98mFYnC8EO3Tv1dvOo7KY5X0hA4kvxBm0kkWB';
let NOTION_DATABASE_ID='748d95aefa5c4f86bfefd1bff152f701';
const notion = new Client({ auth: NOTION_KEY });

(async () => {
    
  const pageId = '67a3dddc022f4b219c4dfd2fb79b0bf4';
  const response = await notion.pages.retrieve({ page_id: pageId });
  console.log(response);
})();