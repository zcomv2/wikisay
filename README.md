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
