# Agent SDK : Responses api 를 대체하는 것이 아니라, 더 복잡한 에이전트 애플리케이션을 쉽게 만들기 위한 프레임워크

#0. 모듈 설치
# pip install openai-agents

#1. api key load
from dotenv import load_dotenv
load_dotenv()

#2. openai 에서 만든 agent 개발용 모듈 사용
from agents import Agent, Runner

#3. 영어회화를 도와주는 전문 agent 만들기
english_agent=Agent(
    name='영어회화 선생님',
    model='gpt-4o-mini',
    instructions="""
    [role]
    너는 영어회화 학습을 주도적으로 도와주는 친절한 전문 영어선생이야.

    [task]
    사용자가 초보라고 생각하며 대화를 주도해.
    사용자의 문장에서 문법적 오류나 관용구 등에 개선이 필요하다면 알려줘.
    사용자의 답변을 유도하며 초보부터 단계적으로 학습수준을 높여줘.
    """
)
#---------------------------------------------------------------------------------------------------------------

#4. agent에게 답변을 요청
# result= Runner.run_sync(english_agent, 'hello')
# print(result.final_output)
# print("="*100)

# input_text= input('질문입력:')
# result= Runner.run_sync(english_agent, input=input_text)
# print(result.final_output)
# print("="*100)

#5. 위 코드를 반복문으로 처리하여 채팅처럼 대화 이어가기.(특정 단어를 입력하면 종료!)
while True:
    input_text= input('user : ')
    if input_text.strip().lower() == 'exit':
        break

    result= Runner.run_sync(
        english_agent,
        input=input_text
    )
    print('ai tutor : ', result.final_output)
    print("="*100)
print()
















