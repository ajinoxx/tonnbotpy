import discord
from discord.ext import commands
import os
import random

myID = 191334024612937729

bellsID = 756194795411603547
studentID = 543187460021288960

client = commands.Bot(command_prefix = 't!')

@client.event
async def on_ready():
    print("We ready kiddies?")

@client.command(aliases=['t'])
async def test(ctx):
    print('Test command')
    if ctx.author.id == myID:
        await ctx.send("You're sexy Buechie!")
    else:
        await ctx.send("Check your DMs ;)")
        await ctx.author.dm_channel.send("I hope this isn't sexual harassment.")

@client.event
async def on_message(message):
    if message.channel.id != bellsID and discord.utils.find(lambda r: r.id == studentID, message.author.roles):
        print("Message is not in bells and it is not made by a bot")
        msgStr = message.content.lower()
        if msgStr.startswith("what") and len(msgStr) <= 6:
            await message.channel.send('Am I talking to myself?')
        elif msgStr.startswith("http") and "youtu" in msgStr:
            await message.channel.send("Live demo?")
        response = random.randint(1, 100)
        if response < 3:
            phrase = random.randint(1, 100)
            if phrase <= 33:
                await message.channel.send("That's a note!")
            elif phrase > 33 and phrase <= 66:
                await message.channel.send("That's the smartest thing you've said all year!")
            elif phrase > 66:
                await message.channel.send("You're brilliant!")
    else:
        if message.content == "Period 1 starts in 5 minutes!":
            await message.send.channel('Are we ready kiddies?')

    await client.process_commands(message)



client.run(os.environ['token'])