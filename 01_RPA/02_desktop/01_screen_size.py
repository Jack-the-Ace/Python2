# python의 desktop 자동화 외부 모듈 설치 : pyautogui

# 1. import
import pyautogui

# 2. 현재 화면 (스크린-모니터) 사이즈 알아보기
size= pyautogui.size()
print(size)
print()

#----------------------듀얼모니터.. 를 사용할때 모니터별 사이즈 알고싶다면... 추가모듈 screeninfo
from screeninfo import get_monitors

# 모든 모니터 정보 가져오기
monitors=get_monitors()

# 0번이 주 모니터, 1번이 보조 모니터
if len(monitors)>1:
    secondary = monitors[1]
    print(f'보조 모니터 크기: {secondary.width} x {secondary.height}')
    print(f'보조 모니터의 위치(좌표): {secondary.x}, {secondary.y}')
else:
    print('보조 모니터가 감지되지 않았습니다.')
