import json

import requests

# csv -> json 파일로 변환된 것을 장고 템플릿을 이용해서 데이터베이스에 적용
if __name__ == "__main__":

    with open('doglist_json.json', 'rt', encoding='UTF8') as f:
        dog_list = json.load(f)


    new_list = []
    for dog in dog_list:
        new_data = {"model": "doglist.Dog"}

        new_data["fields"] = dog

        new_list.append(new_data)

    with open('store_doglist.json', 'w', encoding='UTF-8') as f:
        json.dump(new_list, f, ensure_ascii=False, indent=2)
