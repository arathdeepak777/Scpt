import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(mailhost, username, password, from_addr, to_addrs, subject, body):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = ", ".join(to_addrs)
    msg['Subject'] = subject

    # Attach the email body as plain text
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Establish connection with the SMTP server
        with smtplib.SMTP(mailhost) as server:
            server.starttls()  # Upgrade the connection to secure (TLS)
            server.login(username, password)  # Login with username and password
            server.sendmail(from_addr, to_addrs, msg.as_string())  # Send email

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    if len(sys.argv) < 6:
        print("Usage: python send_email.py <mailhost:port> <username> <password> <from_addr> <to_addr> <subject> <body>")
        sys.exit(1)

    # Parse command-line arguments
    mailhost = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    from_addr = sys.argv[4]
    to_addrs = sys.argv[5].split(',')  # Split the comma-separated email addresses into a list
    subject = sys.argv[6] if len(sys.argv) > 6 else "Test Subject"  # Default subject if not provided
    body = sys.argv[7] if len(sys.argv) > 7 else "Test Body"  # Default body if not provided

    # Send the email
    send_email(mailhost, username, password, from_addr, to_addrs, subject, body)

if __name__ == "__main__":
    main()
