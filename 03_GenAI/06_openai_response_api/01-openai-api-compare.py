# openai 의 3가지 api 비교

#0. api key load
from dotenv import load_dotenv
load_dotenv()

#1. Completions API : 가장 초기 방식. 사용자입력과 지침을 구별하지 않고 입력
from openai import OpenAI
client= OpenAI()

completion= client.completions.create(
    model='gpt-3.5-turbo-instruct',
    prompt='너는 인공지능 전문가야. 인공지능의 미래에 대해 간략히 설명해주세요.',
    temperature=0.7,
    max_tokens=150,
)
print(completion.choices[0].text.strip())
print('='*100)
print()

#2. Chat Completions API : 표준 인터페이스
# 특징: 메시지별 역할을 구분하는 개념이 등장. ("system","user","assistant")

completion= client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {'role':'system','content':'당신은 AI 전문가입니다.'},
        {'role':'user','content':'머신러닝과 딥러닝의 차이점을 설명해주세요.'}
    ],
    temperature=0.7,
    max_completion_tokens=200,
)
print(completion.choices[0].message.content)
print('='*100)
print()

#3. response API : 차세대 에이전트형 인터페이스 - 2025년에 등장
# 대화상태를 유지하는 기능도 포함. 외부 도구와 연결이 용이.

# 첫번째 요청
response1= client.responses.create(
    model='gpt-4o-mini',
    instructions='너는 한국어 AI 전문가입니다.',
    input='최근 인공지능 기술 트렌드를 알려줘.',
    tools=[{'type':'web_search'}]   #웹검색도구 활성화
)
print(response1.output_text)
print('~'*100)

response2= client.responses.create(
    model='gpt-4o-mini',
    instructions='너는 한국어 AI 전문가입니다.',
    input='이 중에서 가장 주목받는 기술은 무엇이야?',
    #이전 응답기록을 인식하도록.. 이전 응답의 식별아이디를 지정
    previous_response_id=response1.id
)
print(response2.output_text)



























