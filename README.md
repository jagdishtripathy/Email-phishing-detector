Phishing Email Detector with Automated Quarantine and Alert System
==================================================================

This project is an automated tool for detecting, quarantining, and alerting about suspicious phishing emails. It integrates with the VirusTotal API to scan URLs found in emails, flags potential phishing threats, quarantines them, and notifies the security team.

Table of Contents
-----------------

-   [Features](#features)
-   [Requirements](#requirements)
-   [Setup Instructions](#setup-instructions)
-   [Configuration](#configuration)
-   [Usage](#usage)
-   [Project Files](#project-files)
-   [Disclaimer](#disclaimer)
-   [License](#license)

* * * * *

Features
--------

-   **Automated Email Scanning**: Fetches unread emails and scans their content for suspicious URLs.
-   **Phishing Detection**: Uses VirusTotal API to check for malicious URLs in email bodies.
-   **Email Quarantine**: Flags and moves potentially harmful emails to quarantine.
-   **Alert System**: Sends an alert email to notify the security team of any phishing attempt.
-   **Logging**: Logs flagged emails for record-keeping and review.

Requirements
------------

-   Python 3.6+
-   Required packages:
    -   `requests` for API calls
    -   `imaplib` and `email` for email handling
    -   `re` and `base64` for URL extraction and encoding
-   A VirusTotal API key for URL analysis.

Setup Instructions
------------------

1.  **Clone the Repository**:

    bash

    Copy code

    `git clone https://github.com/jagdishtripathy/Phishing-Email-Detector.git
    cd Phishing-Email-Detector`

2.  **Create a Virtual Environment** (optional but recommended):

    bash

    Copy code

    `python3 -m venv myenv
    source myenv/bin/activate  # On Windows, use myenv\Scripts\activate`

3.  **Install Required Packages**:

    bash

    Copy code

    `pip install requests`

4.  **Configure Email and VirusTotal API**: Update `email_handler.py` with your email login credentials and IMAP server:

    python

    Copy code

    `EMAIL_ADDRESS = 'your_email@example.com'
    EMAIL_PASSWORD = 'your_password'
    IMAP_SERVER = 'imap.example.com'`

    Update `phishing_detection.py` with your VirusTotal API key:

    python

    Copy code

    `api_key = 'your_virustotal_api_key'`

Configuration
-------------

In the `email_handler.py` file, configure the following:

-   `EMAIL_ADDRESS`: Your email address for accessing the mailbox.
-   `EMAIL_PASSWORD`: Your email account password or app-specific password.
-   `IMAP_SERVER`: IMAP server address (e.g., `imap.gmail.com` for Gmail).

In `phishing_detection.py`:

-   `api_key`: VirusTotal API key for checking URLs.

Usage
-----

To run the project, execute `main.py`:

bash

Copy code

`python main.py`

The program will:

1.  Connect to the email inbox and fetch unread emails.
2.  Check each email's content for URLs and scan them using VirusTotal.
3.  Quarantine flagged phishing emails.
4.  Send an alert email to the security team.
5.  Log details of flagged emails.

Project Files
-------------

-   `main.py`: The main script that runs the program.
-   `email_handler.py`: Handles email connection and fetching.
-   `phishing_detection.py`: Scans email URLs via the VirusTotal API.
-   `quarantine.py`: Manages email quarantine actions.
-   `alert.py`: Sends alerts to the security team.
-   `logger.py`: Logs flagged emails.

Disclaimer
----------

This tool is intended for educational purposes and to improve security awareness. Ensure you have permission before scanning email accounts. Misuse of this tool for unauthorized access or phishing detection without permission may violate legal guidelines.

License
-------

This project is licensed under the MIT License.
