#실시간 음성 인식으로 정확한 텍스트 변환 Speech to Text 

#가격
#1. whisper-1 : 분당 $0.006
#2. gpt-4o-transcribe : 분당 $0.006 (오디오 입력 기준)
#3. gpt-4o-mini-transcribe : 분당 $0.003    텍스트 출력 1M토큰 $5.00

#1. .env에 있는 api key  읽어오기
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
from pathlib import Path
client= OpenAI()

# 01예제에서 만든 음성파일 읽어서 글씨로 보여주기
#audio_file_path= Path(__file__).parent / 'speech.mp3'

# 03예제에서 녹음한 음성파일 읽어서 글씨로 보여주기
audio_file_path= Path(__file__).parent / 'recorded_audio.wav'

# 경로의 오디로 파일을 읽어오기(바이너리로..)
audio_file= open(audio_file_path, 'rb')

# ai에게 오디오데이터를 주고 글씨를 응답받기
transcript= client.audio.transcriptions.create(
    model='gpt-4o-mini-transcribe',
    file=audio_file, #오디오 데이터 바이트 덩어리...
    response_format='text'
)

#추출된 글씨를 출력
print(transcript)
