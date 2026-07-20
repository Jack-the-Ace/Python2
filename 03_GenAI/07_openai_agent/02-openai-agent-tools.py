# openai agent sdk + 도구(함수호출) 결합

from dotenv import load_dotenv
load_dotenv()

from agents import Agent, Runner, function_tool

# 도구로 사용할 함수 만들기 -- @데코레이터 필요.
@function_tool
def get_weather(city:str) -> str:  #파라미터와 리턴값에 자료형을 명시 schema
    """도시의 날씨를 조회합니다."""
    return f"{city}의 현재 날씨는 맑음, 27도C 입니다."

#함수 도구는 여러개일 수 있음.
@function_tool
def get_exchange_rate() -> str:
    '''USD/KRW 환율을 조회합니다.'''
    import requests
    r=requests.get('https://')
    return r.text

#DB정보 읽어오는 기능함수
@function_tool
def search_customer(name:str, amount:int) -> str:
    '''
    고객 정보를 조회합니다.
    
    Args:
    name: 검색할 고객 이름
    amount: 계좌 정보
    '''
    #DB조회
    return f'{name} 고객님은 VIP 회원입니다.'

#1. agent 만들기
agent= Agent(
    name= "Weather Agent",
    model='gpt-4o-mini',
    instructions='''
    사용자가 날씨를 물어보면 get_weather 도구를 사용합니다.
    ''',
    tools=[get_weather],
)

result= Runner.run_sync(agent, '서울 날씨 알려줘')
print(result.final_output)






