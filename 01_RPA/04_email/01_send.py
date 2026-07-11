#이메일 전송 자동화 - google gmail 로 실습
#이메일 전송하려면 로그인이 필요함. 단, 앱에서 로그인하는 [앱 비밀번호]를 이용 ~ 보안수준이 낮은 16자리 비밀번호

# 구글 계정으로 로그인 후 설정 필요
# [계정관리] 버튼을 누르면.. 페이지의 좌측에 [보안 및 로그인] 메뉴 선택 ~2단계 인증 되어있어야 함.
# 상단 검색창에 '앱 비밀번호'를 검색하면 앱 비밀번호 생성 페이지가 열림
# 이 앱만의 고유한 번호를 발급받기 ~16자리 글씨들
# 이메일 주소와 앱비밀번호를 별도의 account.py 파일에 변수로 저장하고 import 하여 사용 권장

from account import EMAIL_ADDRESS, EMAIL_PASSWORD

#이메일 전송을 위한 규약 : smtp [simple mail transfer protocol]
#이 규약을 이용하여 이메일을 전송해주는 파이썬의 표준모듈 smtplib
import smtplib

#SMTP 객체를 생성하여 메일 전송작업 수행 (메일 서버명, 포트번호)
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()  # 연결이 잘 되었는지 확인 [extended Hello]
    smtp.starttls()  # 모든 내용은 암호화 해서 전송 - tls [transport layer security]
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    #메일의 제목, 내용
    subject= "TEST RPA EMAIL"  # 한글안됨
    body= "this is rpa test mail." # 메일 본문

    #이메일을 보내는 정해진 형식 "Subject: 제목\n내용"
    message=f"Subject: {subject}\n{body}"
    smtp.sendmail(EMAIL_ADDRESS, "rmdwjdwjrz@gmail.com",message)   # 발신자 메일, 수신자 메일, 메세지(제목,내용)

