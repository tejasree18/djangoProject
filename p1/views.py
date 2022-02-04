from django.shortcuts import render
from .utils.main import caesar_encrypt, playfairencrypt, transposition_encrypt
import smtplib
import math
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create your views here.
from .utils.playFairC import convertPlainTextToDiagraphs


def caesar_cip(request):
    if request.method == "POST":
        q = request.POST["q"]
        key = request.POST["key"]
        res = caesar_encrypt(q, int(key))
        return render(request, 'c.html', {'res': res})
    else:
        return render(request, 'c.html')


def playfair_cip(request):
    if request.method == "POST":
        q = request.POST["q"]
        q1 = q.replace(" ", "").upper()
        key = request.POST["key"]
        key1 = key.replace(" ", "").upper()
        convertedPlainText = convertPlainTextToDiagraphs(q1)
        res = " ".join(playfairencrypt(convertedPlainText, key1))
        return render(request, 'pf.html', {'res': res})
    return render(request, 'pf.html')


def transposition_cip(request):
    if request.method == "POST":
        q = request.POST["q"]
        key = request.POST["key"]
        key1 = int(int(key) % (len(q)))
        res = " ".join(transposition_encrypt(q, key1))
        return render(request, 't.html', {'res': res})
    else:
        return render(request, 't.html')


def send_mail(request):
    if request.method == "POST":
        msg = request.POST["message"]
        to_email_id = request.POST["to_email"]
        subject = request.POST["sub"]

        sender_email = "tejasree18102001@gmail.com"
        sender_pass = "Teja@123"

        message = MIMEMultipart()
        message['FROM'] = sender_email
        message['TO'] = to_email_id
        message['SUBJECT'] = subject

        message.attach(MIMEText(msg, "plain"))

        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_email, sender_pass)
        text = message.as_string()

        session.sendmail(sender_email, to_email_id, text)
        session.quit()

        return render(request, 'send_email.html', {'res': "Your Email is Sent Successfully"})
    return render(request, 'send_email.html')


def root(request):
    return render(request, 'root.html')


def contact(request):
    if request.method == "POST":
        msg = request.POST["message"]
        sender_email = request.POST["from_email"]
        sender_pass = request.POST["passw"]
        subject = request.POST["sub"]

        to_email_id = "tejasree18102001@gmail.com"

        message = MIMEMultipart()
        message['FROM'] = sender_email
        message['TO'] = to_email_id
        message['SUBJECT'] = subject

        message.attach(MIMEText(msg, "plain"))

        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_email, sender_pass)
        text = message.as_string()

        session.sendmail(sender_email, to_email_id, text)
        session.quit()
        return render(request, 'contact.html', {'res': "Your message is Sent Successfully"})

    return render(request, 'contact.html')
