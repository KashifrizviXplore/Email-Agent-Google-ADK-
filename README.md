📧 Email Agent (Google ADK + MySQL)

An intelligent Email Automation Agent built with Google ADK, using MySQL for persistent session management and secure workflow automation.

🚀 Features

⚙️ Built with Google ADK Agent Framework

🗄️ MySQL integration for session handling

🔒 Secure .env configuration for sensitive data

🌐 CORS-enabled REST API layer

⚙️ Setup Guide
🧩 1️⃣ Create and activate a virtual environment
# Create a new virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate

📦 2️⃣ Install dependencies
pip install -r requirements.txt

🔑 3️⃣ Create and configure a .env file

The .env file stores your Google API key and database credentials securely.
This file should be created in your project’s root directory.

🪄 Steps to create:

In your project root, create a new file named .env

Open it in a text editor (like VS Code or Notepad)

Add the following configuration:

# 🔐 Google API Key
GOOGLE_API_KEY=*****************************************

# 🗄️ MySQL Database Configuration
MYSQL_HOST=localhost
MYSQL_USER=User Name
MYSQL_PASSWORD=****
MYSQL_DB=Database Name
MYSQL_PORT=Port Number

# 🌐 Application Port
PORT=8080


💡 Note: Never share your .env file publicly or commit it to GitHub.
Add it to your .gitignore to keep it private.

▶️ 4️⃣ Run the application
python main.py


Or run it using Uvicorn:

uvicorn main:app --host 0.0.0.0 --port 8080 --reload


🌍 Your application will be available at:
http://localhost:8080

🧠 How It Works

🤖 Google ADK handles agent logic and session persistence

💾 MySQL stores agent data and sessions

🔐 .env keeps credentials secure and configurable

🧰 Example requirements.txt
fastapi
uvicorn
python-dotenv
mysql-connector-python
google-adk
