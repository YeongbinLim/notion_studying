import { Client } from "@notionhq/client"

let NOTION_KEY='secret_rvjCuo98mFYnC8EO3Tv1dvOo7KY5X0hA4kvxBm0kkWB';
let NOTION_DATABASE_ID='748d95aefa5c4f86bfefd1bff152f701';
const notion = new Client({ auth: NOTION_KEY });

(async () => {
  const databaseId = '748d95aefa5c4f86bfefd1bff152f701';
  const response = await notion.databases.retrieve({ database_id: databaseId });
  console.log(response);
})();