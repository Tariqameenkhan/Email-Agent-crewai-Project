import imaplib
import email
from email.header import decode_header

def fetch_emails(imap_server, email_user, email_pass, mailbox="INBOX", limit=10):
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(email_user, email_pass)
    mail.select(mailbox)

    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()
    email_list = []

    for num in email_ids[-limit:]:
        status, data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(data[0][1])
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding or "utf-8")

        # Optionally include the body
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode(errors="ignore")
                    break
        else:
            body = msg.get_payload(decode=True).decode(errors="ignore")

        email_list.append(f"{subject}\n\n{body[:200]}")  # include body preview

    mail.logout()
    return email_list

def is_spam(email_text):
    spam_keywords = ["winner", "prize", "free", "urgent", "money", "offer"]
    return any(word.lower() in email_text.lower() for word in spam_keywords)

def detect_draft(email_text):
    return len(email_text.strip()) < 50

def notify_important(email_text):
    important_keywords = ["meeting", "project", "invoice", "deadline", "proposal", "client"]
    return any(word.lower() in email_text.lower() for word in important_keywords)

def auto_reply(email_text):
    return "Thank you for your email. I’ll get back to you shortly."
