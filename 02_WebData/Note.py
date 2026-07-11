import requests
import folium

url='https://dapi.kakao.com/v2/local/search/keyword.json'
headers= {'Authorization':'kakaoAK 키입력하기'}
params= {'query':'스타벅스', 'x':'126.9296', 'y':'37.48422', 'radius':15000, 'sort':'distance'}

response= requests.get(url, headers=headers, params=params)
response_dict= response.json()
items= response_dict.get('documents', [])

center= [37.5500, 126.9900]
my_map= folium.Map(location=center, zoom_start=14, zoom_control=True)
for item in items:
    place_name= item['place_name']
    road_address= item['road_address_name'] if item['road_address_name'] else item['address_name']
    phone= item['phone'] if item['phone'] else '전화번호 없음.'
    place_url= item['place_url']

    lat, lng= float(item['y']), float(item['x'])

    cat_group, cat_full= item.get('category_group_name',''), item.get('category_name','')
    marker_color, marker_icon= 'blue', 'info-sign'

    if '카페' in cat_full or cat_group == '카페':
        marker_color, marker_icon= 'darkgreen', 'coffee'
    elif '음식점' in cat_full or cat_group == '음식점':
        marker_color, marker_icon= 'orange', 'cutlery'
    elif '지하철역' in cat_full:
        marker_color, marker_icon= 'purple', 'subway'

    
