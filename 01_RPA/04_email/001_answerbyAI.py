import smtplib
from email.message import EmailMessage
from imap_tools import MailBox
from openpyxl import Workbook
from account import EMAIL_ADDRESS, EMAIL_PASSWORD

# 데이터를 담을 리스트 준비
selected_list = []  # 선정자 명단 (최대 3명)
waiting_list = []   # 대기자 명단

# =================================================================
# STEP 1. 메일함에서 신청 메일 조회 및 선착순 분류 (IMAP)
# =================================================================
print("🔍 수신함에서 신청 메일을 조회하는 중...")

with MailBox('imap.gmail.com', 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder='INBOX') as mailbox:
    # 선착순 선정을 위해 오래된 메일부터 읽어옴 (reverse=False)
    # 제목이 '모의 면접 신청합니다.'인 메일만 필터링
    for msg in mailbox.fetch('(SUBJECT "모의 면접 신청합니다.")', reverse=False): 
        
        # 본문 텍스트 가져오기 및 공백 제거
        content = msg.text.strip()
        
        # '/' 기호로 쪼개서 [과정명, 이름, 전화번호] 추출
        try:
            parts = [p.strip() for p in content.split('/')]
            if len(parts) == 3:
                course, name, phone = parts[0], parts[1], parts[2]
            else:
                continue # 형식이 맞지 않는 메일은 패스
        except Exception:
            continue

        # 수집한 정보 딕셔너리로 저장 (발신자 메일 주소 포함)
        sender_email = msg.from_
        person_info = {"course": course, "name": name, "phone": phone, "email": sender_email}

        # 선착순 3명까지는 선정자, 그 이후는 대기자로 분류
        if len(selected_list) < 3: 
            selected_list.append(person_info)
        else:
            waiting_list.append(person_info)

# =================================================================
# STEP 2. 결과 안내 메일 자동 발송 (SMTP)
# =================================================================
print("📤 결과 안내 메일을 발송합니다...")

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    # 2-1. 선정 안내 메일 발송
    for idx, person in enumerate(selected_list, start=1):
        res_msg = EmailMessage()
        res_msg['Subject'] = "[선정] 모의 면접 신청" 
        res_msg['From'] = EMAIL_ADDRESS
        res_msg['To'] = person['email']  # 실제 환경에서는 신청자 메일로 발송
        
        body = f"{person['name']}님 축하드립니다. 모의면접 대상자로 선정되셨습니다. (선정순번 {idx}번)" 
        res_msg.set_content(body)
        smtp.send_message(res_msg)
        print(f"✅ {person['name']}님께 선정 메일 발송 완료 (순번: {idx})")

    # 2-2. 탈락(대기) 안내 메일 발송
    for idx, person in enumerate(waiting_list, start=1):
        res_msg = EmailMessage()
        res_msg['Subject'] = "[탈락] 모의 면접 신청" 
        res_msg['From'] = EMAIL_ADDRESS
        res_msg['To'] = person['email']
        
        body = f"{person['name']}님 모의 면접 대상자에 아쉽게도 선정되지 못했습니다.\n취소 인원이 발생하는 경우 연락드리겠습니다. (대기순번 {idx}번)" 
        res_msg.set_content(body)
        smtp.send_message(res_msg)
        print(f"❌ {person['name']}님께 대기 메일 발송 완료 (대기순번: {idx})")

# =================================================================
# STEP 3. 선정 명단 및 대기자 명단 엑셀 저장 (openpyxl)
# =================================================================
print("📊 결과를 엑셀 파일로 저장합니다...")

wb = Workbook()

# 첫 번째 시트: 선정자 명단
ws1 = wb.active
ws1.title = "선정자 명단" [cite: 18]
ws1.append(["순번", "과정명", "이름", "전화번호"])  # 헤더 추가
for idx, person in enumerate(selected_list, start=1):
    ws1.append([idx, person['course'], person['name'], person['phone']])

# 두 번째 시트: 대기자 명단
ws2 = wb.create_sheet(title="대기자 명단") [cite: 27]
ws2.append(["순번", "과정명", "이름", "전화번호"])  # 헤더 추가
for idx, person in enumerate(waiting_list, start=1):
    ws2.append([idx, person['course'], person['name'], person['phone']])

# 파일 저장
wb.save("모의면접_신청_결과.xlsx")
print("💾 '모의면접_신청_결과.xlsx' 파일 저장 완료!")