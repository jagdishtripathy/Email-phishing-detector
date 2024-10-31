import sqlite3

def log_flagged_email(email):
    conn = sqlite3.connect('phishing_alerts.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS flagged_emails
                      (sender TEXT, subject TEXT, body TEXT)''')

    cursor.execute("INSERT INTO flagged_emails (sender, subject, body) VALUES (?, ?, ?)",
                   (email['from'], email['subject'], email['body']))
    conn.commit()
    conn.close()
    print("Email logged.")
