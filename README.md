# Phishing Email Detector with Automated Quarantine and Alert System

This project is an automated tool for detecting, quarantining, and alerting about suspicious phishing emails. It integrates with the VirusTotal API to scan URLs found in emails, flags potential phishing threats, quarantines them, and notifies the security team.

---

## Table of Contents

- [Features](#features)

- [Requirements](#requirements)

- [Setup Instructions](#setup-instructions)

- [Configuration](#configuration)

- [Usage](#usage)

- [Project Files](#project-files)

- [Disclaimer](#disclaimer)

- [License](#license)

---

## Features

- **Automated Email Scanning**: Fetches unread emails and scans their content for suspicious URLs.

- **Phishing Detection**: Uses VirusTotal API to check for malicious URLs in email bodies.

- **Email Quarantine**: Flags and moves potentially harmful emails to quarantine.

- **Alert System**: Sends an alert email to notify the security team of any phishing attempt.

- **Logging**: Logs flagged emails for record-keeping and review.

---

## Requirements

- Python 3.6+

- Required packages:

- `requests` -- for API calls

- `imaplib` and `email` -- for email handling

- `re` and `base64` -- for URL extraction and encoding

- A VirusTotal API key for URL analysis

---

## Setup Instructions

1\. **Clone the Repository**:

```bash

    git clone https://github.com/jagdishtripathy/Email-phishing-detector.git
    cd Email-phishing-detector
```

2\. **Create a Virtual Environment** (optional but recommended):

```bash
    python3 -m venv myenv
    source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

3\. **Install Required Packages**:

```bash
    pip install requests

```

4\. **Configure Email and VirusTotal API**:

   Update `email_handler.py`:

```python

    EMAIL_ADDRESS = 'your_email@example.com'
    EMAIL_PASSWORD = 'your_password'
    IMAP_SERVER = 'imap.example.com'

```

   Update `phishing_detection.py`:

```python

    api_key = 'your_virustotal_api_key'

```

---

## Configuration

In `email_handler.py`, set:

- `EMAIL_ADDRESS`: Your email address

- `EMAIL_PASSWORD`: Your email account password or app-specific password

- `IMAP_SERVER`: IMAP server address (e.g., `imap.gmail.com` for Gmail)

In `phishing_detection.py`, set:

- `api_key`: Your VirusTotal API key

---

## Usage

To run the project, execute:

```bash

python main.py
```
The program will:

1.  Connect to the email inbox and fetch unread emails.

2.  Check each email's content for URLs and scan them using VirusTotal.

3.  Quarantine flagged phishing emails.

4.  Send an alert email to the security team.

5.  Log details of flagged emails.

* * * * *

Project Files
-------------

-   `main.py` -- Orchestrates the overall detection process

-   `email_handler.py` -- Handles email connection and fetching

-   `phishing_detection.py` -- Uses VirusTotal to scan URLs

-   `quarantine.py` -- Moves flagged emails to quarantine

-   `alert.py` -- Sends alert emails

-   `logger.py` -- Logs flagged email details

* * * * *

Disclaimer
----------

This tool is intended for educational and security awareness purposes only. Ensure you have appropriate permission before scanning any email account. Unauthorized usage may violate legal or ethical guidelines.

* * * * *

