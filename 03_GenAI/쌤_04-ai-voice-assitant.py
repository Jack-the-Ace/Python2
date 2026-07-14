# AI 음성 비서의 워크플로와 파이프라인 구축
# 사용자 음성데이터 --> STT --> openai model 응답 --> TTS --> 사용자 음성으로 듣기

#0. 필요한 모듈 사용
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import streamlit as st

#1. openai 생성형 api 객체 준비 .. api key 읽어오기
load_dotenv()
client= OpenAI()

#[기능함수 #1] 오디오 데이터를 글씨를 변환
def STT(audio_data):
    # 오디오 데이터를 파일로 저장
    with open('audio_question.wav', 'wb') as f:
        f.write(audio_data.getvalue())
    
    # 음성파일 읽어오기
    audio_file= open('audio_question.wav', "rb")

    # openai api를 이용하여 음성을 글씨로 변환
    transcript= client.audio.transcriptions.create(
        model='gpt-4o-mini-transcribe',
        file=audio_file,
        response_format='text'
    )

    return transcript #음성에서 추출된 글씨 데이터 ... 반환
#------------------------------------------------

#[기능함수 #2] 사용자 질문에 대한 GPT 모델의 응답 기능 함수 만들기...
def askGPT(prompt):
    #AI 답변 지침을 정의하기.----
    instrunctions='''
    ** role **
    너는 웹사이트를 검색하여 질문에 대답해주는 유능한 비서야.

    ** task **
    - 답변은 가급적 짧게 해.
    - 미리학습된 질문내용이 아니면 웹검색을 통해 대답해.
    - 답변이 10줄이 넘어가면 더 할지 물어봐.
    - 정보만 답변하고 실제 예약, 선택등의 실제 action 은 수행하지 말고 물어봐.
    - 답변의 근거가 명확하지 않다면 '죄송합니다. 답변이 부정확합니다.'라고 응답하고. 이유를 1줄로 말해줘.
    '''
    #-------------------------

    response= client.responses.create(
        model='gpt-5-nano',
        input= prompt,
        instructions=instrunctions,
        max_output_tokens=10000,
        tools=[{'type':'web_search'}]
    )
    return response.output_text
#---------------------------------------

#[기능함수#3] GPT 응답 글씨를 음성으로 출력하기
def TTS(text):
    audio_file_path= Path(__file__).parent / 'response_audio.mp3'

    with client.audio.speech.with_streaming_response.create(
        model='gpt-4o-mini-tts',
        voice='marin',
        input=text,
        instructions='밝고 친절한 톤으로 말해.',
    ) as response:
        response.stream_to_file(audio_file_path)

    #저장된 음성을 streamlit 에서 자동 재생되도록...
    #html에서 음성을 실행하는 요소를 이용 (단, 스트림릿은 정책문제로 오디오파일 경로를 직접 플레이하는 것은 금지.. 음성바이트값들을 글씨로 변환하는 base64 데이터형식으로 변경하여 플레이해야 함)
    import base64
    with open(audio_file_path, "rb") as f:
        data= f.read()
        b64= base64.b64encode(data).decode() #재생을 위해 decode()

        md=f'''
        <audio>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        '''
        st.markdown(md, unsafe_allow_html=True)
#------------------------------------------------

#화면 구현
def main():
    #탭에 표시될 이름
    st.set_page_config(page_title='음성 비서 챗봇', layout='wide')

    #화면을 2개의 컬룸으로 구성
    col1, col2= st.columns([1,3], gap='large') #너비비율 1:3

    #왼쪽 컬룸(사용자의 음성입력 영역)
    with col1:
        st.header('AI VOICE ASSISTANT')
        st.image('./logo-ai-voice-assistant.png', width=200)
        st.markdown('---')

        #오디오 녹음 버튼
        audio_data= st.audio_input('마이크를 누르고 질문하세요.')
        if audio_data is not None:
            # 사용자의 질문 음성을 채팅창에 쓰기
            #1) 음성을 글씨로 변환 [기능함수#1]
            question= STT(audio_data)

            #2) 이전 메세지가 기억되기 위해..
            st.session_state.messages.append({'role':'user','content':question})

            #3) question에 대한 openai의 비서 응답을 받기
            response= askGPT(question)

            #4) 응답결과를 챗봇에 표시하기.
            st.session_state.messages.append({'role':'assistant','content':response})

            #5) 응답글씨를 음성으로 읽어주기
            TTS(response)
    
    #오른쪽 컬룸(채팅화면 영역)
    with col2:
        st.header('대화 기록')
        st.markdown('---')

        #a. sesstion_state에 messages 리스트 보관
        if "messages" not in st.session_state:
            st.session_state.messages= [{'role':'assistant','content':'저는 음성 비서입니다. 무엇이든 물어보세요.'}]
        
        #b. session_state에 저장된 메세지리스트들 모두 채팅메세지로 출력
        for msg in st.session_state.messages:
            st.chat_message(msg['role']).markdown(msg['content'])


# 모듈이 아니라면 실행
if __name__ == '__main__':
    main()


#[수행과제]
#1. 교재 part5. 이미지분석 설명 AI 도슨트
#2. 교재 part9. 이미지생성 스토리동화 파이프라인 이해하기 ~~ zeta 라는 ai app 과 비슷한 컨셉.
#              (랭체인을 사용하지 않고도 구현가능. 
#               ch09_gpt.py 문서의 get_llm()함수의 내용을 
#               그냥 responses api의 instructions로 구현하면 됨.)
#               --- 사용하는 쪽도 invoke()대신 응답 메세지 활용.


