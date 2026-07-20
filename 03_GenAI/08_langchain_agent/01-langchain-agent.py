#랭체인 프레임워크를 사용하여 OpenAI, Anthropic, Google, Llama, 자체 LLM 등
#AI 모델 회사별 Agent SDK를 추상화 하여 통일된 방식으로 에이전트 구현 가능

#0. 설치
# pip install langchain langchain-openai (= langchain + langchain-openai)

#1. api key load
from dotenv import load_dotenv
load_dotenv()

#2. 랭체인 LLM 모델 만들기
from langchain_openai import ChatOpenAI
model= ChatOpenAI(model='gpt-4o-mini', temperature=0)

#3. 랭체인 Tools 연결
from langchain.tools import tool

@tool
def multiply(a:int, b:int) -> int:
    '''두 숫자를 곱합니다.'''
    return a*b
    #return a+b

#4. Agent 생성
from langchain.agents import create_agent
agent= create_agent(
    model=model,  # 이 모델은 다른 AI회사의 LLM으로 변경해도 됨. [모델 추상화]
    tools=[multiply]
)

#5. Agent 실행(사용자 질문)
response= agent.invoke({
    "messages":[{'role':'user','content':'123과 456을 곱해줘.'}]
})
print(response)
print('-'*100)
#마지막 AI응답 메세지만 출력
print(response['messages'][-1].content)
print()
#----------------------------------------------------------------------------------------------------------------------

#6. 여러개의 도구 연결
@tool
def substract(a:int, b:int)->int:
    '''두 숫자를 뺄셈합니다.'''
    return a-b

@tool
def weather(city:str)->str:
    '''도시의 날씨를 조회합니다.'''
    return f'{city}의 날씨는 맑음입니다. 최고기온은 31도, 최저기온은 22도 입니다.'

agent= create_agent(
    model=model,
    tools=[substract, multiply, weather]
)

#호출
response= agent.invoke({
    "messages":[
        {'role':'user','content':'서울 날씨 알려주고 가장 낮은 온도와 가장 높은 온도의 차이를 구해줘.'}
    ]
})
print(response['messages'][-1].content)
print('='*100)
print()
#-----------------------------------------------------------------------------------------------------------------------------

#7. 대화 메모리 사용  --  pip install langgraph
from langgraph.checkpoint.memory import InMemorySaver
memory= InMemorySaver()

agent= create_agent(
    model=model,
    tools=[substract, multiply, weather],
    checkpointer=memory
)

#대화기록 식별자를 langgraph 이전에는 session_id로 지칭했으나..
#랭그래프에서는 thread_id로 지칭함.
# responses api의 previous의 경우에는 다른 사람의 대화기록도 활용될 수 있지만.
# thread_id를 통해 대화구분이 용이해짐.

config= {
    "configurable":{
        "thread_id":'sam'
    }
}

response= agent.invoke({
    "messages":[{'role':'user','content':'내 이름은 홍길동이야.'}]
}, config=config)
print(response['messages'][-1].content)

response= agent.invoke({
    "messages":[{'role':'user','content':'내 이름이 뭐였지?'}]
}, config=config)
print(response['messages'][-1].content)
print()
#-----------------------------------------------------------------------------------------------------------------
#8. 시스템 프롬프트 - 지침
agent= create_agent(
    model=model,
    tools=[substract, multiply],
    system_prompt='''
    당신은 친절한 AI 비서입니다.
    항상 한국어로 답변하세요.
    계산이 필요하면 Tool을 사용하세요.
    '''
)

response= agent.invoke({
    "messages":[{'role':'user','content':'1970년생이면 지금이 몇살이지?'}]
})
print(response['messages'][-1].content)
print('='*100)
print()
#----------------------------------------------------------------------------------------------------------------------

#9. 토큰 단위로 스트리밍 하기: 실시간으로 글자가 생성되는 것 처럼 출력되도록.. 타자 써지도록(like. chat gpt)
agent= create_agent(model=model, system_prompt='너는 강아지야. 이름은 울이야.')
for token, metadata in agent.stream({"messages":[{'role':'user','content':'파이썬을 소개해줘'}]},stream_mode='messages'):
    print(token.content, end='',flush=True)
    