import smtplib
import time
from email.message import EmailMessage
from account import EMAIL_ADDRESS, EMAIL_PASSWORD

apply_list= [
    {"course":"aix", "name":"손흥민", "phone":"1234"},
    {"course":"web", "name":"김민재", "phone":"5678"},
    {"course":"aix", "name":"류현진", "phone":"1111"},
    {"course":"aix", "name":"박찬호", "phone":"2222"},
    {"course":"web", "name":"김연아", "phone":"3333"},
    {"course":"design", "name":"박세리", "phone":"4444"}
]

print("신청 메일 6건 발송을 시작합니다...")

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for person in apply_list:
        msg= EmailMessage()
        msg['Subject']= "모의 면접 신청합니다."
        msg['From']= EMAIL_ADDRESS
        msg['To']= EMAIL_ADDRESS

        msg.set_content(f"{person['course']} / {person['name']} / {person['phone']}")
        smtp.send_message(msg)
        print(f"{person['name']}님의 신청 메일 발송 완료!")

        time.sleep(0.5)

print("---- 테스트용 메일 발송 작업이 완료되었습니다. ----")
