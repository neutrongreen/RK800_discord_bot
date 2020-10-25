#test update for main.pyw
import discord
from discord.ext import commands
client = commands.Bot(command_prefix="$", pm_help=False)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="$help"))

extentions = ['learning', 'enforcer'] 

if __name__ =='__main__':
    for extention in extentions:
        try:
            client.load_extension("cogs."+extention)
            print("{} loaded".format(extention))
        except Exception as error:
            print("{} cannot be loaded. [{}]".format(extention, error))

client.run('')