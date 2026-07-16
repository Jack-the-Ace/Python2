# LLM은 이전 대화내용을 기억하지 못함. LLM에게 이전 대화의 history를 인식하도록 연결

#0. api key 적용
from dotenv import load_dotenv
load_dotenv()

#1. 필요한 모듈 import 및 openai 모델 생성
from langchain_openai import ChatOpenAI
model= ChatOpenAI(
    temperature=0.1,
    max_completion_tokens=5000,
    model='gpt-4o-mini',
)

#2. 랭체인 model에게 질문 및 응답
# question= '안드레이 카파시가 누구인지 설명해주세요.'
# response= model.invoke(question)
# print(response.content)

#3. 랭체인은 프롬프트를 조금 더 자세하고 규격화하여 작성하기 편하도록(프롬프트 엔지니어링과 연관) 프롬프트 템플릿을 만들어 적용할 수 있음. import 필요
from langchain_core.prompts import PromptTemplate
prompt_temple= "{who}가 누구인지 설명해주세요."
prompt= PromptTemplate(template=prompt_temple, input_variables=['who'])
#완성된 프롬프트 확인하기
# print(prompt.format(who='안드레이 카파시'))
# print(prompt.format(who='이순신 장군'))

# .format()으로 직접 프롬프트를 완성하고 요청하는 것도 짜증.
# 이 프롬프트 템플릿과 모델을 체인으로 연결하면.. 응답을 요청할때 알아서 템플릿을 참고하여
# 프롬프트를 완성한 후 응답해줌.

# chatbot_chain= prompt | model  # 파이프라인 처럼 연결됨  # | 연산자는 LCEL 언어임. 별도수업.
# response= chatbot_chain.invoke({'who':'제프리 힌튼'})
# print(response.content)
# print('-'*100)

# # 이전 대화를 기억하는지 확인
# response= chatbot_chain.invoke('그(그들)이 현재 어디에서 살고있나?')
# print(response.content)

# 이전 대화를 기억하도록 구현해보기 -- 템플릿에 이전 기록들이 표시되도록

# (이전까지의 대화기록 history)과 (현재 사용자의 질문 input)을 같이 알 수 있도록 프롬프트 템플릿 만들기
prompt_template='''
아래는 사람과 AI의 대화기록입니다. AI 이름은 MBCA 친구봇 입니다.
대화문맥을 바탕으로 친절하고 간결한 답변을 진행하세요.

현재 대화:
{history}

사람:{input}
AI:
'''
#프롬프트 완성 ~ 변수명 2개 지정
prompt= PromptTemplate(template=prompt_template, input_variables=['history','input'])

# 모델과 템플릿을 체인으로 연결
chatbot= prompt | model

# prompt의 {history}에 대화기록을 남기려면 메세지 단위로 관리해야함. 메세지 단위의 대화기록을 관리하는 클래스 ChatMessageHistory 임.
# 이 클래스를 사용하기 위해 langchain의 하위모듈 community를 설치  pip install langchain-community
from langchain_community.chat_message_histories import ChatMessageHistory

# 단, 이 앱을 사용하는 사용자가 여러명이면 chatbot이 어떤 사용자의 대화기록인지 구별 안됨.
# 실제 챗봇들이 대화기록을 구별하기 위해 [세션session]이라는 개념을 사용.

# 개념을 이해해보면..
#1. 사용자 A가 챗봇과 대화를 시작하면 세션1이 됨
#2. 동시에 사용자 B가 챗봇과 대화를 또 시작하면 세션2가 됨
# 즉, 챗봇은 세션ID를 기반으로 대화기록을 구별하여 답변을 생성함.

# 사용자들의 세션과 ChatMessageHistory 객체를 저장할 dictionary를 생성
session_messages= {}  #빈 딕셔너리  {key(세션ID):value(ChatMessageHistory)}

#세션 ID를 부여하는 여러 방법
#1. UUID를 생성하여 session_id를 생성 [UUID : 범용 고유 식별자 -- 고유한 식별자를 만들어 사용]
#2. 이미 사용자 고유 ID가 존재하고 있다면 이를 사용
#3. 타임스탬프 사용.

# 실습목적으로 간단하게 미리 session_id를 고정
session_id= 'sam'

#혹시 기존에 session_messages로 등록된 id가 있는지 확인 후 등록
if session_id not in session_messages:
    session_messages[session_id]= ChatMessageHistory()

# 대화기록 session_messages 를 chatbot(model+prompt)와 연동되어 응답하도록.. 메모리 챗봇 만들기
# 메모리와 chatbot을 연동해주는 클래스 사용
from langchain_core.runnables.history import RunnableWithMessageHistory
chatbot_memory= RunnableWithMessageHistory(
    chatbot,
    get_session_history= lambda session_id: session_messages[session_id],
    input_messages_key='input',
    history_messages_key='history'
)

#이전 대화를 기억하는 챗봇에게 질문하고 답변받아오기
response= chatbot_memory.invoke({'input':'BTS가 누구인지 설명해줘.'}, config={'configurable':{'session_id': session_id}})
print(response.content)
print('==================================================================================================')
print()
response= chatbot_memory.invoke({'input':'빌보드에서 1등한 곡들은?'}, config={'configurable':{'session_id': session_id}})
print(response.content)





