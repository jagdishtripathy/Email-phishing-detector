def quarantine_email(mail, email_id):
    mail.create('Quarantine')  # Create 'Quarantine' folder if it doesn't exist
    mail.store(email_id, '+X-GM-LABELS', 'Quarantine')  # Moves the email (Gmail-specific)
    print(f"Email {email_id} moved to Quarantine.")
