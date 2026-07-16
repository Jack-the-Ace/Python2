from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

script= "요약을 원하는 장문의 텍스트"
llm= ChatOpenAI(
    model='gpt-4o-mini',
    temperature=0.2,
    max_completion_tokens=1200,
)
prompt= ChatPromptTemplate.from_template(
    "다음 내용을 한 문장으로 요약해주세요. : {text}" 
)
parser= StrOutputParser()

chain= prompt | llm | parser

response= chain.invoke({'text':'나는 오늘 축구를 봤다. 근데 한국팀이 졌다. 패배원인은 홍명보 때문이라고 생각한다. 하지만 홍명보는 LA로 도망갔다. 현재 한국 대표팀 감독은 공석이다.'})
print(response)