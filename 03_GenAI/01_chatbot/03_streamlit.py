# streamlit : python으로 간단한 웹페이지를 만들 수 있는 고수준 모듈(대신 커스텀이 제한적이어서 실무에서의 사용은 제한적. 프로토타입에 많이 사용됨)

#0. 모듈 설치
# pip install streamlit

#1. 모듈 사용
import streamlit as st

#2. 제목과 기본글씨 표시 [ html의 h요소와 p요소 ]
st.title('Hello streamlit')
st.write('스트림릿을 이용하여 간단하게 웹페이지를 만들 수 있어요.')

#3. 실행은.. 리액트때 처럼 터미널에서 명령어를 통해 실행 (파일이 있는 폴더로 이동)
# streamlit run <파일명.py>
#실행결과 : 웹브라우저 http://localhost:8501
#-------------------------------------------------------------------------------------------------

#4. 다양한 방법으로 글씨 출력
st.write('가장 기본적인 텍스트 출력기능')
st.title('가장 큰 제목')
st.header('title 보다 작은 제목글씨')
st.subheader('서브 제목글씨')

# 마크다운 문법으로 출력 가능 (html과 같은 마크업 언어를 보다 간결하게.. 마크다운문법. 나중에 colab 다룰때 별도 수업예정)
st.markdown('**마크다운 문법 strong**')
st.markdown('*마크다운 문법 emphasize*')
st.markdown('# h1요소')  #  # 다음에 띄어쓰기!
st.markdown('## h2요소')
st.markdown('### h3요소')
st.markdown('#### h4요소')
st.markdown('- openai')
st.markdown('- google genai')
st.markdown('---')   # 수평선 <hr>

# streamlit이 버전업이 되면서 그냥 write()기능에 마크다운을 써도 인식됨
st.write('**마크다운 잘됨**')

# 설명이나 주석을 표시
st.caption('설명이나 주석')   #회색으로 표시

# AI나 머신러닝 개발자들이 본인 코드를 소개할때 사용하기 편하도록..
# 코드를 출력하는 기능
st.code('import streamlit as st', language='python')
# 여러줄의 코드를 출력하려면.. 세따옴표 사용
st.code('''
import requests
        
response= requests.get('https://www.naver.com')
print(response.text)
''', language='python')

# 언어를 다르게 설정해도 보여짐. 다만.. 색상표시가 좋지않음.. 인식을 못해서.
st.code('document.write("Hello Javascript")', language='python')
st.code('document.write("Hello Javascript")', language='javascript')

# 데이터분석이나 머신러닝은 수학적 표현식이 많음.
# 대부분의 수학식에는 편의를 위해 라틴어를 사용함. 이를 위한 전용 문법 LaTeX 문법
st.latex(' a^{2}+b^{2}=c^{2}')
st.latex(r'c=\sqrt{a^{2}+b^{2}}', width='content')
st.latex(r'\sigma(x) = \frac{1}{1 + \exp(-x)}')

#5. 기본적으로 streamlit 글씨는 색상을 지정하는 문법이 없음.
# 대신 글씨의 성질에 따라 다른 색상으로 표시하는 기능이 있음.
st.success('정상 처리 완료!')
st.warning('주의 필요!')
st.error('에러 발생!')
st.info('정보 메세지')

#전체 테마 색상 변경도 있지만... 모든 글씨의 색상이 바뀌기에 권장하지 않음.
#설정문서를 만들어 처리 .streamlit/config.toml

st.divider()   # 가로 구분선 <hr>과 같은 기능

#6. 사용자 입력 받기
#1) 글씨 입력
name= st.text_input('이름을 입력하세요.') #enter를 치면 입력됨
st.write(f"입력된 이름: {name}")
st.divider()

#2) 숫자 입력
age= st.number_input('나이를 입력하세요.', min_value=0, max_value=100, step=1)
st.write(f"입력된 나이: {age}")
st.divider()

#3) 슬라이더 입력
number= st.slider('this is slider', min_value=0, max_value=100, step=2, value=24)
st.write(f"변경된 숫자: {number}")

# 범위로 슬라이더 사용
number_range= st.slider('this is slider', min_value=0, max_value=100, step=2, value=(24,60))
st.write(f"변경된 범위: {number_range}")
st.write(f'최소: {number_range[0]}')
st.write(f'최대: {number_range[1]}')
st.divider()

#4) 날짜 입력
selected_date= st.date_input('날짜 선택')
st.write(f"선택한 날짜: {selected_date}")
st.divider()

#5) 시간 입력
selected_time= st.time_input('시간 선택')
st.write(f"선택한 시간: {selected_time}")
st.divider()

#6) 여러줄 입력
message= st.text_area('메세지를 입력하세요.')  #enter가 줄바꿈. ctrl+enter가 입력완료
st.write(f"입력된 메세지:\n{message}")
st.divider()

#7) 파일 업로드 [드래그 or 탐색기 선택]
file= st.file_uploader("파일을 업로드 하세요.")
if file is not None:
    st.write('업로드 된 파일: ', file.name)
st.divider()

