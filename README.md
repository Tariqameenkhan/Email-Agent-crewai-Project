# 📧 Gmail Email Agent (CrewAI-powered)

This project is an intelligent email assistant powered by [CrewAI](https://docs.crewai.com). It connects to your **Gmail inbox**, filters **spam**, detects **drafts**, flags **important emails**, and generates **professional auto-replies** — all using a team of AI agents.

---

## 🚀 Features

- ✅ Fetches real emails via **Gmail IMAP**
- 🧠 Uses multiple AI agents (CrewAI) for:
  - Spam filtering
  - Draft detection
  - Important email notification
  - Auto-reply generation  **Not Set**
- 🔐 Loads credentials securely from a `.env` file
- ✉️ Easily extendable to send replies or log to a file **Not Set**

---

## 📁 Project Structure

- app/
- ├── .env # Secure Gmail login (never commit this!)
- ├── pyproject.toml # uv config
- ├── src/
- │ └── app/
- │ ├── main.py # Entry point: kickoff function
- │ ├── tools/
- │ │ └── email_tools.py # Email fetching and filters
- │ └── crews/
- │ └── poem_crew/
- │ └── crew.py # AI agents definition


# ** 💡 Step 1: Enable App Passwords in Gmail**
⚠️ Don't use your Gmail password!
Use a Gmail App Password.

If you're using your main Gmail password, it won't work — Google blocks "less secure apps."

✅ Do this:

Go to → https://myaccount.google.com/apppasswords

Select Mail as the app, and Windows Computer as the device.

Google will give you a 16-character app password.
(Example: xxyy zzqq aabb cdef — no spaces.) 

# 💡 Enable IMAP in Gmail:
Before connecting, make sure IMAP is enabled:

Go to Gmail Settings

Click the "Forwarding and POP/IMAP" tab

In the IMAP access section, select "Enable IMAP"

Save changes

# Yep! ✅ Every Gmail account uses the same IMAP server:

IMAP Server: imap.gmail.com

# 📦 Dependencies
  ## 📦 Dependencies

- [CrewAI](https://docs.crewai.com/)
- **imaplib** (built-in with Python)
- **email** (built-in with Python)
- [uv](https://github.com/astral-sh/uv) (project runner like `poetry`)

- [`python-dotenv`](https://pypi.org/project/python-dotenv/)
  python-dotenv
  uv pip install python-dotenv crewai 


# ** 💡 Step 2: Create .env File **
- GEMINI_API_KEY=123444444444
- EMAIL_USER=your_email@gmail.com
- EMAIL_PASS=your_16_digit_app_password
- EMAIL_FETCH_MODE=first
- <!-- # EMAIL_FETCH_MODE=middle -->
- <!-- # EMAIL_FETCH_MODE=last -->

⚠️ Don't use your Gmail password!
Use a Gmail App Password.



# 🔒 Security
Never commit .env to Git

Uses Gmail App Passwords (safe alternative to your main password)

Can be extended to Gmail API with OAuth2 for more control



# 🧠 How It Works
Each email is processed by:

Spam Filter Agent → skips junk

Draft Detector Agent → skips incomplete emails

Important Notifier Agent → flags urgent/priority emails

Reply Agent → writes short, polite replies


# 🧑‍💻 Author
Tariq Ameen — CrewAI Gmail Automation Project


# 📈 To Do (optional)
 Send actual email replies via SMTP

 Store logs in a CSV or SQLite

 Add LLM-based summarization

 Add unit tests