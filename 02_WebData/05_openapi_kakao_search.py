# 공공데이터 외에도 많은 정보를 가진 디지털기업도 자사의 정보를 활용하여
# 사용자에게 유용한 애플리케이션을 제작할 수 있도록 OPEN API 를 제공하고 있음.

# kakao, naver 의 apikey 방식이 달라 각각 실습으로 경험해보기

# 카카오의 [로컬검색 API : 특정키워드를 주면 해당 키워드에 해당하는 장소들에 대한 정보(상호, 위도, 경도, 소개페이지url)를 json으로 제공해주는 api]
# 카카오 개발자 사이트. 가이드 문서 확인. 키 발급(REST API KEY)
import requests

# end point url
url= 'https://dapi.kakao.com/v2/local/search/keyword.json'

# 인증키는 url이 아닌. header 에 넣어서 전송함 (REST API KEY)
headers= {'Authorization':'KakaoAK 키입력하기'}

# 요청 파라미터들
params= {'query':'스타벅스', 'x':'126.9296', 'y':'37.48422', 'radius':'15000', 'sort':'distance'}

# 요청과 응답
response= requests.get(url, headers=headers, params=params)
#print(response.text)

# json 형식은 응답문자열에서 원하는 정보를 추출
response_dict= response.json()  # json --> dict
items= response_dict['documents']

for item in items:
    print('장소명:', item['place_name'])
    print('주소:', item['road_address_name'])
    print('전화번호:', item['phone'])
    print('위도, 경도:', item['y'],", ",item['x'])
    print('상세정보페이지 url:', item['place_url'])
    print("="*100)
    print()

# 이 정보들을 지도로 보여주기
# 파이썬 지도 모듈 folium [이쁘지 않아요. 실무에서는 웹으로 데이터를 보내고 이를 지도로 보여줌]
# 데이터분석용으로 특정지역 상점밀집도, 유동인구 분포 등을 시각적으로 간단하게 시각화해야 할때 사용

# 파이썬 지도 모듈 실습 [06_map_folium.py]

#[수행과제] 위 정보들을 지도에 표시하기
#0. kakao search api에 요청했던 중심좌표를 이용하여 지도를 보여주기
#1. 위 장소들의 위도,경도 정보를 이용하여 마커 표시
#2. 마커의 툴팁에는 [상호명(장소명)]이 표시
#3. 마커의 팝업에는 [주소, 전화번호]가 표시
#4. 각 마커의 팝업을 클릭하면 장소들의 [상세정보페이지url] 을 이용하여 새탭으로 정보 보여주기
#5. 장소별 카테고리 구분에 따라 마커의 색상과 아이콘을 다르게 표시

# (지도 시각화 사례 조사)
# 구글 이미지 검색 : '데이터분석 지도 시각화'

