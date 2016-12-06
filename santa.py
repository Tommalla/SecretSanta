# Tomasz [Tommalla] Zakrzewski, 2016
# Secret Santa
import copy
import email
import getpass
import random
import re
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def matching_ok(people, targets):
    for person, target in zip(people, targets):
        if person == target:
            return False
    return True


def mail_auth():
    user = input('Gmail username:')
    password = getpass.getpass()
    smtp_host = 'smtp.gmail.com'
    smtp_port = 465
    server = smtplib.SMTP_SSL(smtp_host, smtp_port)
    server.ehlo()
    server.login(user, password)
    return (user, server)


def send_mail(server, user, to, message):
    tolist = [to]
    sub = 'Secret Santa'

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = email.utils.COMMASPACE.join(tolist)
    msg['Subject'] = sub
    msg.attach(MIMEText(message))
    server.sendmail(user, tolist, msg.as_string())


def main():
    if len(sys.argv) != 3:
        print('Bad argument count. Usage:\n\tpython santa.py <names list file> <mail template file>')
        return -1
    list_filename = sys.argv[1]
    template_filename = sys.argv[2]
    people = open(list_filename).read().splitlines()
    template = open(template_filename).read()

    targets = copy.deepcopy(people)

    random.shuffle(targets)
    while not matching_ok(people, targets):
        random.shuffle(targets)

    print('Finished shuffling, sending emails...')

    user, server = mail_auth()
    total_people = len(people)
    idx = 1
    for person, target in zip (people, targets):
        print('%d/%d' % (idx, total_people))
        idx += 1
        regex = r'(\w+) ([a-zA-z ]+) ([^@]+@[^@]+)'
        m_person = re.match(regex, person)
        m_target = re.match(regex, target)
        person_firstname = m_person.group(1)
        person_mail = m_person.group(3)
        target_fullname = m_target.group(1) + ' ' + m_target.group(2)
        rendered_template = template.replace('<PERSON_FIRSTNAME>', person_firstname)\
                                    .replace('<TARGET_NAME>', target_fullname)
        send_mail(server, user, person_mail, rendered_template)

    server.quit()


if __name__ == '__main__':
    main()