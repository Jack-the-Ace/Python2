# 벡터값을 체계적으로 저장하는 벡터 DB 중 유명한 오픈소스 3개
#1. Chroma (크로마) : 처음 다루기 용이. 대규모에는 적합하지 않음. python하고 잘 맞음
#2. Faiss  (파이스) : 검색속도 빠름. GPU 사용. 대규모 용이. / DB라기 보다는 검색엔진에 가까움. CRUD, 메타데이터를 직접 구현해야 함.
#3. Milvus (밀버스) : 완전한 벡터 DB. 분산저장. 수억~수십억 벡터 지원 / 설치와 운영이 복잡. 리소스 요구량이 큼

# [실습 - Chroma] --   pip install langchain-chroma 
# RAG 서비스를 위한 벡터DB 저장 워크플로 구상하기 --------
#1. 데이터 준비 - RAG에 사용할 PDF문서를 읽어와서 LLM이 처리할 수 있는 단위로 자르기(chunk) : pyPDFLoader, RecursiveCharacterTextSplitter
#2. 청크들(문장들)을 벡터값으로 임베딩 : OpenAIEmbeddings [비용발생]
#3. chroma 벡터DB에 저장하고 질문에 대해 유사도가 높은 문자 추출 : chroma
#----------------------------------------------------------------------------------------------------------------------------------

#1. PDF파일을 읽어와서 적절한 크기로 잘라 chunk 만들기
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader= PyPDFLoader('./05_langchain_rag/2023_북한인권보고서.pdf')
docs= loader.load()
splitter= RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks= splitter.split_documents(docs)
print(len(chunks))
print('============================================================================================================================')
print()

#2. 청크들을 벡터값으로 만들어주는 임베딩 객체 준비 (api key 필요)
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAIEmbeddings
embeddings= OpenAIEmbeddings(model='text-embedding-ada-002')
# 벡터값을 만드는 작업은 직접하지 않고.. 벡터DB를 만들때 임베딩 객체를 주면 알아서 벡터화 진행함.

#3. 벡터 DB 만들기
from langchain_chroma import Chroma
db= Chroma.from_documents(chunks, embedding=embeddings)  # 이때 돈!!
print('저장된 문서의 개수:', db._collection.count())   # No-SQL 방식.. _collection(컬렉션: RDBMS의 테이블 같은 역할 )
print('=============================================================================================')
print()

# [벡터 DB 사용]
#1) 사용자의 특정 질문에 대한 답변을 위해 검색할 유사도가 높은 문장들 찾기
question= '북한의 교육 과정'
docs= db.similarity_search(query=question)
print(f'{question}과 유사한 문서의 개수:', len(docs))

# 각 문장들이 무엇인지 확인해보기
for doc in docs:
    print(doc)
    print('================================================================================================')
#-------------------------------------------------------------------------------------------------------------

#2) 상위 3개의 문서로만 제한하고 유사도 점수도 같이 확인해보기
top3_docs= db.similarity_search_with_relevance_scores(question, k=3)
for doc in top3_docs:
    print(doc)
    print('================================================================================================')
#--------------------------------------------------------------------------------------------------------------

#4. 벡터DB를 만들때 영구적으로 데이터를 저장하여 재사용하는 것이 효율적
#1) chroma vector dv에 청크들을 저장하면서  .db 파일로 저장하기
db1= Chroma.from_documents(chunks, embedding=embeddings, persist_directory='./05_langchain_rag/chroma_test.db')
print('벡터로 잘 저장되었습니다. 문서개수:', db1._collection.count())
print()

#2) 저장되어 있는 .db로부터 크로마 벡터 DB객체 생성하여 사용하기
db2= Chroma(persist_directory='./05_langchain_rag/chroma_test.db', embedding_function=embeddings)
print('파일에서 읽어온 벡터DB의 문서 개수:',db2._collection.count())

question='북한의 군 복무기간'
docs= db2.similarity_search_with_relevance_scores(query=question, k=3)
for doc in docs:
    print(doc)