#여러개 파일 선택
file_list= st.file_uploader("파일을 업로드 하세요.", accept_multiple_files=True)
if file_list is not None:
    st.write("업로드된 파일 개수: ",len(file_list))
    # 각 파일명을 출력하고 싶다면.. file_list의 요소(file)들의  .name을 출력
    st.info([f.name for f in file_list])  # 리스트의 컴프리헨션..
st.divider()

#8) 색상 선택
color= st.color_picker('색상을 선택하세요.', value="#00FF00")
st.write(f"선택한 색상: {color}")
st.divider()

#7. 버튼 및 선택형 입력
#1) 기본 버튼 -- 클릭 이벤트 콜백함수 처리 대신 if문으로 처리
if st.button('클릭하세요'):  # 버튼을 누르면 True
    st.write('버튼이 클릭되었습니다.')
st.divider()

#2) 체크박스
agree=st.checkbox('동의합니다.')
if agree:
    st.write('동의하셨습니다.')
st.divider()

#체크박스의 라벨이 같으면 구별이 안된다며 에러발생. [혹시 같은 라벨로 써야 한다면.]
agree2=st.checkbox('동의합니다.', key='agree2')
if agree2:
    st.write('동의하셨습니다.')
st.divider()

#3) 라디오 버튼
selected_option=st.radio('옵션을 선택하세요.', options=('옵션1','옵션2','옵션3'))
st.write(f"선택된 옵션: {selected_option}")
st.divider()

#4) 드롭다운 선택
fruits= st.selectbox('과일을 선택하세요.', options=['사과','바나나','오렌지'])
st.write(f"선택된 과일: {fruits}")
st.divider()

#5) 다중선택
planets= st.multiselect('행성들 선택', options=['수성','금성','지구','화성','목성','토성'])
st.write(f"선택된 행성들: {planets}")
st.divider()

#6) 슬라이더 중 특정 값 선택 슬라이더
rating= st.select_slider('평가를 선택하세요', options=['매우 아니다','아니다','보통','그렇다','매우 그렇다'])
st.write(f"선택된 평가: {rating}")
st.divider()
#------------------------------------------------------------------------------------------------------

#8. 미디어 파일 표시
#1)이미지 -- 이미지 라이브러리 필요 -- pillow 모듈 ( pip install pillow )
from PIL import Image

image=Image.open("./media_files/storm.jpg")
st.image(image, caption='storm', width=100)

st.audio("./media_files/old_pop.mp3")
st.video("./media_files/trailer.mp4")
st.divider()
#----------------------------------------------------------------------------

#9. 시각화를 구현하기 용이함
#1) 판다스의 데이터프레임(표 모양)을 이쁘게 출력
import pandas as pd

df= pd.read_csv('./data/student.csv')
#print(df)
#스트림릿으로 아주 쉽게 표형태의 데이터프레임을 출력
st.dataframe(df)
st.table(df)  # 정적 테이블로 보여줄때..
st.divider()

#2) json 데이터도 이쁘게.. 출력
st.json({
    '이름':'홍길동',
    '나이':24,
    'address':'광주'
})
st.divider()

#3) 주요지표 및 통계 출력...
st.metric(label='삼성전자', value='310,000원', delta='1.02%')
st.metric(label='하이닉스', value='2,700,000원', delta='-2.25%')
st.divider()
#------------------------------------------------------------------------------------

#10. 차트 시각화. 지도 시각화
#1) matplotlib
import matplotlib.pyplot as plt
import numpy as np

rand= np.random.normal(1,2, size=20)  # 정규분포 그래프 난수 생성(평균1, 표준편차 2인 정규분포에서 20개 난수 생성)
fig, ax= plt.subplots()
ax.hist(rand, bins=15)

st.pyplot(fig)

#2) 엑셀파일의 데이터를 읽어서 그래프로 시각화 [openpyxl 모듈이 없으면 에러날 수 있음]
student_df= pd.read_excel('./data/scores.xlsx')
df_chart= student_df.set_index('학번')[['중간고사','기말고사']]
st.line_chart(df_chart, color=['#FF0000','#0000FF'])
st.divider()

#지도 출력
st.map()
st.map(latitude='37.5', longitude='126.5', zoom=12)

#데이터프레임으로..
df= pd.DataFrame({
    'lat':[37.5, 37.6],
    'lon':[126.5, 126.6],
    'color':[
        [0,255,0],  # 첫번째 좌표 색상
        [255,0,0, 128]   # 두번째 좌표 색상 : 빨강 + 반투명 
    ]
})
st.map(df)
st.divider()

#12. 상태메세지와 진행률 표시
#1) 진행률 표시
import time

progress_bar= st.progress(0)  #초기값 0
for person in range(0,101,5):
    time.sleep(0.5)
    progress_bar.progress(person)
st.divider()

#2) 스피너 - 시간이 걸리는 작업 로딩 메세지 표시
with st.spinner('잠시 기다려주세요.'):
    # 이 안의 코드가 실행될때까지 spinner 가 보여짐
    time.sleep(4)
st.success('작업완료')

#3) 축하 애니메이션
st.balloons()








