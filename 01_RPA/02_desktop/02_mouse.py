import pyautogui

#1. 특정 위치로 마우스 커서를 이동
#pyautogui.moveTo(100,100)  그냥 팍 이동...

#2. 이동하는데 시간을 걸리도록..
#pyautogui.moveTo(100,100, duration=3) # 3초 동안 해당 위치로 이동

#3. 상대좌표로 이동
pyautogui.moveTo(200,200,duration=1)
pyautogui.move(20,20, duration=0.25) #현재위치 기준.. 20,20, 이동
pyautogui.move(-20,20, duration=0.25) #현재위치 기준.. 20,20, 이동
pyautogui.move(-20,-20, duration=0.25) #현재위치 기준.. 20,20, 이동
pyautogui.move(-20,-20, duration=0.25) #현재위치 기준.. 20,20, 이동
#pyautogui.move(20,20, duration=0.25) #현재위치 기준.. 20,20, 이동

#현재 마우스 좌표 출력해보기
print(pyautogui.position()) #Point(x=000, y=000)
pos= pyautogui.position()
print('x축 좌표: ', pos[0])
print('y축 좌표: ', pos[1])
print('x축 좌표: ', pos.x)
print('y축 좌표: ', pos.y)

#해당 좌표를 클릭
#pyautogui.click()

# 특정 위치로 가서 클릭하시오..
# pyautogui.click(26,191, duration=3)

# 클릭의 횟수 지정
#pyautogui.click()

#pyautogui.click(151,156, duration=2, clicks=3)

#클릭횟수 지정에 제한은 없음.. 그래서.. 그림판에 점선 그려보기
# pyautogui.sleep(5)  # 5초간 동작을 멈추기 (멈춘 사이에 그림판 앱을 실행)
# pyautogui.click(clicks=500)

# 마우스 우클릭
# pyautogui.moveTo(500,500,duration=1)
# pyautogui.rightClick()

#마우스 드래그
pyautogui.moveTo(600,500,duration=1)
# pyautogui.drag(100,10,duration=2)    #상대죄표
pyautogui.dragTo(700,550,duration=2)  #절대좌표

#마우스 스크롤
pyautogui.scroll(600) #양수면 위로.. 음수면 아래로... (픽셀사이즈 아님)