#__author__ = 'oushun'
#__date__ = '2016.5.27'

import time,cv2,os,smtplib,socket
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage  


#gain picture
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
	    time = time.strftime('%Y%m%d%H%M%S')
	    pic = cv2.imwrite(time+'.png',frame)
	    break
cap.release()

#test network
while 1:
	try:
	    socket.gethostbyname("baidu.com")
	except:
	    continue
	else:
	    break
#STMP
sender = '358984048@qq.com'  
receiver = '358984048@qq.com'  
subject = 'python email test'  
smtpserver = 'smtp.qq.com'  
username = '358984048@qq.com'  
password = '**********'  
  
msgRoot = MIMEMultipart('related')  
msgRoot['Subject'] = time 
  
## msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>good!','html','utf-8')  
msgText = MIMEText('<img src="cid:image1">','html','utf-8')  
msgRoot.attach(msgText)  
  
fp = open(time+'.png', 'rb')  
msgImage = MIMEImage(fp.read())  
fp.close()  
#You can choose to save pictures or not.
os.remove(time+'.png')
  
msgImage.add_header('Content-ID', '<image1>')  
msgRoot.attach(msgImage)  
  
smtp = smtplib.SMTP()  
smtp.connect('smtp.qq.com')  
smtp.starttls() 
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msgRoot.as_string())  
smtp.quit()  