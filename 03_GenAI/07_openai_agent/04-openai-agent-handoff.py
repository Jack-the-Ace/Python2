# 여러 Agent를 조율하여 최종 목적을 달성하도록 하는 에이전틱 AI 개발에 용이한 기능

# 예제: 수학 Agent와 역사 Agent

from dotenv import load_dotenv
load_dotenv()

from agents import Agent, Runner

#1) 수학 Agent
math_agent= Agent(
    name='수학 선생님',
    model='gpt-4o-mini',
    instructions='''수학문제를 해결하는 전문가입니다.'''
)

#2) 역사 Agent
history_agent= Agent(
    name='역사 선생님',
    model='gpt-4o-mini',
    instructions='''역사 질문에 답하는 전문가입니다.'''
)

#문제해결에 적절한 agent를 조절하는 라우터 Agent.. 즉, 여러 Agent를 오케스트레이션하는 메인 Agent
router= Agent(
    name='감독 에이전트',
    model='gpt-4o-mini',
    instructions='''
    질문을 보고 적절한 전문가에게 전달하세요.
    두 전문가의 지식이 모두 필요하다면 한 에이전트의 결과를 다른 에이전트가 입력으로 받아 대답해줘.
    두 전문가의 지식이 아닌 것이면 '모르는 분야입니다. 저는 역사/수학 에이전트 입니다.' 라고 응답해.

    [제한사항]
    markdown 문법을 사용하지 말 것!
    ''',
    handoffs=[math_agent, history_agent]
)

#(실습)
# result=Runner.run_sync(router, '세종대왕은 누구인가?') #역사
# print(result.final_output)
# print('='*100)

# result=Runner.run_sync(router, '표준점수는 어떻게 구하는가?') #수학
# print(result.final_output)
# print('='*100)

# result=Runner.run_sync(router, '조선이 건국된지 올해로 몇 년이 되었나요?') #역사+수학
# print(result.final_output)
# print('='*100)

result=Runner.run_sync(router, '3박4일 일본 여행일정을 계획해줘') #다른 분야
print(result.final_output)
print('='*100)

