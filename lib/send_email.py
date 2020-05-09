import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from config.config import *
import logging

def send_email(report_file):
    msg = MIMEMultipart()
    msg.attach(MIMEText(open(report_file, encoding='utf-8').read(), 'html', 'utf-8'))

    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = Header(subject, 'utf-8')

    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename = "{}"'.format(report_file)
    msg.attach(att1)

    try:
        mails = smtplib.SMTP_SSL(smtp_server, 465)
        mails.login(smtp_user, smtp_password)
        mails.sendmail(sender, receiver, msg.as_string())
        logging.info("邮件发送完成！")
    except Exception as e:
        logging.error(str(e))
    finally:
        mails.quit()
