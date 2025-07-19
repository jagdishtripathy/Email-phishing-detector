import smtplib
from email.mime.text import MIMEText

def send_alert_email(subject, message):
    smtp_server = smtp.gmail.com  # Replace with your SMTP server
    smtp_port = 587
    alert_email =   # Replace with sender email
    alert_password =   # Replace with sender password

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = alert_email
    msg['To'] =  # Replace with security team email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(alert_email, alert_password)
        server.sendmail(alert_email,"Add here your alert email", msg.as_string())  #Remove the all the things from the double coat and add your alert email
    print("Alert email sent.")
