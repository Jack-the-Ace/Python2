import requests
import folium

# 1. 카카오 로컬 검색 API 설정
url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
headers = {'Authorization': 'KakaoAK d50fc61dbf1c193a3081e1faeb17c2b4'}

# 0번 과제 반영: 중심 좌표 설정 (x: 경도, y: 위도)
center_x, center_y = '126.9296', '37.48422'  # 신림역 부근 좌표
params = {
    'query': '스타벅스', 
    'x': center_x, 
    'y': center_y, 
    'radius': '15000', 
    'sort': 'distance'
}

# API 요청 및 데이터 변환
response = requests.get(url, headers=headers, params=params)
response_dict = response.json()
items = response_dict.get('documents', [])

# 0. 중심좌표를 이용하여 지도 생성 (위도, 경도 순서 주의)
center_location = [float(center_y), float(center_x)]
my_map = folium.Map(location=center_location, zoom_start=14, zoom_control=True)

# 1~5. 장소 데이터를 순회하며 마커 표시
for item in items:
    # 데이터 추출
    place_name = item['place_name']
    road_address = item['road_address_name'] if item['road_address_name'] else item['address_name']
    phone = item['phone'] if item['phone'] else '전화번호 없음'
    place_url = item['place_url']
    
    # 1. 위도(y), 경도(x) 변환
    lat = float(item['y'])
    lng = float(item['x'])
    
    # 5. 장소별 카테고리 구분에 따른 마커 색상 및 아이콘 설정
    # 카카오 API의 대분류 카테고리(category_group_name) 혹은 전체 카테고리명 기반 판별
    cat_group = item.get('category_group_name', '')
    cat_full = item.get('category_name', '')
    
    # 기본값 (기타 장소)
    marker_color = 'blue'
    marker_icon = 'info-sign'
    
    if '카페' in cat_full or cat_group == '카페':
        marker_color = 'darkgreen'  # 스타벅스 등 카페는 초록색
        marker_icon = 'coffee'      # fontawesome 아이콘
    elif '음식점' in cat_full or cat_group == '음식점':
        marker_color = 'orange'
        marker_icon = 'cutlery'
    elif '지하철역' in cat_full:
        marker_color = 'purple'
        marker_icon = 'subway'
        
    icon = folium.Icon(color=marker_color, icon=marker_icon, prefix='fa') # fontawesome 사용을 위해 prefix='fa' 지정
    
    # 2. 마커 툴팁 설정 [상호명(장소명)]
    tooltip_content = f"<b>{place_name}</b>"
    
    # 3~4. 마커 팝업 설정 [주소, 전화번호, 클릭 시 새탭으로 상세페이지 url 이동]
    # 가로 크기가 깨지지 않게 html과 folium.IFrame 구조 사용
    html_content = f"""
    <div style="font-family: 'Malgun Gothic', sans-serif; font-size: 12px; width: 220px;">
        <h4 style="margin: 0 0 5px 0; color: #333;">{place_name}</h4>
        <p style="margin: 3px 0;"><b>주소:</b> {road_address}</p>
        <p style="margin: 3px 0;"><b>전화:</b> {phone}</p>
        <hr style="margin: 8px 0; border: 0; border-top: 1px solid #ccc;">
        <a href="{place_url}" target="_blank" style="display: inline-block; color: white; background-color: #2db400; padding: 4px 8px; text-decoration: none; border-radius: 4px; font-weight: bold;">상세정보 보기 (새탭)</a>
    </div>
    """
    iframe = folium.IFrame(html_content, width=240, height=140)
    popup_content = folium.Popup(iframe, max_width=300)
    
    # 지도에 마커 추가
    folium.Marker(
        location=[lat, lng],
        tooltip=tooltip_content,
        popup=popup_content,
        icon=icon
    ).add_to(my_map)

# 결과 확인 및 저장
my_map.show_in_browser()
# my_map.save('./saved/kakao_search_map.html')  # 폴더가 존재할 경우 주석 해제 후 저장 가능