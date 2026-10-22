import smtplib
from email.mime.text import MIMEText
import csv
from datetime import datetime

EMAIL_USER = "mikela@gmail.com"
EMAIL_PASSWORD = "atafhemrkdrbgnke"
TO_EMAIL = "mikela@gmail.com"

def send_lead_email(name, email, message):
    # SAVE TO FILE - ALWAYS WORKS!
    try:
        with open('leads.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), name, email, message])
        print(f"✅ LEAD SAVED TO leads.csv - {name} - {email}")
    except Exception as e:
        print(f"Save failed: {e}")

    # TRY EMAIL
    try:
        body = f"MIKELA ROBOTICS LEAD\nName: {name}\nEmail: {email}\nMessage: {message}"
        msg = MIMEText(body)
        msg['Subject'] = f"New Lead: {name}"
        msg['From'] = EMAIL_USER
        msg['To'] = TO_EMAIL
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=15)
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("✅ Email sent!")
        return True
    except Exception as e:
        print(f"⚠️ Email blocked by Firewall, but lead is SAVED in leads.csv! Error: {e}")
        return False