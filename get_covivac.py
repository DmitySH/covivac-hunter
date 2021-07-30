import smtplib


def send_mail(sender, password, recipient, subject, text):
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_obj.starttls()
    message = "Subject: {}\n\n{}".format(subject, text)
    smtp_obj.login(sender, password)
    smtp_obj.sendmail(sender, recipient, message)
    smtp_obj.quit()


if __name__ == '__main__':
    send_mail('emailsender9221@gmail.com', 'alexei4!!', 'di.im2015@yandex.ru',
              'testTitle', 'testemessage')