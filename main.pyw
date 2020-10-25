import discord
from discord.ext import commands
from cogs.learning import nlp
from cogs.enforcer import interested
client = commands.Bot(command_prefix="$", pm_help=False)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="$help"))

client.add_cog(nlp())
client.add_cog(interested())
client.run('Insert Token Here')