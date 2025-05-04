from crewai import Agent, Task, Crew
from app.tools import email_tools

class EmailAgentCrew:
    def __init__(self, emails):
        self.emails = emails

        self.spam_filter_agent = Agent(
            role="Spam Filter",
            goal="Detect spam emails",
            backstory="Expert at filtering out unwanted emails.",
            allow_delegation=False,
            verbose=True
        )

        self.draft_detector_agent = Agent(
            role="Draft Detector",
            goal="Detect emails that look incomplete",
            backstory="Identifies half-written or placeholder messages.",
            allow_delegation=False,
            verbose=True
        )

        self.important_email_agent = Agent(
            role="Important Email Notifier",
            goal="Notify about useful or high-priority emails",
            backstory="Flags emails that seem important for work or personal matters.",
            allow_delegation=False,
            verbose=True
        )

        self.reply_agent = Agent(
            role="Reply Writer",
            goal="Write short professional replies",
            backstory="Generates polite, short replies to important emails.",
            allow_delegation=False,
            verbose=True
        )

    def process_emails(self):
        for i, email in enumerate(self.emails, 1):
            print(f"\n📩 Processing Email {i}:\n{email[:100]}...")  # preview first 100 chars

            if email_tools.is_spam(email):
                print("🚫 Detected as spam. Skipping.")
                continue

            if email_tools.detect_draft(email):
                print("📝 This looks like a draft or incomplete email.")
                continue

            if email_tools.notify_important(email):
                print("✅ Important email found!")
                reply = email_tools.auto_reply(email)
                print(f"✉️ Suggested reply:\n{reply}")
            else:
                print("ℹ️ Email is not marked as important.")
