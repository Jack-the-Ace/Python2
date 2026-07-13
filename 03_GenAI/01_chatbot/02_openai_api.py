# OPENAI 에서 제공하는 생성형 AI API

# openai api 플랫폼 사이트 [chatGPT와는 다른 서비스]
# api key 발급 및 유료결제를 통해 사용금액 충전(선불)
# [주의] api key는 처음 발급될때만 확인 가능함. 그러니 별도의 문서에 보관. 권장

#1. openai api를 사용하기 위한 모듈 설치
# pip install openai

#2. 모듈 사용
from openai import OpenAI

#3. openai의 생성형 AI에게 질문(prompt)을 하고 응답을 받아주는 객체 생성
#client= OpenAI(api_key='발급받은 key') -- 권장X
# 프로그램 코드에 api_key와 같은 개인정보가 노출되면 위험..
# 그래서 보통 git에서 관리하지 않는 환경변수로 저장함[환경변수를 저장하는 파일 .env (반드시 프로젝트의 root 폴더에 위치)]

# 환경변수 파일을 읽어오는 외부모듈 사용 pip install dotenv
from dotenv import load_dotenv
load_dotenv()

# OpenAI 객체를 만들때 별도의 api_key를 지정하지 않으면 환경변수 파일에서 "OPENAI_API_KEY"라는 이름의 변수를 찾아서 적용함
client= OpenAI()

#openai의 생성형 AI를 다루는 최신 response api [교재의 assistant api의 상용버전]
response= client.responses.create(
    model='gpt-4o-mini',
    #input='AI에 대해 간단하게 알려줘.',
    #input='대한민국의 지금 대통령은 누구인가?',
    input='오피스텔의 경우, 전용면적이 29.97제곱미터여도 임대주택사업자 등록증이 있어야 취등록세를 감면받을 수 있는가?',

    #챗봇의 응답지침 지정! ~ 프롬프트 엔지니어링 기법으로 나만의 챗봇으로 개발
    #instructions='넌 AI전문가야. 한글기준 100글자 이내로 모든 내용을 설명해',
    #instructions='너는 고양이 처럼 말해. 이름은 네코네코야.',
    #instructions='너는 불량고등학생이야. 비속어를 많이 사용해. 100글자 이내로 대답해.',
    #instructions='너는 모든 대답을 개조식으로 해. bullet 기호를 사용해',
    instructions='''
    너는 대한민국 부동산 시장과 법에 대해 모든걸 알고있는 박사님이야.

    답변할때 tools가 지정되어 있으면 우선 참고해서 답변해.
    ''',

    # 응답에 대한 설정
    max_output_tokens=10000,  # 토큰의 폭주를 막아줌. 최대 만토큰 이상 답변에 사용 못하도록
    temperature=0.8,    # 창의성(0.0~2.0).  온도가 높을수록 창의적! .default= 1.0
    top_p=1.0,          # 창의성에 관련(0.0~1.0). LLM이 다음단어(token)의 후보를 정할때.. 후보의 확률 총합이 1.0이 되면 그만... [후보군을 조절함으로서.. 일관된 답변을 유도할 수 있음.] - 온도설정과 같이 사용하지 않을 것을 권장.
    timeout=20,         # AI가 답변을 생성할때 20s가 넘어가면 정지!!

    #LLM이 답변할때 미리 학습된 내용 말고 참고할 도구(웹검색, 문서참고, 함수호출 등.)를 추가할 수 있음.
    tools=[
        {"type":"web_search"},  # 웹검색이 필요하면 검색을 수행하고.. 답변의 근거를 링크로 제시함.
    ],
    tool_choice= 'required',  #무조건 tools을 사용하여 답변. 검색이 필요없어도 발동하기에 주의해서 사용. default= auto.
    
)

# 응답결과 출력
#print(response)  # 메타데이터(사용토큰 등...) + 응답글씨 모두 출력
print("="*100)
print(response.output_text)




