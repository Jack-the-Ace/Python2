import pyautogui 

#1. 현재 화면을 스크린샷을 찍어서 이미지로 저장
img= pyautogui.screenshot()
img.save('./02_desktop/aaa.png')

#2. 특정 범위를 캡쳐하기
img2= pyautogui.screenshot(region=(70, 120, 200, 100))  # left, top, width, height
img2.save('./02_desktop/bbb.png')

#3. 듀얼모니터를 사용한다면..
img3= pyautogui.screenshot(allScreens=True)
img3.save('./02_desktop/ccc.png')
