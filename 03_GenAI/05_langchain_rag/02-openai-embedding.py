# openai 에서 제공하는 임베딩 모듈 사용
# 나중에 RAG를 구축하기 위해 Langchain 프레임워크 모듈과 함께 사용

#0. 필요한 모듈 설치
# pip install langchain
# pip install langchain-openai

#1. 임베딩 모델 import
from langchain_openai import OpenAIEmbeddings

#2. api key 불러오기
from dotenv import load_dotenv
load_dotenv()

#3. 임베딩을 해주는 객체 생성
embeddings= OpenAIEmbeddings(model='text-embedding-ada-002')

#[임베딩 테스트] 텍스트를 주고 임베딩 요청 -- 숫자로 된 벡터값으로 만들어 주세요~
# result= embeddings.embed_query('저는 배가 고파요')
# print(result)  # 벡터값 확인 가능 [0.0485, -0.015, 0.75,.................]
#----------------------------------------------------------------------------------------------------

#4. 여러개의 문장을 가진 데이터 준비(RAG에서는 chunk들)
data= [
    '저는 배가 고파요',
    '저기 배가 지나가네요',
    '굶어서 허기가 지네요',
    '허기워기라는 게임이 매우 재밌어',
    '스팀에서 재밌는거 해야지',
    '스팀에어프라이어로 연어구이 해먹을거야',
]

#데이터의 출력을 보기좋게 pandas 라는 표형태(데이터프레임)의 데이터를 다루는 모듈 사용
import pandas as pd
df= pd.DataFrame(data, columns=['TEXT'])
#print(df)

# TEXT컬룸만 가진 df에 새로운 컬룸을 추가하고 그 값들로 글씨의 벡터값을 저장
vector_data= []
for text in data:
    vector_data.append(embeddings.embed_query(text))

df['VECTOR']= vector_data  # 새로운 'VECTOR'컬룸을 만들고 데이터들을 대입해줌
print(df)
print('=========================================================================================================')
print()

#[구현] 벡터값들을 이용하여 사용자가 입력한 어떤 문장과 가장 유사도가 높은 상위 3문장 뽑아내기
#1) 유사도 계산 함수 만들기
import numpy as np
from numpy import dot
from numpy.linalg import norm
def cos_sim(A,B):
    return dot(A,B)/(norm(A)*norm(B))

#2) 전달받은 글씨와 가장 유사도가 높은 문장을 dataframe 에서 찾아서 유사도값이 높은 상위 3개만 리턴하는 함수 만들기
def get_similarity_top3(df,query):
    #사용자 요청질문을 임베딩하기
    vector_query= embeddings.embed_query(query)

    #문장들의 벡터값을 가진 데이터프레임(df)의 각 줄마다 위 사용자 요청글씨 벡터값과의 유사도 구하기
    similarities= []
    for i in range(len(df)):  #데이터프레임의 개수만큼
        #현재번째 줄의 벡터값
        vector=df.iloc[i]['VECTOR']

        #벡터의 수학적 계산을 위해 넘파이 배열로 만들기
        A= np.array(vector_query)  #사용자 질문
        B= np.array(vector)        #현재번째 문장

        similarities.append(cos_sim(A,B))
    #-------------------------------------------for문 끝

    #구해진 유사도 값들을 데이터프레임의 새로운 컬룸을 만들어 저장
    df['SIMILARITY']= similarities

    # 유사도 높은 top3 추출
    top3= df.sort_values('SIMILARITY', ascending=False).head(3)
    return top3
#----------------------------------------------------------------------------------------------------

#[사용하기] 사용자의 특정 질문과 가장 유사한 문장을 찾기
result=get_similarity_top3(df=df, query='아무것도 안먹었더니 꼬르륵 소리가 나네')
print(result)




