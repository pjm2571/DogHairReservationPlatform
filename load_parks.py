import json

import requests

# Geocoding !! --> 주소값을 Coordinate로 바꿔줌
def geocode(address):
    url = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode'
    headers = {
        'X-NCP-APIGW-API-KEY-ID': 'zo6ogrtxyl', # client id
        'X-NCP-APIGW-API-KEY': 'fcGoiK9GYRM3Kl6rMTlLWd6hXuvjBSJFMeaObSsp' # client secret
    }

    params = {
        'query': address,
        'coordType': 'latlng'
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()

        if data['status'] == 'OK':
            coordinate = data['addresses'][0]['x'], data['addresses'][0]['y']
            return coordinate
    return None


# csv -> json 파일로 변환된 것을 장고 템플릿을 이용해서 데이터베이스에 적용
if __name__ == "__main__":

    with open('park_json_gs.json', 'rt', encoding='UTF8') as f:
        park_list = json.load(f)


    new_list = []
    for park in park_list:
        new_data = {"model": "parkmap.Park"}

        location = geocode(park['location'])
        park['latitude'] = location[0]
        park['longitude'] = location[1]
        new_data["fields"] = park

        new_list.append(new_data)

    with open('park_data_gs.json', 'w', encoding='UTF-8') as f:
        json.dump(new_list, f, ensure_ascii=False, indent=2)
