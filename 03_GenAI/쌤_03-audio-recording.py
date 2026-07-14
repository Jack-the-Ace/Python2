#스트림릿에서 오디오를 입력받는 방법

import streamlit as st
st.title('음성 녹음 테스트')

# 사용자로 부터 오디오을 입력받는 기능
audio_data= st.audio_input('마이크를 대고 말씀하세요.')

# 녹음된 오디오 데이터가 있는지 확인
if audio_data is not None:
    st.success('녹음이 완료되었습니다.!')
    #오디오 재생
    st.audio(audio_data, format='audio/wav') #streamlit 은 무조건 .wav 만 가능

    #파일에 저장
    with open('recorded_audio.wav', 'wb') as f:
        f.write(audio_data.getvalue())
    
    st.write('파일 저장 완료: recorded_audio.wav')
    st.write(audio_data.type)
