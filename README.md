## discord_bitrate_bot
A Discord.py bot which can adjust a voice channel's bitrate depending on the number of users connected. Programmed to be run on a Raspberry Pi, but can work on either Linux or Windows.

Also has features which allows users to write and view entries to lists related to video game and movie ideas.

# What Can This Be Used For?

If you want to change the bitrate of voice channels based on the number of users, this bot can do that. One legitimate use case could be for people with very low-quality internet connections.

# Crunch Down Audio

I should preface this by saying that this use of the bot was made almost entirely for comedic effect. It was a funny idea that solves a problem in a very impractical way.

Sometimes, Discord just has too many people connected to a single channel. Communication might start to get loud, messy, and frustrating. Rather than set hard user limits that force people to be left out, this bot allows one to take a softer touch.

By default, if this bot detects that more than six people are in a single voice chat, it will wait for a short period of time, and then change the voice channel's bitrate from 64000 bits per second, all the way down to 8000. This makes it noticeable and slightly less pleasant to be in the channel, but voice chat still works well enough to communicate fine with each other.

The time delay is random, and is meant to make it less obvious what is happening when the 7th person joins the voice call.

# Configuration file

This bot allows you to customize most important values. 

You can customize how many users must be in a voice channel before the bitrate change takes effect, the minimum and maximum bits per second, the minimum and maximum time delay, the bot's prefix token, and you can also "whitelist" specific voice channels if you want to exclude them from the bot's effect.

If you want to whitelist a voice channel, get the channel's ID by right-clicking on it and selecting "Copy ID" (Make sure you have developer mode enabled in Settings > Advanced > Developer Mode), and then pasting it into the list in configuration.py. If there's more than one channel to whitelist, put commas between the values.

# Setup

Make sure you have Python installed, as well as discord.py. With these, you can run the bot on either Windows or Linux (though I have not rigorously tested running on Windows).

Most importantly, the bot first needs a bot token to work. To get a token, you can use the following tutorial: https://www.writebots.com/discord-bot-token/

That tutorial also provides instructions on how to add a bot to a Discord server. Note that for "scopes", just choose "bot", whereas for "bot permissions", you need to at least allow for "manage channels" and "send messages" to get the functionality of the bot.

After this, you can run the bot using Python, and it should come online and work!
