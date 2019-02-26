#!/usr/bin/env python
# -*- coding: utf-8 -*-



######################################## 
"""LIBRARIES"""
import sys
import subprocess
import smtplib
import time
import cgi
import uuid
import os

from subprocess import check_output
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEImage import MIMEImage
from email.mime.image     import MIMEImage
from email.mime.application import MIMEApplication
from email.header         import Header

######################################## 
delayTime=6
######################################## 
"""EMAIL SETTINGS"""
sender = 'Empresa <empresa@email.com>'
#sender = 'Mi nombre <correo@gmail.com>'

fileToSend=str(sys.argv[1])

with open(fileToSend) as f:
    content = f.read()  
    linex = content.split('\n')


for i in range(len(linex)):
    print(linex[i])
    dataz = linex[i].split('|')
    #Nombre
    nombre=str(dataz[0])
    #Correo
    receiver=str(dataz[1])
    

    courseImgmd="./logo.png"


    ######################################## 
    imgLogo  = dict(title=u'Imagen 1', path=courseImgmd, cid=str(uuid.uuid4()))
    

    #Declare MSG
    msg = MIMEMultipart('related')
    
    #
    msg['Subject'] =str("Subjec del correo").decode('utf-8')
    msg['From'] = sender
    msg['Reply-to'] = sender
    msg['Return-Path'] = sender
    msg['To'] = receiver



    msg_alternative = MIMEMultipart('alternative')
    msg.attach(msg_alternative)
    msg_text  = MIMEText(u'[image: {title}]'.format(**imgLogo), 'plain', 'utf-8')
    msg_alternative.attach(msg_text)

   

    msg_html2=MIMEText('<div>'
'<img height="60px" onerror="this.src=\'https://es.wikipedia.org/wiki/Logo_de_Google#/media/File:Google_2015_logo.svg\';" src="cid:image1" alt="Logo" >'
'<p>Estimado(a)'+nombre+'</p>'
'<p>Aka va el texto completo en HTML</p>'
'</div>','html', 'utf-8')

    

    msg_alternative.attach(msg_html2)

    with open(imgLogo['path'], 'rb') as file:
        msg_image = MIMEImage(file.read(), name=os.path.basename(imgLogo['path']))
        msg.attach(msg_image)
    msg_image.add_header('Content-ID', '<image1>'.format(imgLogo['cid']))

######################################## 





    ##START SERVER

    """GMAIL"""
    
    username = 'user@gmail.com'
    password = '*********'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    
    """SMTP"""
    #username = 'user@empresa.com'
    #password = '******'
    #server = smtplib.SMTP('mail.empresa.com:25')


    server.login(username,password)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()
    time.sleep( delayTime )