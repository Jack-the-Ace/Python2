# 알림창을 띄우는 기능

import pyautogui

#카운트 다운 기능
pyautogui.countdown(3) #터미널창에 3 2 1 ... 이 표시됨

#1. 간단한 다이얼로그
pyautogui.alert('This is alert dialog','경고') #메시지, 제목

#2. 사용자 선택 다이얼로그 [확인]/[취소]
answer= pyautogui.confirm('파일 탐색기를 여시겠습니까?','선택')
print(answer)  # OK or Cancel

#3. 사용자 입력 다이얼로그
age= pyautogui.prompt('나이를 입력하세요','나이 입력')
print(age)

#3.1 비밀번호 입력 다이얼로그
pw=pyautogui.password('암호입력!')
print(pw)
#-------------------------------------------------------------------------------------------------------------------------

#4. 파일 탐색기(explorer)를 실행하기 [단축키: win+e]
pyautogui.hotkey('win','e')

import time
time.sleep(1)  #탐색기 열릴때까지 잠시 대기

# 특정 폴더로 이동 - 주소창을 클릭하거나.. 단축키로 주소 입력
pyautogui.hotkey('alt','d')
pyautogui.write('C:/Users/Public/Documents')
pyautogui.press('enter')
time.sleep(2)

#[수행과제]  '문서' 폴더 안에 특정 파일 형식의 파일을 찾아서 클릭하여 실행되도록.. [ locateAllOnScreen() 기능 필요 ]
print("화면에서 파일 아이콘을 찾는 중...")

try:
    # 1. 우선 A 이미지('./02_desktop/capture_img_icon.png')를 먼저 찾습니다.
    file_positions = list(pyautogui.locateAllOnScreen('./02_desktop/capture_img_icon.png'))
    
    # 2. 만약 A 이미지를 찾지 못했다면(개수가 0개라면)?
    if len(file_positions) == 0:
        print("A 이미지를 찾지 못해 B 이미지로 다시 검색합니다...")
        # 💡 B 이미지 경로를 넣어줍니다 (예시: capture_img_icon2.png)
        file_positions = list(pyautogui.locateAllOnScreen('./02_desktop/capture_txt_icon.png'))

    # 3. 최종적으로 (A든 B든) 찾았는지 검사합니다.
    if len(file_positions) == 0:
        print("화면에서 A와 B 이미지 모두 찾지 못했습니다.")
        pyautogui.alert("파일 아이콘을 찾지 못했습니다. 이미지를 확인해 주세요.")
    else:
        print(f"총 {len(file_positions)}개의 파일을 찾았습니다. 순서대로 실행합니다.")
        
        # 4. 찾은 아이콘들의 위치를 하나씩 꺼내어 더블클릭합니다.
        for pos in file_positions:
            center_x, center_y = pyautogui.center(pos)
            
            pyautogui.moveTo(center_x, center_y, duration=0.5)
            pyautogui.doubleClick()
            
            time.sleep(1.5)  # 파일이 실행되는 동안 대기
            
except Exception as e:
    print(f"에러가 발생했습니다: {e}")
