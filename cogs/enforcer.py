import discord
from discord.ext import commands

class interested(commands.Cog):
    
    """\nadds @intrested role"""
    @commands.command()
    async def tog(self, ctx):
        if isinstance(ctx.channel, discord.DMChannel):
            ctx.channel.send("cannot use commands in dm channels")
            return None
        """\nToggle intrested role"""
        try:
            role = None
            roles = ctx.guild.roles
            for i in roles:
                if i.name == "interested":
                    role = i
                    break
            if not role:
                await ctx.guild.create_role(name="interested", hoist=True)
            
            if role in ctx.message.author.roles:
                    await ctx.message.author.remove_roles(role)
            else:
                    await ctx.message.author.add_roles(role)
            await ctx.channel.send("role has been toggled")
        except:
            await ctx.channel.send("cant change role hank")

    

    async def on_guild_join(self, guild):
        role = None    
        for i in guild.roles:
            if i.name == "interested":
                role = i
                break

        role = role or await guild.create_role(name="interested", hoist=True)
        for i in guild.members:
            if not i.bot:
                try:
                    await i.add_roles(role)
                except:
                    pass

def setup(client):
    client.add_cog(interested())
            