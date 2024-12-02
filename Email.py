import smtplib
import sys
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def send_email(mailhost, username, password, from_addr, to_addrs, subject, body):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = ", ".join(to_addrs)
    msg['Subject'] = subject

    # Attach the email body as plain text
    msg.attach(MIMEText(body, 'plain'))

    try:
        logger.debug(f"Connecting to SMTP server: {mailhost}")
        # Establish connection with the SMTP server
        with smtplib.SMTP(mailhost) as server:
            server.set_debuglevel(1)  # Enable debug mode (verbose communication with SMTP)
            logger.debug("Starting TLS encryption")
            server.starttls()  # Upgrade the connection to secure (TLS)
            logger.debug("Logging in to SMTP server")
            server.login(username, password)  # Login with username and password
            logger.debug("Sending email")
            server.sendmail(from_addr, to_addrs, msg.as_string())  # Send email

        logger.info("Email sent successfully!")

    except Exception as e:
        logger.error(f"Failed to send email: {e}")

def main():
    if len(sys.argv) < 6:
        logger.error("Usage: python send_email.py <mailhost:port> <username> <password> <from_addr> <to_addr> <subject> <body>")
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
