# python의 PDF 리더 모듈 중 3대장
# pip install pypdf   : 기본 모듈
# pip install pymupdf : pdf를 다루는 다양한 기능이 추가된 모듈
# pip install pdfplumber : pdf에서 표, 텍스트, 비텍스트 요소를 구분하여 추출해주는 모듈

# pip install langchain-community  :  랭체임과 pdf loader 모듈 연결해주는 모듈

# 시간상 1개만 해보기.  [나머지도 코드는 거의 비슷]
# 3개 모듈 모두 랭체인과 자동 연동됨.

from langchain_community.document_loaders import PyPDFLoader  # 향후에는 langchain_pdf
loader= PyPDFLoader("./05_langchain_rag/2023_북한인권보고서.pdf")

#문서 읽기
docs= loader.load()
print('문서의 개수(페이지수):', len(docs))

# 문서를 읽고 청크까지 나눠주는 기능이 있음.
chunks= loader.load_and_split()   # 이제는 권장하지 않음. 청크 품질이 안좋음.
print('청크의 개수:', len(chunks))
#-----------------------------------------------------------------------------------------------------------
# RecursiveCharacterTextSplitter 를 권장.




















