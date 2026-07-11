import smtplib
from email.message import EmailMessage
from imap_tools import MailBox
from openpyxl import Workbook
from account import EMAIL_ADDRESS, EMAIL_PASSWORD

selected_list, waiting_list = [], []

print("----수신함에서 신청 메일을 조회하는 중----")

with MailBox('imap.gmail.com', 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder='INBOX') as mailbox:
    for msg in mailbox.fetch('(SUBJECT "모의 면접 신청합니다.")', reverse=False):
        
        content= msg.text.strip()
        
        try:
            parts= [p.strip() for p in content.split('/')]
            if len(parts) == 3:
                course, name, phone = parts[0], parts[1], parts[2]
            else:
                continue
        except Exception:
            continue

        sender_email= msg.from_
        person_info= {"course":course, "name":name, "phone":phone, "email":sender_email}

        if len(selected_list) < 3:
            selected_list.append(person_info)
        else:
            waiting_list.append(person_info)

print("----결과 안내 메일을 발송합니다----")

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    




