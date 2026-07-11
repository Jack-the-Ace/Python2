# 실행되는 프로그램들의 창(window)객체를 참조하여 제어하기!
# mac os 에서는 지원되지 않음.

import pyautogui

# 현재 활성화된 창의 정보 가져오기
active_window= pyautogui.getActiveWindow()

print('창의 제목:',active_window.title)
print('창의 크기:',active_window.size)
print('창의 좌표:',active_window.left, active_window.top, active_window.right, active_window.bottom)

# 마우스의 위치를 현재 활성화된 창의 좌상단에.. 옮기기
pyautogui.moveTo(active_window.left+30, active_window.top+30, duration=3)

#2. 실행되고 있는 모든 프로그램들의 윈도우 가져오기
for window in pyautogui.getAllWindows():
    print(window)
print('-'*20)

#3. 특정 title을 가진 창(윈도우)를 찾아오기 [윈도우 탐색기 [홈] ]
window=pyautogui.getWindowsWithTitle('홈')[0] #여러개 일수도 있어서 첫번째 윈도우 선택
if not window.isActive:
    print('비활성화 상태')
    window.activate()  # 활성화
    window.maximize()  # 최대화

    pyautogui.sleep(2)
    window.restore()  #원래 사이즈로 복구

    pyautogui.sleep(2)
    window.close()


