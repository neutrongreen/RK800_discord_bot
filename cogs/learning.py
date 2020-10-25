import discord
from discord.ext import commands
import os 
import markovify
import datetime
import time 
from pathlib import Path
import json
class nlp(commands.Cog):
    """\nnatual langauge processing """
    @commands.command()
    async def run(self, ctx):
        if isinstance(ctx.channel, discord.DMChannel):
            ctx.channel.send("cannot use commands in dm channels")
            return None
        """\n Genrate sentence based upon messsages from channel or user.\nTo scan a users or a channels messages menton them """
        msg = await ctx.channel.send("Processing")
        try:    
            #get channel wanted and member wanted 
            member = ctx.message.mentions
            channel = ctx.message.channel_mentions or [ctx.message.channel]
            print(member)
            print(channel)


            #format file location
            storage_loc = os.getcwd() + "\\data\\{ch}".format(ch=channel[0].id)
            print(storage_loc)
            #check if directoy exist if not make one
            if not os.path.exists(Path(storage_loc)):

                os.makedirs(storage_loc)
                print('dirmade')
            #add file final 
            if member:
                storage_loc += "\\{}.json".format(member[0].id)
                print('eyy embmer')
            else:
                storage_loc += "\\main.json"
            print(storage_loc)
            storage_loc = Path(storage_loc)
            #check if file exists if not do main else load unread messages
            newdata = None
            newappend = ""
            jsonmodel = None
            filemodel = None
            date = None

            if os.path.exists(storage_loc):
                print('path exists')         
                with open(storage_loc, "r") as f:
                    data = json.load(f)
                    date = data["time"]
                    jsonmodel = markovify.NewlineText.from_json(data["model"])
                newdata = channel[0].history(after=datetime.datetime.fromtimestamp(date))
                print(newdata)


            else:
                print('path doesnt eyyy')
                newdata = channel[0].history(limit=15000)

            async for i in newdata:
                if member:
                    if i.author == member[0]:
                        newappend += i.content +"\n"
                else:
                    newappend += i.content +"\n"
            if newappend:
                filemodel = markovify.NewlineText(newappend)
            if jsonmodel and newappend:
                filemodel = markovify.combine([jsonmodel, filemodel], [1,1])
            elif jsonmodel:
                filemodel = jsonmodel


            temp = None
            for i in range(100):
                temp = filemodel.make_sentence()
                if temp:
                    break
            await ctx.channel.send(temp.replace("@", "") or "somthign wrong")
            del temp
            
            tempdata = {"time" : time.time(), "model" : filemodel.to_json()}
            with open(storage_loc, "w+") as f:
                f.write(json.dumps(tempdata, separators=(',', ':')))
                print("writine")
            del filemodel
            await ctx.message.delete()
            await msg.delete()
        except:
            await ctx.message.delete()
            await msg.delete()
            await ctx.channel.send("somthings wrong")

def setup(client):
    client.add_cog(nlp())
            


        
        


        

            

        

        