# LCEL [LangChain Expression Language] : 랭체인에서 체인을 구성하기 위한 표현언어
# 핵심 아이디어는 Runnable (각 도구들. 작업수행자들) 들을 파이프(|)로 연결

# 총 3개의 runnable 을 연결해보기(prompt - model - 출력파서)

#0. api key
from dotenv import load_dotenv
load_dotenv()

#1. 체인으로 구성할 구성요소들 import
from langchain_core.prompts import ChatPromptTemplate     # 프롬프트 템플릿
from langchain_openai import ChatOpenAI                   # LLM
from langchain_core.output_parsers import StrOutputParser # 출력 파서

#1) 프롬프트 템플릿
prompt= ChatPromptTemplate.from_template(
    "다음 문장을 영어로 번역하세요: {text}"
)

#2) LLM모델
model= ChatOpenAI(model='gpt-4o-mini')

#3) 출력파서 - 응답을 일반 문자열로...
parser= StrOutputParser()

#(핵심) 랭체인의 체이닝 기법(순서 중요! ~파이프라인 구축~) : 입력 -> prompt -> LLM -> output parser -> 최종문자열
chain= prompt | model | parser

#요청 및 응답
response= chain.invoke({'text':'안녕하세요.'})
print(response)
print('=========================================================================================')

#출력파서의 종류는 아주 많음. 검색
from langchain_core.output_parsers import JsonOutputParser
parser= JsonOutputParser()

prompt= ChatPromptTemplate.from_template('''
다음 문장을 JSON으로 출력하세요.
                                         
문장 : {text}
                                         
반드시 아래 형식으로만 출력하세요.
{{"message:":"<문장>"}}
''')

chain= prompt | model | parser
response= chain.invoke({'text':'나는 홍길동 입니다.'})
print(response)


######################################################################

#[수행1] part8 유튜브 요약/번역 서비스
#[수행2] part9 이미지생성 동화 AI