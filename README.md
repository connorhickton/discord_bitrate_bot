## discord_bitrate_bot
A Discord.py bot which can adjust a voice channel's bitrate depending on the number of users connected. Programmed to be run on a Raspberry Pi (any type of Pi except Pico should do).

Also allows users to write and view entries to lists related to video game and movie ideas.

# Why?

I should preface this by saying that this bot was made almost entirely for comedic effect. It started as my first attempt at writing a discord bot, then I got a funny idea that solves a problem in a very impractical way.

# Crunch Down Audio

Sometimes, Discord just has too many people connected to a single channel. Everyone individually is pleasant enough, but when there's too many, people talk over each other, have cross-conversations, some people get ignored, and overall, it's not always a great experience. Rather than set hard user limits that force people to be left out, this bot allows one to take a softer touch.

By default, if this bot detects that more than six people are in a single voice chat, it will wait for a short period of time, and then change the voice channel's bitrate from 64000 bits per second, all the way down to 8000. This makes it noticeable and slightly less pleasant to be in the channel, but voice chat still works well enough to communicate fine with each other.

The time delay is random, and is meant to make it less obvious what is happening when the 7th person joins the voice call.

# Configuration

This bot allows you to customize most important values. 

Most importantly, the bot first needs a bot token to work.

You can customize how many users must be in a voice channel before the bitrate change takes effect, the minimum and maximum bits per second, the minimum and maximum time delay, the bot's prefix token, and you can also "whitelist" specific voice channels if you want to exclude them from the bot's effect.
