import { Client } from "@notionhq/client"
 
let NOTION_KEY='secret_rvjCuo98mFYnC8EO3Tv1dvOo7KY5X0hA4kvxBm0kkWB';
let NOTION_DATABASE_ID='748d95aefa5c4f86bfefd1bff152f701';
const notion = new Client({ auth: NOTION_KEY });

(async () => {
    
  const pageId = '67a3dddc022f4b219c4dfd2fb79b0bf4';
  const response = await notion.pages.retrieve({ page_id: pageId });
  console.log(response);
})(); 


2.1.1- 이미지와 영상 데이터를 다루는 컴퓨터비전 분야의 전문가가 되고 싶다면 꼭 알아야 하는 
이론을 학습합니다. 
2.1.2- 인식 분야에서 가장 중요한 Task인 Object Detection과 Segmentation을 실내, 실외 
데이터로 나누어 총 4개의 프로젝트를 진행해봅니다.
2.1.3- 생성 분야에서는 최근에 가장 주요하게 떠오르는 NeRF 기반 모델을 4개 다뤄봅니다.
2.1.4- Pytorch 기반 딥러닝 모델을 경량화해서 Android, iOS 환경에 올리기 위한 과정을 
실습해봅니다.
2.1.5- 비전과 다른 기술, 데이터를 결합해서 학습하는 멀티모달 비전 프로젝트 다룹니다. 