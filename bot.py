import random
import sys
import discord
import asyncio
import configuration
from discord.ext import commands


# "constants"
false = 0
FALSE = 0
true = 1
TRUE = 1

max_vc_members = configuration.max_vc_members
min_delay = configuration.min_delay
max_delay = configuration.max_delay
low_bps = configuration.low_bps
high_bps = configuration.high_bps
whitelist = configuration.whitelist
prefix = configuration.prefix

vote_list = []
user_votes = []

TOKEN = configuration.token

bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


# Function: poke
# Mostly used for debugging. Poke the bot if you want it to react.

@bot.command()
async def poke(ctx):
    
    await ctx.send("Yes, I'm here!")


# Function: sayuser
# Mostly used for debugging. @'s the user and says their username.

@bot.command()
async def sayuser(ctx):

    user=ctx.message.author
    uid=ctx.message.author.id
    await ctx.send("mention: " + user.mention + " name: " + user.name)


# Function: addmovie
# Adds user's movie suggestion to the movie_list.txt file.

@bot.command()
async def addmovie(ctx, *, uInput):

    #Format is <uid:message\n>
    
    user=str(ctx.message.author.id)     

    f = open("movie_list.txt", "a")
    
    await ctx.send("Added \"" + uInput + "\" to the movie list.")

    output = user + ":"
    output = output + uInput
    output = output + "\n"
    f.write(output)
    f.close()


# Function: addgame
# Adds user's game suggestion to the game_list.txt file.

@bot.command()
async def addgame(ctx, *, uInput):
    
    user=str(ctx.message.author.id)

    f = open("game_list.txt", "a")

    await ctx.send("Added \"" + uInput + "\" to the game list.")

    output = user + ":"
    output = output + uInput
    output = output + "\n"
    f.write(output)
    f.close()


# Function: deletemovie
# Removes a line from the stored movie_list.txt file, but only if the user sending this command was the one who first added the line.

@bot.command()
async def deletemovie(ctx, *, uInput):

    user=ctx.message.author.id

    # https://stackoverflow.com/questions/4710067/
    with open("movie_list.txt", "r") as f:
        lines = f.readlines()
    with open("movie_list.txt", "w") as f:
        
        line_removed = 0
        
        for line in lines:
            checkLine = line.strip("\n")
            
            splitLine = checkLine.split(":", 1)
            
            if (splitLine[1].lower() != uInput.lower() or splitLine[0] != str(user)) or line_removed != 0:
                f.write(line)
            else:
                line_removed+=1
        
        await ctx.send("Removed " + str(line_removed) + " lines.")



# Function: deletegame
# Removes a line from the stored game_list.txt file, but only if the user sending this command was the one who first added the line.

@bot.command()
async def deletegame(ctx, *, uInput):

    user=ctx.message.author.id

    # https://stackoverflow.com/questions/4710067/
    with open("game_list.txt", "r") as f:
        lines = f.readlines()
    with open("game_list.txt", "w") as f:
        
        line_removed = 0
        
        for line in lines:
            checkLine = line.strip("\n")
            
            splitLine = checkLine.split(":", 1)
            
            if (splitLine[1].lower() != uInput.lower() or splitLine[0] != str(user)) or line_removed != 0:
                f.write(line)
            else:
                line_removed+=1
        
        await ctx.send("Removed " + str(line_removed) + " lines.")




# Function: printlist
# prints the specified list, formatted with numbers.

@bot.command()
async def printlist(ctx, *, uInput):


    await ctx.send(printlist_helper(uInput))

################################################################################################################
# The following functions which involve printing exist because the users were confused at how arguments work.
################################################################################################################


# Function: printlistmovie
# Prints specifically the movie list. Exists because users didn't understand how arguments work.

@bot.command()
async def printlistmovie(ctx):

    await ctx.send(printlist_helper("movie"))


# Function: printmovielist
# Prints specifically the movie list.

@bot.command()
async def printmovielist(ctx):

    await ctx.send(printlist_helper("movie"))

# Function: printlistgame
# Prints specifically the game list.

@bot.command()
async def printlistgame(ctx):

    await ctx.send(printlist_helper("game"))


# Function: printgamelist
# Prints specifically the game list.

@bot.command()
async def printgamelist(ctx):

    await ctx.send(printlist_helper("game"))


# Function: printlist_helper
# All functions involving printing call this function to print the lists.
# Prints the content of a specified list (with numerical formatting) into the text channel that the command was called in.

def printlist_helper(uInput):
    
    lines = []

    if uInput == "game":
        with open("game_list.txt", "r") as f:
            lines = f.readlines()
    
    elif uInput == "movie":
        with open("movie_list.txt", "r") as f:
            lines = f.readlines()

    else:
        return "Error. That either wasn't a list that exists, or the bot's wrong. And I'm never wrong."
        

    if lines == []:
        return "The " + uInput + " list is empty."
    
    output = ""

    i = 0

    for i in range(len(lines)):
        add = lines[i].split(":", 1)
        list_num = i + 1
        output = output + str(list_num) + ": " + add[1]
        
    return output



# TODO: Add bot commands which allow for voting on game/movie list



# Function: choose
# Chooses a random entry from the list specified by the argument.

@bot.command()
async def choose(ctx, *, uInput):
    
    list_type = ""

    if uInput == "game":
        list_type="game_list.txt"
    elif uInput == "movie":
        list_type = "movie_list.txt"
    else:
        await ctx.send("You didn't use the command correctly!\nThe correct format is >>choose [game/movie]")


    with open(list_type, "r") as f:
        lines = f.readlines()
        
        val = random.randint(0, len(lines)-1)
        
        output = lines[val].split(":", 1)
        await ctx.send(uInput + " suggestion: " + output[1])



# Function on_voice_state_update
# Is called whenever a user joins or leaves a voice channel, or if a user deafens/mutes.
# This function (combined with its helper function) changes the bitrate of a voice channel depending on the number of users in a voice channel.
# By default, with the default values used in configuration.py, it will lower the bitrate when more than 6 users are in a voice channel.
# By default, there will be a random delay of 20 to 200 seconds between when the 7th user joins, and when the bitrate will change.

@bot.event
async def on_voice_state_update(member, before, after):
   
    channel = None

    if before.channel is not None and before.channel.id not in whitelist:
        await bitrate_adjust_helper(before.channel)

    if after.channel is not None and after.channel.id not in whitelist:
        await bitrate_adjust_helper(after.channel)
 


# Function: bitrate_adjust_helper
# Is called when a voice state update happens in a channel that is not on the whitelist (and also that exists).
# Input: Channel that exists and is not whitelisted
# Lowers the bitrate of the channel if more than max_vc_members are connected, and raises it back if less than max_vc_members are connected.

async def bitrate_adjust_helper(channel):

    print("CURRENT MEMBERS IN ", channel, ": ", (len(channel.members)))
    
    if len(channel.members) > max_vc_members and channel.bitrate != low_bps:
        print(channel, " has gone above max vc users, with ", len(channel.members), " users. Bitrate change imminent:")
        await asyncio.sleep(random.randint(min_delay, max_delay))
        await channel.edit(bitrate = low_bps)
        print("Bitrate change to ", low_bps, " is done.")

    elif len(channel.members) <= max_vc_members and channel.bitrate != high_bps:
        
        print(channel, " has calmed down and now only has ", len(channel.members), " users.")
        await asyncio.sleep(random.randint(min_delay, max_delay))
        await channel.edit(bitrate = high_bps)
        print("Bitrate change to ", high_bps, " is done.")






bot.run(TOKEN)

