import requests
import base64
import re

def check_url_virustotal(email_body):
    api_key = " " #Add your virustotal API key
    urls = re.findall(r'https?://[^\s]+', email_body)  # Extract URLs

    for url in urls:
        url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
        headers = {"x-apikey": api_key}
        response = requests.get(f"https://www.virustotal.com/api/v3/urls/{url_id}", headers=headers)

        if response.status_code == 200:
            result = response.json()
            print("VirusTotal Analysis Result:", result)  # Print the result for debugging

            # Check for malicious indicators
            if result.get('data', {}).get('attributes', {}).get('last_analysis_stats', {}).get('malicious', 0) > 0:
                return True  # Flagged as phishing

    return False  # No phishing detected

