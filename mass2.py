import smtplib
import random
import time
import os
import requests
import threading
import re
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from rich.console import Console
from rich.progress import track
from rich.panel import Panel
from rich.table import Table
from colorama import init

init(autoreset=True)
console = Console()

# CONFIG FILE
CONFIG_FILE = "config.json"

# STARTUP BANNER
console.print(Panel.fit("🚀 [bold cyan]Y4BN's Ultimate Bulk Sender[/bold cyan] 💀", style="magenta"))

# LOAD CONFIG
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    return None

# SAVE CONFIG
def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)

# SETUP CONFIGURATION
config = load_config()
if not config:
    console.print("[yellow]⚙️ First-time setup: Enter SMTP and Telegram details.[/yellow]")
    config = {
        "TELEGRAM_BOT_TOKEN": input("Enter Telegram Bot Token: "),
        "TELEGRAM_CHAT_ID": input("Enter Telegram Chat ID: "),
        "SMTP_SERVERS": []
    }
    
    smtp_data = {
        "server": input("Enter SMTP Server (e.g., smtp.gmail.com): "),
        "port": int(input("Enter SMTP Port (e.g., 587): ")),
        "email": input("Enter SMTP Email: "),
        "password": input("Enter SMTP Password: ")
    }
    config["SMTP_SERVERS"].append(smtp_data)

    # OPTION TO ADD MULTIPLE SMTP
    while True:
        add_more = input("Add another SMTP? (y/n): ").strip().lower()
        if add_more == "y":
            smtp_data = {
                "server": input("Enter SMTP Server: "),
                "port": int(input("Enter SMTP Port: ")),
                "email": input("Enter SMTP Email: "),
                "password": input("Enter SMTP Password: ")
            }
            config["SMTP_SERVERS"].append(smtp_data)
        else:
            break

    save_config(config)
    console.print("[green]✅ Configuration saved![/green]")

# LOAD VARIABLES
TELEGRAM_BOT_TOKEN = config["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = config["TELEGRAM_CHAT_ID"]
SMTP_SERVERS = config["SMTP_SERVERS"]

# SELECT A RANDOM SMTP SERVER OR THE SINGLE ONE IF ONLY ONE EXISTS
def get_smtp():
    if len(SMTP_SERVERS) == 1:
        return SMTP_SERVERS[0]
    return random.choice(SMTP_SERVERS)

# EMAIL SETTINGS
SENDER_NAMES = ["University IT", "Admin Support", "Helpdesk", "Student Portal"]

EMAIL_TEMPLATES = {
    "1": {"name": "🔵 Student Verification", "subject": "University Student Verification Required", "body": "<p>Dear Student,</p><p>Please verify your student portal account.</p><p><a href='{link}'>Click here to verify</a></p>"},
    "2": {"name": "🔒 Account Security Alert", "subject": "Unusual Activity Detected", "body": "<p>We've detected suspicious activity.</p><p><a href='{link}'>Secure your account now</a></p>"},
    "3": {"name": "📊 University Survey Invitation", "subject": "Share Your Feedback – University Survey", "body": "<p>Your feedback is valuable!</p><p><a href='{link}'>Click here to participate</a></p>"}
}

# EMAIL VALIDATION
def is_valid_email(email):
    return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)

# LOAD EMAIL LIST
def load_valid_emails(filename="emails.txt"):
    try:
        with open(filename, "r") as file:
            return [email for email in file.read().splitlines() if is_valid_email(email)]
    except FileNotFoundError:
        console.print("[red]❌ File not found: emails.txt[/red]")
        return []

# TELEGRAM NOTIFICATION
def send_telegram_notification(email, sender_name, status):
    message = f"📧 Email Sent!\n🔹 To: {email}\n🔹 From: {sender_name}\n🔹 Status: {status}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": message})
    except Exception as e:
        console.print(f"[red]⚠️ Telegram error: {e}[/red]")

# SEND EMAIL FUNCTION
def send_email(target_email, sender_name, subject, message):
    smtp_data = get_smtp()
    msg = MIMEMultipart()
    msg['From'] = f"{sender_name} <{smtp_data['email']}>"
    msg['To'] = target_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, "html"))

    try:
        server = smtplib.SMTP(smtp_data["server"], smtp_data["port"])
        server.starttls()
        server.login(smtp_data["email"], smtp_data["password"])
        server.sendmail(smtp_data["email"], target_email, msg.as_string())
        server.quit()
        console.print(f"[green]✅ Email sent to {target_email} ({sender_name})[/green]")
        send_telegram_notification(target_email, sender_name, "✅ Sent Successfully")
    except Exception as e:
        console.print(f"[red]❌ Failed to send email to {target_email}: {e}[/red]")
        send_telegram_notification(target_email, sender_name, "❌ Failed to Send")

# SEND EMAILS IN BATCHES
def send_batch(emails, sender_name, subject, message):
    for email in track(emails, description="🚀 Sending emails..."):
        send_email(email, sender_name, subject, message)
        time.sleep(random.uniform(1, 3))

# COOL INTERFACE TO SELECT EMAIL TYPE
def bulk_send():
    console.print("\n📩 [bold blue]Bulk Email Sender by Y4BN[/bold blue]\n")

    table = Table(title="📜 Email Templates", show_lines=True)
    table.add_column("Option", justify="center", style="cyan", no_wrap=True)
    table.add_column("Template Name", style="magenta")

    for key, value in EMAIL_TEMPLATES.items():
        table.add_row(key, value["name"])
    console.print(table)

    choice = input("\nEnter your choice: ")
    if choice not in EMAIL_TEMPLATES:
        console.print("[red]Invalid choice! Exiting...[/red]")
        return

    phishing_link = input("\n🔗 Enter the phishing link: ")
    selected_template = EMAIL_TEMPLATES[choice]
    subject = selected_template["subject"]
    message = selected_template["body"].format(link=phishing_link)

    emails = load_valid_emails("emails.txt")
    if not emails:
        console.print("[red]⚠️ No valid emails found![/red]")
        return

    sender_name = random.choice(SENDER_NAMES)
    console.print(f"\n📤 Sending emails from: [cyan]{sender_name}[/cyan]")

    thread = threading.Thread(target=send_batch, args=(emails, sender_name, subject, message))
    thread.start()
    thread.join()

bulk_send()
