# 특정 프로그램을 자동 실행하는 방법

#0. 파이썬의 표준 라이브러리
import subprocess

#1. 크롬 브라우저 실행
chrome_path= 'C:/Program Files/Google/Chrome/Application/chrome.exe'
subprocess.Popen(chrome_path)

#크롬 앱이 실행되길 잠시 대기
import time
time.sleep(1)

import pyautogui
pyautogui.hotkey('ctrl','t') # 새 탭 열기
time.sleep(2)

#2. 메모장 앱 실행 -- 메모장 프로그램 설치 위치.. 알고싶다면.. cmd창에 where notepad
notepad_path=r'C:\Users\mbc\AppData\Local\Microsoft\WindowsApps\notepad.exe'
subprocess.Popen(notepad_path)

time.sleep(1)
pyautogui.write('Hello. nice to meet you', interval=0.1)

#3. 단축키로 그림판 실행해보기
pyautogui.hotkey('win','r') #검색기능
pyautogui.write('mspaint') #그림판 프로그램 명
pyautogui.press('enter')


