from email_handler import Class_eMail

To_Email_ID = "pankaj_suthar@persistent.co.in"

email = Class_eMail()
email.send_Text_Mail(To_Email_ID, 'Plain Text Mail Subject', 'This is sample plain test email body.')
del email

email = Class_eMail()
email.send_HTML_Mail(To_Email_ID, 'HTML Mail Subject', '<html><h1>This is sample HTML test email body</h1></html>')
del email