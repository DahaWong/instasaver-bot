# Instasaver
> v2.0.4
## Intro
A [Telegram Bot](https://core.telegram.org/bots/api) for sending links to Instapaper conveniently.

## Use
Here is [the link of bot](https://t.me/saveinstapaper_bot).
Chinese version only by now.

### Basics
After `/start` the bot, he will ask you to log in Instapaper account. Once logged in, you can send messages with links to the bot, then the article links can automatically be found and saved.

You can also delete/star your saved articles easily.

### Commands
- `/start`: Start the bot to log in.
- `/quit`: Log out.
- `/today`: Show articles saved today.
- `/about`: About the bot.

## Host Yourself
Considering privacy, I recommend you host this bot on your own server.

### Configuration
Rename `template.ini` to `config.ini` in root directory and then write your own configuration. 

You'll need both telegram bot token, which generated by [Bot Father](https://t.me/BotFather), and [Instapaper Full Developer API Token](https://www.instapaper.com/main/request_oauth_consumer_token).

### Dependencies
`python -m pip install -r requirements.txt` to install all dependencies required.


## Credits
- [Python Telegram Bot](https://python-telegram-bot.readthedocs.io/en/stable/index.html)
