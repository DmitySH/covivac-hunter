import re
import smtplib
from bs4 import BeautifulSoup
import requests
import time


def send_mail(sender, password, recipient, subject, text):
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_obj.starttls()
    message = "Subject: {}\n\n{}".format(subject, text)
    smtp_obj.login(sender, password)
    smtp_obj.sendmail(sender, recipient, message)
    smtp_obj.quit()


if __name__ == '__main__':
    headers = {
        'Accept': '*/*',
        'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
    url = 'https://www.mos.ru/city/projects/covid-19/privivka/'
    time_online = 0

    while True:
        if time_online % 1440 == 0:
            send_mail('emailsender9221@gmail.com', 'alexei4!!', 'di.im2015@yandex.ru',
                      'Online', 'Still online')
        try:
            req = requests.get(url, headers=headers)
            src = req.text
            soup = BeautifulSoup(src, 'lxml')
            vaccine_info = soup.find(text=re.compile('нет в наличии'))
            if not vaccine_info:
                for i in range(4):
                    send_mail('emailsender9221@gmail.com', 'alexei4!!', 'di.im2015@yandex.ru',
                              'Covivac', 'Something happened!')
        except Exception as ex:
            send_mail('emailsender9221@gmail.com', 'alexei4!!', 'di.im2015@yandex.ru',
                      'Exception', 'Something went wrong!')
        time.sleep(1800)
        time_online += 30