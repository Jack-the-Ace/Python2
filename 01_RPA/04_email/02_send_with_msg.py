from account import EMAIL_ADDRESS, EMAIL_PASSWORD
import smtplib
#한글과 첨부파일등의 함께 보낼 수 있는 EmailMessage 클래스 사용
from email.message import EmailMessage

#1. 이메일 객체 생성
msg= EmailMessage()

#2. 제목/발신자 주소/수신자 주소 를 설정
msg['Subject']= '테스트 메일입니다.' #제목
msg['From']= EMAIL_ADDRESS        # 발신자 메일주소
#msg['To']= 'rmdwjdwjrz@gmail.com' #수신자 메일주소

#5. 여러명에게 전송하는 메일이라면..
mail_list= ['rmdwjdwjrz@gmail.com','rmdwjdwjrz@naver.com']
msg['To']= ", ".join(mail_list)  #파이썬의 리스트를 특정 문자 기준으로 합친 문자열

#6. 참조
#msg['Cc']= 'rocketboost.aiapp@gmail.com'  # Carbon Copy
#비밀참조
#msg['Bcc']= '2017mrhi@gmail.com'  # Blind CC

#3. 메일의 본문내용
msg.set_content('이 메일은 테스트 메일입니다. 한글도 잘 보내집니다.\n자동화된 메일 시스템 구축가능')

#4. SMTP객체를 생성하여 메일 메세지 전송
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)


