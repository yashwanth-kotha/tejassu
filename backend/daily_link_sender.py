import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
import datetime
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get credentials from environment variables
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

def send_link():
    # Setting up the email
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = "Your Daily Link for writing Journal"

    # Create the body of the email
    link = "https://chatgpt.com/g/g-6749268985ac8191b2e72f40f9e64f08-journal*"
    body = f"Hello! Here is your link for today: {link}\nDate: {datetime.date.today()}"
    msg.attach(MIMEText(body, 'plain'))

    # Sending the email everyday at 8:30 PM
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Schedule the send_link function at 9:00 PM every day
schedule.every().day.at("20:30").do(send_link)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute
