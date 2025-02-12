# wikisay
WikiSay is an IRC bot that allows users to search for information on Wikipedia in three languages: Spanish, English, and Japanese. It connects to irc.libera.chat and listens for specific commands at the beginning of messages to provide accurate responses.

📌 Features

✅ Multi-language Wikipedia Search (!wiki-es, !wiki-en, !wiki-ja).

✅ Strict Command Detection (only activates if the command is at the start of the message).

✅ Safe Input Handling (prevents shell injection attacks and excessive input).

✅ Limited Response Length (first 400 characters, with a "Read more" link).

✅ Auto-Reconnects to IRC and responds to PING requests.

✅ User-Agent Compliance (ensures proper API requests to Wikipedia).

✅ Runs in Background using pm2 for stability.

🛠️ Installation

1️⃣ Install Required Dependencies

Make sure you have Python 3.7+ installed and install the required libraries:

pip3 install wikipedia-api

If wikipedia-api is not found, install it manually:

pip3 install git+https://github.com/martin-majlis/Wikipedia-API.git

3️⃣ Configure the Bot

Edit the bot settings inside wikisay.py (if necessary):

SERVER = "irc.libera.chat"

PORT = 6667

NICK = "Wikisay"

CHANNEL = "#VoxAssist"

USER_AGENT = "WikiSayBot/1.0 (https://yourwebsite.com/)"

4️⃣ Run the Bot

To start the bot manually, run:

python3.14 wikisay.py

To run it in background mode using pm2:

pm2 start wikisay.py --name wikisay

pm2 save

🔍 How It Works

Command Syntax

Users can request Wikipedia summaries using these commands:

Command	Description

!wiki-es <topic>	Search Wikipedia in Spanish

!wiki-en <topic>	Search Wikipedia in English

!wiki-ja <トピック>	Search Wikipedia in Japanese

⚙️ Technical Details

The bot connects to irc.libera.chat and joins a channel using socket.

Listens for messages in #VoxAssist and processes commands at the start of a line.

Uses Wikipedia API (wikipediaapi) to fetch article summaries.

Limits responses to 400 characters and appends a "Read more" link.

Uses regular expressions (re.compile) to validate input and avoid false activations.

Implements anti-shell injection filters to prevent abuse.

🛡️ Security Features

🔹 Strict Input Validation: Only allows letters, numbers, and spaces in queries.

🔹 No Command Execution: Prevents malicious command injections (; | & < >).

🔹 User-Agent Header: Uses a custom User-Agent to comply with Wikipedia API policies.

🔹 Message Pattern Matching: Commands must be at the beginning of the message.

Handles IRC PING/PONG messages to maintain connection stability.

Can be deployed with pm2 to ensure automatic restarts.

🔄 Future Improvements

Add more languages for Wikipedia searches.

Improve error handling for API failures.

Allow direct message queries (/msg Wikisay !wiki-es ...).

Implement rate-limiting to prevent spam.
