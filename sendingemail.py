import smtplib
import subprocess
import datetime
import time


ip_get_old = ""

while (1):

	ip_get = subprocess.Popen("curl ifconfig.co", shell=True, stdout=subprocess.PIPE).stdout.read()
	print ip_get
	if (ip_get != ip_get_old):
		ip_get_old = ip_get 
		body = ip_get + "\n AT TIME: " + str(datetime.datetime.now())
		gmail_user = "w@gmail.com"  
		gmail_password = "password"
		from1 = "w@gmail.com"
		to = "w@gmail.com" 
		subject = "IP UPDATE"  
		#email_text = "hello world"

		email_text = "\r\n".join([
			"From: w@gmail.com",
			"To: w@gmail.com",
			"Subject: IP UPDATE",
			"",
			body
			])

		try:  
		    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		    server.ehlo()
		    server.login(gmail_user, gmail_password)
		    server.sendmail(from1, to, email_text)
		    server.close()

		    print 'Email sent!'
		except:  
		    print 'Something went wrong...'

	else:
		print "IP is no change"
	print datetime.datetime.now()
	time.sleep(900);
