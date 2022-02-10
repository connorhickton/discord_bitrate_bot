# configuration.py
# Use this to change the values used by bot.py

# BOT TOKEN - needed for the bot to exist. You must enter your own token here.
# Format: token = '[long string of characters]', i.e. token = '839hv.08h923b0cs80klahdKJLHseh'
token = ''

# Bot Prefix - Choose which character(s) commands are preceded by.
# Default is '>>', i.e. >>poke
prefix = '>>'

# bitrate (in bits per second) that applies when more than the max_vc_members are connected to a single channel.
# Minimum is 8000 as per Discord's limit.
# Default is 8000.
low_bps = 8000

# bitrate (in bits per second) that applies when less than the max_vc_members are connected to a single channel.
# Maximum recommended is 64000, as the guild needs to be 'boosted' a certain amount to get more.
# Default is 64000.
high_bps = 64000

# Maximum number of users connected to a single voice channel before the low bitrate will be applied.
# Default is 6 members.
max_vc_members = 6


#############################################################################################################################################
# The "delay" is the random amount of time between when a number of users above max_vc_members is reached, and when a bitrate change happens.
# This is to make it harder to detect that it was the number of users connected that caused the bitrate change. 
#############################################################################################################################################

# Minimum possible amount of delay (in seconds) between when the user count increases above the max_vc_members amount, and when the bitrate changes.
# Default is 20 seconds.
min_delay = 20

# Maximum possible amount of delay (in seconds) between when the user count increases above the max_vc_members amount, and when the bitrate changes.
# Default is 200 seconds.
max_delay = 200


# Whitelist: If you want a channel to not have the bitrate adjustments apply to it, enter the channel ID into this list.
# format: whitelist = [012345678910111213, 141516171819202122]
whitelist = []




