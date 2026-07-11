# 데이터를 수집하는 가장 안전한 방법은 각 기관/업체에서 제공하는 Open API 를 사용
# 대표적인 Open API : 공공데이터포털, 카카오 API, 네이버 API, ...

#[1] 공공데이터 포털 : data.go.kr [제주도 심야약국 정보 xml 수집]
import requests

#심야약국 리스트 open api end-point url : ?뒤의 파라미터를 제외한 url
url='http://data.jeju.go.kr/rest/nightpharmacy/getNightPharmacyList'

# 서비스키를 포함한 파라미터 dict
params= {
    'serviceKey':'a2ea8f430c59a9feb8e5429a2e46e5e3f6ecd44cb82cfb422fbe19b3dc251b61',
    'pageSize':10,
    'startPage':1
}

# url과 param를 get방식으로 요청
response= requests.get(url, params=params)
#print(response.text)  # xml 형식의 문자열

# xml 문자열을 분석하여 특정요소들의 값들만 추출
import xml.etree.ElementTree as ET
root= ET.fromstring(response.text)

#약국 정보들을 가진 요소들 찾기
pharmacy_datas= root.find('body').find('data').findall('list')

# 약국 정보들 중에서 원하는 데이터만 추출
pharmacy_list=[]
for pharmacy in pharmacy_datas:
    name= pharmacy.find('dataTitle').text
    address= pharmacy.find('adres').text
    tel= pharmacy.find('telNo').text
    latitude= pharmacy.find('la').text
    longitude= pharmacy.find('lo').text

    # 약국 1개의 정보를 dict로 만들어서 리스트에 추가
    pharmacy_list.append({'name':name, 'address':address, 'tel':tel, 'geolocation':[latitude, longitude]})


#출력
for pharmacy in pharmacy_list:
    print(pharmacy)  # dict 데이터들 출력

# 이 정보를 기반으로 지도에 표시하거나 데이터 분석에 사용.



