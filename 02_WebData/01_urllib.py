#표쥰모듈로 웹데이터를 가져오기 실습

# 실습을 위해 webdata폴더의 파일들을 dothome 서버에 업로드

# 네트워크 작업을 수행하는 표준모듈 사용
from urllib import request  # HTTP Request 작업을 수행

#1] 일반 텍스트 파일 읽기
address= 'https://mbca2026aix.dothome.co.kr/webdata/aaa.txt'
url= request.urlopen(address)
data= url.read()
print(data)  # 한글 깨짐
print('------------------------------------------------------------------------------------------------------------')
print(data.decode('UTF-8'))
print()

#2] GET 방식으로 서버에 데이터를 전송하고 응답 받기
#보낼 데이터를 dict 타입으로 준비
data= {'title':'안녕하세요', 'msg':'반가워요'}
#dict 타입을 URL의 key=value 형태로 변환
from urllib import parse
encoded_data= parse.urlencode(data).encode('utf-8')
#print(encoded_data)
address= 'https://mbca2026aix.dothome.co.kr/webdata/bbb.php?' + str(encoded_data)
url = request.urlopen(address)
response= url.read()
print(response.decode('UTF-8'))
print()

#3] POST로 보내고 응답 받기
url= 'https://mbca2026aix.dothome.co.kr/webdata/ccc.php'
req= request.Request(url, data=encoded_data, method='POST')
#요청 보내고 받는 작업을 예외처리까지 해서..
import urllib.error
try:
    with request.urlopen(req) as response:
        response_body= response.read().decode('utf-8')
        print(f'Status: {response.status}') # 200, 403, 404
        print(f'body: {response_body}')  # 응답 데이터
except urllib.error.URLError as e:
    print(f'Error: {e}')

# 표준모듈을 사용하면.. 인코딩. 예외처리. 등 해야 할 작업이 많아. 코드가 불편함.
# 실무에서는 이를 편하게 해주는 requests 외부모듈을 선호함.

# 단, 표준모듈 urllib는 웹파일을 다운로드 할 때 여전히 많이 사용됨
url= 'https://mbca2026aix.dothome.co.kr/webdata/aaa.txt'
request.urlretrieve(url, './download/aaa.txt')


