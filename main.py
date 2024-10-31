from email_handler import connect_to_email, fetch_emails
from phishing_detection import check_url_virustotal
from quarantine import quarantine_email
from alert import send_alert_email
from logger import log_flagged_email

def run():
    # Connect to the email server
    mail = connect_to_email()  
    
    # Fetch unread emails
    emails = fetch_emails(mail)  
    
    # Print the fetched emails
    if not emails:
        print("No unread emails found.")
    else:
        for email in emails:
            print(f"From: {email['from']}")
            print(f"Subject: {email['subject']}")
            print(f"Body: {email['body']}\n")  # Print the body content
            
            # Check if the email body contains a phishing URL
            if check_url_virustotal(email['body']):
                quarantine_email(mail, email['id'])  # Quarantine the email
                send_alert_email("Phishing Alert", "Suspicious email detected and quarantined.")  # Send alert
                log_flagged_email(email)  # Log the flagged email

if __name__ == "__main__":
    run()

