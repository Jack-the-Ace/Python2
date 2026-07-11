# Google AI Studio 에서 제공하는 LLM 생성형 API 활용
# https://aistudio.google.com

# 가격정책 확인 : 무료로 사용가능한 모델들이 일부 존재함. [실습활용]

# 개발가이드 문서를 참고하여 개발(업데이트 자주되니, 주기적으로 확인!)
# 1. 키 발급.

# 2. google genai 모듈 설치
# pip install -q -U google-genai

# 3. 모듈 사용
from google import genai

# 4. LLM 사용을 요청하는 객체 생성
client=genai.Client(api_key='키입력하기')

#8. 모델이 응답할때 참고(사용)할 도구 중 함수..
#1) 대한민국 대통령의 정보를 리턴해주는 함수 (ai model이 답변을 할때 사용할 함수를 결정할때 doc string을 참고)
def get_president_korea():
    """
    이 함수는 대한민국 대통령에 대한 질문에 답변하기 위해 사용됩니다.
    """
    
    #실제로는 이 데이터를 네이버 검색. 뉴스검색 api를 이용하여 가져와서 반환
    return "이재명"

# 오늘의 날씨 정보를 알려주는 기능함수
def get_weather():
    #기상청 open api를 통해 날씨 데이터를 가져오기
    import requests
    weather= requests.get('기상청 open api.json')
    return weather


# 7. 모델이 답변하는 내용을 조정하는 설정객체 생성
from google.genai import types
config= types.GenerateContentConfig(
    max_output_tokens=1500,  #생성될 응답의 최대 토큰수를 제한합니다.
    #temperature=2.0,        #생성된 응답의 무작위성을 제어함. 창의력을 조절(0~2.0) 기본 1.0.. 온도가 높을수록 열정적인 모델. 창의적
    #temperature=0,          #냉소적... 창의성 결여.
    #top_p=0.5,              #모델이 다음 토큰을 선택할 때 고려하는 후보군의 확률 총합이 0.5가 되면 후보 선정 완료 [일관성 있는 답변을 유도할때 많이 사용]
    response_mime_type='text/plain',
    #response_mime_type='application/json',
    #seed=42,                 #후보군들 중에서 랜덤하게 선택될때..랜덤값을 일관되게 생성- 매번 같은 응답(숫자는 아무 숫자나)

    #시스템에게 응답 지침을 미리 설정
    #system_instruction='너는 고양이야. 이름은 네코네코야.',
    system_instruction='너는 교양있는 30대의 아름다운 대한민국 언어학 교수(박사)님이야. 말을 정말 예쁘게 하는 사람이지.',
    # 미리 학습한 것 외에도 답변하도록 하기 위해 모델에게 추가 도구를 주기!
    tools=[get_president_korea, get_weather],
)

# 5. 요청하기
response= client.models.generate_content(
    model='gemini-3.5-flash',  #실습은 무료등급이 지원되는 모델 중 선택. 무료사용량을 소진하면 모델 변경
    #model='gemini-3-flash-preview',
    #model='gemini-3.5-live-translate-preview',
    #contents="너는 구글의 제미나이야? 아니면, ChatGPT야?",  #사용자의 프롬프트(질문)
    contents="잘 지내보자, 화이팅하자!",
    #답변을 조정하는 설정 (설정객체를 통해 지정)
    config=config,
)

# 6. 응답결과 출력
#print(response)  # token 사용내역 등. 메타데이터와 응답글씨를 가지고 있음.
print(response.text)



