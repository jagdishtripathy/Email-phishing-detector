import imaplib
import email

# Configuration
EMAIL_ADDRESS = ''   # Replace with your email
EMAIL_PASSWORD = ''           # Replace with your password or app-specific password
IMAP_SERVER = 'imap.gmail.com'           # Replace with your email provider's IMAP server

def connect_to_email():
    # Connect to the IMAP server and log in
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    return mail

def fetch_emails(mail):
    mail.select("inbox")
    result, data = mail.search(None, "UNSEEN")
    
    email_ids = data[0].split()
    emails = []
    
    for email_id in email_ids:
        result, msg_data = mail.fetch(email_id, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        email_info = {
            'from': msg['From'],
            'subject': msg['Subject'],
            'body': ""
        }

        # Check if the message has a payload
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    email_info['body'] = part.get_payload(decode=True).decode() if part.get_payload(decode=True) else ""
                    break
        else:
            # Handle non-multipart messages
            email_info['body'] = msg.get_payload(decode=True).decode() if msg.get_payload(decode=True) else ""
        
        emails.append(email_info)
    
    return emails

