📧 Advanced Bulk Email Sender by Y4BN

🚀 Description
A cool as fuck bulk email sender with multiple SMTP configurations, email validation, Telegram notifications, and a professional modern interface. Designed for high efficiency and reliability.

⚙️ Features
Multi-SMTP Support – Add multiple SMTP servers in config.json, but the system will use only one randomly.

Telegram Notifications – Get real-time updates on email status.

Customizable Email Templates – Predefined templates for phishing awareness campaigns.

Email Validation – Filters out invalid email addresses.

Modern UI – Uses rich and colorama for a stylish command-line interface.

Automated Configuration – First-time setup prompts you for credentials and saves them.

🛠️ Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/Y4BN/Bulk-Email-Sender.git
cd Bulk-Email-Sender
2️⃣ Install Dependencies
Ensure you have Python 3.8+ installed. Then, run:

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Configure SMTP & Telegram
Run the script once to set up the config.json:

bash
Copy
Edit
python main.py
It will ask for:

Telegram Bot Token

Telegram Chat ID

SMTP Server, Port, Email & Password

📌 Usage
1️⃣ Add Emails to emails.txt
Put target emails in emails.txt, one per line.

2️⃣ Run the Script
bash
Copy
Edit
python main.py
3️⃣ Select an Email Template
Choose from predefined phishing awareness emails.

4️⃣ Enter the Phishing Awareness Link
Provide a URL (e.g., a security training page).

5️⃣ Start Sending
The script will:

Validate emails

Select a random SMTP server from config.json

Send emails

Notify you via Telegram

🔄 Config File (config.json)
json
Copy
Edit
{
    "TELEGRAM_BOT_TOKEN": "your_bot_token",
    "TELEGRAM_CHAT_ID": "your_chat_id",
    "SMTP_SERVERS": [
        {
            "server": "smtp.gmail.com",
            "port": 587,
            "email": "youremail@gmail.com",
            "password": "yourpassword"
        }
    ]
}
🛑 Disclaimer
This tool is meant for ethical and educational purposes ONLY.
Do not use it for illegal activities.

📜 License
This project is open-source under the MIT License.

🚀 Developed by Y4BN
🔥 Making Python projects cool as fuck! 🔥
