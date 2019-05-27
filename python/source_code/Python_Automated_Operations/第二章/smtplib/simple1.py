import smtplib
import string
 
HOST = "smtp.gmail.com"
SUBJECT = "Test email from Python"
TO = "test@qq.com"
FROM = "test@gmail.com"
text = "Python rules them all!"
BODY = string.join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT ,
        "",
        text
        ), "\r\n")
server = smtplib.SMTP()
server.connect(HOST,"25")
server.starttls()
server.login("test@gmail.com","123456")
server.sendmail(FROM, [TO], BODY)
server.quit()
