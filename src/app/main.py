from app.crews.poem_crew.crew import EmailAgentCrew
from app.tools import email_tools
from dotenv import load_dotenv
import os
load_dotenv()
os.environ['GEMINI_API_KEY'] = ('GEMINI_API_KEY')

def kickoff():
    load_dotenv()
    imap_server = "imap.gmail.com"
    email_user = os.getenv("EMAIL_USER")
    email_pass = os.getenv("EMAIL_PASS")

    if not email_user or not email_pass:
        print("❌ Email credentials not found in .env")
        return

    emails = email_tools.fetch_emails(imap_server, email_user, email_pass)
    print("🚀 Starting Email Agent Crew...\n")
    crew = EmailAgentCrew(emails)
    crew.process_emails()
    print("\n✅ All emails processed.")

if __name__ == "__main__":
    kickoff()



