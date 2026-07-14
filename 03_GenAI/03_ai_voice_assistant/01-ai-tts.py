#TTS : 텍스트를 자연스러운 음성으로 변환 Text to Speech
#openai tts api 검색
# openai에서 제공하는 tts 모델의 price
#1. gpt-4o-mini-tts [텍스트 입력: 100만 토큰 당 $0.60,  오디오 출력: 100만 토큰당 $1.20]
#2. tts-1    : 백만토큰당 $15.0
#3. tts-1-hd : 백만토큰당 $30.0

#1. .env 에 있는 api key 값 읽어오기
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client= OpenAI()

# 음성으로 변환한 음성파일을 저장할 경로와 파일명 미리 지정
from pathlib import Path
audio_file_path= Path(__file__).parent / 'speech.mp3' # 현재 실행 중인 파일이 위치한 폴더에 "speech.mp3" 파일명으로 경로 만들기
# pathlib 모듈에서 / 연산자는 나눗셈이 아니라 경로를 결합(join)하는 연산자
# macos, linux, windows 마다 경로구분자가 다른데.. 이를 알아서 해줌.

with client.audio.speech.with_streaming_response.create(
    model='gpt-4o-mini-tts',
    voice='ballad',  # https://www.openai.fm/  에서 목소리 들을 수 있음
    input='안녕하세요, 저는 AI 비서입니다.',
    instructions='밝고 친절한 톤으로 말해.',

) as response:
    response.stream_to_file(audio_file_path)























