import discord, os, json, string, asyncio, random
from discord.ext import commands, tasks
from discord.ext.commands import has_role, has_permissions, check
from termcolor import colored

TOKEN = "no"

i = discord.Intents.all()

client = commands.Bot(command_prefix="!", intents=i)
client.remove_command("help")

#############################__events__#############################

@client.event
async def on_ready():
    global status

    print("ID: "+colored(f"{str(client.user.id)}", "green")+" NAME: "+colored(f"{client.user.name}", "green"))

    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="people ban eachother!"))

#############################__functions__#############################

def is_authed(ctx):
    return ctx.author.id in [508372340904558603]

#############################__messages__#############################

@client.event
async def on_message(message):
    if not message.author.bot:
        await client.process_commands(message)

    if "slave" in message.content.lower() and "bad" in message.content.lower() and message.author.id != 526188598253584404:
        punish = True
        for word in ["aint", "ain't", "nuh", "not", "isnt", "isn't", "never", "cant be", "unbad", "is out of", "isn", "n0t", "dont", "don't", "doesn't"]:
            if word in message.content.lower() or len(message.content) > 11:
                punish = False
                print("Ok")
            print(word)

        if punish:
            await message.author.send("KILL YOUR SELF NIGGA")
            await message.author.kick()

#############################__commands__#############################

@client.command()
async def help(ctx):
    await ctx.send("NAH, No help for you!")

#############################__run__#############################

for folder in os.listdir('cogs'):
    print(colored(f'\nStarting {folder} Cogs\n', 'yellow'))

    for i, filename in enumerate(os.listdir(f"./cogs/{folder}")):
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{folder}.{filename[:-3]}")

print("\n")

client.run(TOKEN)
