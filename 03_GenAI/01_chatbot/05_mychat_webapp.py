# 스트림릿 모듈을 이용하여 챗봇 UI 구성 방법 실습

#0. 모듈
# pip install streamlit

#1. 모듈 사용
import streamlit as st

#2. 채팅 메세지 UI를 만드는 기능함수
with st.chat_message('user'):
    st.write('안녕하세요.')

with st.chat_message('assistant'):
    st.write('반가워요.~ :)')

# 'role'역할에 없는 명칭을 사용하면 첫글자 표시
with st.chat_message('bot'):
    st.write('this is bot')

with st.chat_message('sam'):
    st.write('this is sam')

with st.chat_message('홍길동'):
    st.write('this is hong')
    st.write('반가워')
    st.button('눌러줘')

# 한줄로 간결하게..
st.chat_message('ai').write('한줄로 써도 됩니다.')
st.divider()


#2) 채팅처럼 대화하는 형태가 되려면 각각의 메세지들을 리스트로 잘 보관되어 있어야 함.
# 단, 메세지 데이터는 {역할:'', 내용:''} 구조로 만들어야 함.
messages=[
    {'role':'assistant','content':'무엇을 도와드릴까요?'},
    {'role':'user','content':'대한민국의 수도는?'},
    {'role':'assistant','content':'대한민국의 수도는 **서울**입니다.'},
    {'role':'user','content':'오... 고맙 ㅎ'}
]

for msg in messages:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])
st.divider()


#3) 사용자 채팅메세지 입력 UI

#이전 채팅메세지가 사라질것임. streamlit의 랜더링 방식때문에..
# 새로운 메세지가 입력될때마다 이 프로그램을 처음부터 다시 실행함. 즉, react의 state 화면갱신과 같음
# 그래서 화면이 갱신되어도 데이터를 저장하는 변수를 streamlit에서 제공함
# st.session_state 라고 부름

# a. messages 라는 이름의 변수가 st.session_state 에 존재하는지 부터 확인하고 첫 문장 저장
if "messages" not in st.session_state:
    st.session_state.messages=[
        {'role':'assistant','content':'무엇이든 물어보세요'},
    ]

# b. st.session_state에 저장된 "messages" 리스트들을 채팅메세지로 그려내기
for msg in st.session_state.messages:
    st.chat_message(msg['role']).markdown(msg['content'])

question= st.chat_input('질문을 입력하세요.')  # 화면의 bottom에 위치함 - enter 입력완료. shift+enter 줄바꿈
if question:
    question= question.replace('\n','  \n')
    st.session_state.messages.append({'role':'user','content':question})
    st.chat_message('user').write(question)

    #입력메세지에 대해 ai모델을 이용하여 응답하도록.. 지금은 실습을 위해.. Mock 데이터
    response= f'{question}에 대해 알고싶군요,  \n 어쩌구 저쩌구...'  #마크다운에서 줄바꿈은 \n 앞에 띄어쓰기 2개 있어야함
    st.session_state.messages.append({'role':'assistant','content':response})
    st.chat_message('assistant').markdown(response)

#-------------------------------------------------------------------------------------------
# [실행] 스트림릿을 실행하는 명령어를 터미널에서 수행
# streamlit run 파일명.py




