#첨부파일과 함께 메일 전송
from account import *
import smtplib
from email.message import EmailMessage

#1. 이메일 객체 생성
msg= EmailMessage()

#2. 제목/발신자/수신자/본문내용
msg['Subject']= '첨부파일 테스트 메일이다.'
msg['From']= EMAIL_ADDRESS
msg['To']= 'rmdwjdwjrz@gmail.com'
msg.set_content('첨부파일 확인부탁')

#3. 첨부파일 전송위해 파일을 binary mode로 읽어와야함. 파일타입(mime type)을 전송할때 명시해야함
with open('./04_email/aaa.png', 'rb') as file:
    msg.add_attachment(file.read(), maintype='image', subtype='png', filename=file.name)  # (파일 데이터 bytes, MIME type(main, sub), 파일명) #마임타입 종류를 알고싶다면. 검색 mime type 검색

with open('./04_email/aaa.pdf', 'rb') as file:
    msg.add_attachment(file.read(), maintype='application', subtype='pdf', filename=file.name)

with open('./04_email/aaa.xlsx', 'rb') as file:
    msg.add_attachment(file.read(), maintype='appication', subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename=file.name)
    # or
    #msg.add_attachment(file.read(), maintype='application', subtype='octet-stream', filename=file.name)

#4. SMTP 객체를 생성하여 이메일 메세지 전송
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)

