# 키보드 조작

import pyautogui

# 메모장 앱을 실행하여 그 안에 글씨를 쓰도록..
window=pyautogui.getWindowsWithTitle('제목 없음')[0]
window.activate()

# 메모장에 클릭하여 글씨 입력상태로 만들 시간을 확보하기 위해..
pyautogui.sleep(2)  # 2초 사이에 메모장 클릭하세요......

#1. 글쓰기
pyautogui.write('Hello, ')
pyautogui.write('Nice to meet you', interval=0.25) #타자 써지듯이..

# 단점. 한글은 안됨
pyautogui.write('안녕하세요')
#꼼수로 되게 할 수 있음.
pyautogui.write('dkssudgktpdy~!') #권장하지 않음.
#우회방법으로 한글을 써야함.. 이건 조금 후에...

#2. enter, shift, ctrl 등의 키보드 특수키를 사용하려면.. .write()대신 .press()
pyautogui.sleep(1)
pyautogui.write('  enter')  # enter라는 글씨..
pyautogui.sleep(1)
pyautogui.press('enter') # 엔터키
pyautogui.sleep(1)
pyautogui.press('up') #방향키 up

#3. ctrl+c, ctrl+v 등의 단축키 사용
pyautogui.sleep(1)
pyautogui.press('numlock') #end키가 windows에서 Numlock 버튼에 의해 숫자1로 인식될 수 있음.
pyautogui.hotkey('shift','end') # 한줄 전체선택...

pyautogui.sleep(1)
pyautogui.hotkey('ctrl','c')  # mac os : 'command'(ctrl대신)
print('복사완료')
pyautogui.press('numlock')

pyautogui.sleep(1)
pyautogui.press('down')
pyautogui.hotkey('ctrl','v')

#4. 한글 쓰기를 위한 우회... 방법.. 클립복사 기법
#실습의 편의를 위해 메모장의 새탭을 열어서 작성 [단축키 new tab : ctrl+n]
pyautogui.sleep(2)
pyautogui.hotkey('ctrl','n')
pyautogui.sleep(1)

#한글을 복사하여 붙이는 방법.. 추가 모듈 필요 pyperclip
#영어처럼 인터벌을 주어.. 타자 써지듯이 하고 싶다면 개발자가 직접 기능을 만들어야 함.
import time
import pyperclip
def slow_type_hangul(text, interval=0.25):
    for char in text:  #문자열에서 한글자 씩...
        pyperclip.copy(char)         #한글자 복사
        pyautogui.hotkey('ctrl','v') #붙여넣기
        time.sleep(interval)

# 사용
slow_type_hangul('안녕하세요. 업무 보고를 시작합니다.', interval=0.1)
pyautogui.press('enter')
pyautogui.press('enter')

slow_type_hangul('오늘 수행한 업무 내역은 아래와 같습니다.', interval=0.1)
pyautogui.press('enter')

#업무 내역 리스트
task_done= ['대리점 압박', '물건 강매', '매출계산','순이익 숨기기']
for task in task_done:
    slow_type_hangul(task, interval=0.1)
    pyautogui.press('enter')

slow_type_hangul('-'*40, interval=0.0001)
pyautogui.press('enter')
pyautogui.press('enter')

slow_type_hangul('내일 수행할 업무 내역은 아래와 같습니다.', interval=0.1)
pyautogui.press('enter')

task_todo=['기록삭제','직원입단속']
for task in task_todo:
    slow_type_hangul(task, interval=0.01)
    pyautogui.press('enter')


