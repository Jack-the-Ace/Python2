# 랭체인 프레임워크 - 생성형 AI 웹앱 개발을 용이하게 해주는 AI용 프레임워크

# LLM모델(OpenAI, Google, Anthropic)마다 구현코드가 일부 다름. 랭체인을 사용하면 모델을 변경해도 코드의 큰 변화없이 동작이 가능함(모델추상화)

#1. 필요한 모듈 설치
# 랭체인 : LLM 애플리케이션을 만들기 위한 core 모듈 pip install langchain
# 랭체인 OpenAI : OpenAI 모델(GPT)을 랭체인과 연결해주는 모듈 pip install langchain-openai
# 랭체인 Google : Google 모델(Gemini)을 랭체인과 연결해주는 모듈 pip install langchain-google-genai
# 랭체인 Anthropic : Anthropic 모델(소넷,오퍼시,미토스)을 랭체인과 연결해주는 모듈 pip install langchain-anthropic

#2. API KEY 환경변수에 등록하고 Model객체 생성하기
from dotenv import load_dotenv
load_dotenv()

# OpenAI
from langchain_openai import ChatOpenAI
model= ChatOpenAI(model='gpt-4o-mini',temperature=1, max_completion_tokens=10000)

# Google
from langchain_google_genai import ChatGoogleGenerativeAI
model_google= ChatGoogleGenerativeAI(model='gemini-3-flash-preview')


#3. 모델에게 질의하고 응답받기
# response= model.invoke('랭체인이 뭐지?')
# print(response)
# print("="*90)
#----------------------------------------------------------------------

#모델에게 지침을 주고 싶다면. 사용자의 발화인지, 시스템의 메세지인지 구별할 수 있어야 함.
#랭체인에서는 3종류의 메세지 클래스를 제공함.

#4. 메세지 종류
# HumanMessage   사용자의 발화를 담는 메세지 클래스   {'role':'user','content':'..'}
# AIMessage      LLM의 응답을 담는 메세지 클래스     {'role':'assistant','content':'..'}
# SystemMessage  시스템 메세지 클래스 (지침 or 역할)  {'role':'system','content':'..'}
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
system_message= SystemMessage(content='너는 랭체인 테스트를 위한 챗봇이야. 모든 질문의 답을 한 문장으로 간단하게 요약해서 대답해.')
ai_message= AIMessage(content='무엇이든 물어보세요, 한 문장으로 설명해줄께요!')
user_message= HumanMessage(content='안녕? 랭체인이 뭐지?')

# 모델에게 입력하기 위해 리스트로 만들기
messages= []
messages.append(system_message)
messages.append(user_message)

# 모델에게 메세지를 전달하고 응답받기
response= model.invoke(messages)
print(response.content)
print('='*50)

# google model에 메세지를 전달하고 응답받기
response2= model_google.invoke(messages)
print(response2.content)

# LLM이 응답이 모두 완료될때 까지...는 화면에 아무것도 표시되지 않음.
# 모델이 데이터를 조금씩 생성할때 마다 바로바로 출력해서 마치 타자써지듯 구현 가능
# stream 기능












