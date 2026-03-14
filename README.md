# Discord AI ChatBot

A Discord bot built with `discord.py` that listens for keywords in designated channels and automatically responds with relevant messages and reactions.

## Features

- **Keyword Auto-Responses** — Detects keywords in messages and replies with a preset response
- **Emoji Reactions** — Adds a reaction to triggered messages
- **Channel Filtering** — Only responds in whitelisted channel IDs
- **Cog Architecture** — Modular design using discord.py cogs
- **Logging** — Console and file logging via Python's `logging` module

## Keyword Triggers

| Keyword | Response |
|---------|----------|
| hello | My world |
| kev | Has a bigger brain |
| bot | I am a bot |
| thanks | Always here to help! |
| goodbye | Farewell and take care! |
| help | How can I assist you today? |
| funny | I'm glad you enjoyed that! |
| weather | Looking up the weather for you! |
| music | Let's talk about music! |
| news | Here's what's happening around the world |
| sports | Which sport are you interested in? |
| food | What type of cuisine are you craving today? |
| halil | Hello Halil! What can I do for you today? |
| curse words | Watch your language! |

## Project Structure

```
Discord-AI-ChatBot/
├── main.py            # Entry point, bot setup
├── settings.py        # Logging config, loads .env
├── serverconfig.yml   # Keyword/response/reaction config
├── cogs/
│   └── autoresponse.py  # Autoresponse cog
└── .env               # Bot token (not committed)
```

## Setup

### Prerequisites

- Python 3.10+
- A Discord bot token ([Discord Developer Portal](https://discord.com/developers/applications))

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Keval88/Discord-AI-ChatBot.git
   cd Discord-AI-ChatBot
   ```

2. Install dependencies:
   ```bash
   pip install discord.py python-dotenv
   ```

3. Create a `.env` file in the root directory:
   ```
   DISCORD_API_TOKEN=your_bot_token_here
   ```

4. Update the allowed channel IDs in `cogs/autoresponse.py` to match your server's channels.

5. Run the bot:
   ```bash
   python main.py
   ```

## Usage

Once the bot is running and invited to your server, it will automatically monitor whitelisted channels. Any message containing a keyword from the trigger list will receive a response and a reaction — no commands needed.

The command prefix is `!` for any future commands.

## License

This project is open source and available under the [MIT License](LICENSE).
