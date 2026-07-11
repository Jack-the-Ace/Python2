# 메일박스 수신함(Inbox)을 접근하는 외부모듈 설치
# pip install imap-tools

from account import *
from imap_tools import MailBox

#1. 메일박스를 읽어오기 위한 객체 생성
mailbox=MailBox('imap.gmail.com', 993) # IMAP port번호 [Internet Mail Access Protocol]
#2. 로그인, 특정 수신함을 열기
mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder='INBOX')

#3. 메일함에서 최신순(reverse=True)으로 메세지를 읽어오기. 일단. 1개만...
for msg in mailbox.fetch(limit=1, reverse=True):
    print('제목: ', msg.subject)
    print('발신자: ', msg.from_)  # 변수명에 _있음
    print('수신자: ', msg.to)
    print('참조: ', msg.cc)
    print('비밀참조: ', msg.bcc)
    print('수신날짜: ', msg.date)  # 시간대가 구글이어서 미국시간일 수 있음. (서버에 저장된 시간)
    print('본문내용: ', msg.text)
    print('HTML 메세지: ', msg.html)
    print('='*40)

    #혹시 첨부파일이 있다면 자동으로 다운로드 되도록...
    for file in msg.attachments:
        #원본파일명에 경로이름이 써있음. 분리
        path= file.filename.split('/')
        name= path[len(path)-1]

        print('첨부파일명:', name)
        print('첨부타입:', file.content_type)
        print('파일크기:', file.size, "bytes")

        with open('./04_email/rpa_mail_download_'+name, 'wb') as f:
            f.write(file.payload)
            print('첨부파일 {} 다운로드 완료'.format(name))
        print("~"*30)

#4. 메일박스에서 로그아웃
mailbox.logout()
