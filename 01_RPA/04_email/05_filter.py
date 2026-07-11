# 특정 조건의 메일만 필터링하여 읽기

from imap_tools import MailBox
from account import *

# with 와 함께하면 logout() 알아서
with MailBox('imap.gmail.com', 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder='INBOX') as mailbox:
    #전체 메일 가져오기(메일이 너무 많으면 읽어올때 시간이 오래걸림. limit=20으로 제한)
    # for msg in mailbox.fetch(limit=20):
    #     print(f'보낸사람: {msg.from_} - 제목: {msg.subject}')

    #읽지않은 메일만 가져오기
    # for msg in mailbox.fetch('(UNSEEN)', limit=10): #정해진 글자 (UNSEEN)
    #     print(f'보낸사람: {msg.from_} - 제목: {msg.subject}')

    #특정인이 보낸 메일만 가져오기
    # for msg in mailbox.fetch('(FROM rmdwjdwjrz@gmail.com)', limit=10): #정해진 글자 (FROM 발신자)
    #     print(f'보낸사람: {msg.from_} - 제목: {msg.subject}')

    # #(제목, 본문)에 특정 문자열이 포함된 메일만 가져오기
    # for msg in mailbox.fetch('(TEXT "test mail")', limit=10): #정해진 글자 (TEXT "문자열") <-- 반드시 큰따옴표만
    #     print(f'보낸사람: {msg.from_} - 제목: {msg.subject}')

    #제목에만 특정 문자열이 포함된 메일만 가져오기 -- 한글은 안됨. 영어만 찾아짐.
    # for msg in mailbox.fetch('(SUBJECT "test")', limit=10, reverse=True): #정해진 글자 (SUBJECT "문자열") <-- 반드시 큰따옴표만
    #     print(f'보낸사람: {msg.from_} - 제목: {msg.subject}')

    #한글로 검색되게 하려면.. 전체메일을 가져온 후 반복문으로 코드를 구현
    # for msg in mailbox.fetch(limit=10, reverse=True):
    #     if "테스트" in msg.subject:
    #         print(f'보낸사람: {msg.from_} - 제목: {msg.subject}')

    # 특정 날짜 이후에 수신된 메일만 가져오기
    # for msg in mailbox.fetch('(SENTSINCE 01-Jul-2026)', limit=10, reverse=True):
    #     print(f'보낸사람: {msg.from_} - 제목: {msg.subject}')

    # 특정 날짜에 수신된 메일만 가져오기
    # for msg in mailbox.fetch('(ON 08-Jul-2026)', limit=10, reverse=True):
    #     print(f'보낸사람: {msg.from_} - 제목: {msg.subject}')

    # 2개 이상의 조건을 사용해야 할 때. 열거하면 됨
    # 특정 날짜에 특정인으로부터 수신된 메일만 가져오기
    # for msg in mailbox.fetch('(ON 08-Jul-2026 FROM rmdwjdwjrz@gmail.com)', limit=10, reverse=True):
    #     print(f'보낸사람: {msg.from_} - 제목: {msg.subject}')

    # 2개 중 하나이상의 조건을 만족할 때. OR ...
    # 안붙이면 AND이고, OR 붙이면 OR
    for msg in mailbox.fetch('(OR ON 08-Jul-2026 FROM rmdwjdwjrz@gmail.com)', limit=10, reverse=True):
        print(f'보낸사람: {msg.from_} - 제목: {msg.subject}')

# time 모듈을 이용하여 특정 날짜의 미국 약어 표시 만들 수 있음.
import time
print(time.strftime('%d-%b-%Y'))  # %b = month의 약어 표기(Abbreviated:약어)
print(time.strftime('%a'))  # %a = 요일 약어

