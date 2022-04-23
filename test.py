# importing the discord package
from unicodedata import name
import discord
from discord.ext import commands

#client / bot
client = commands.Bot(command_prefix = '!')

@client.command(name='stats')
async def stats(context):
    myembed = discord.Embed(title="Celeste", description="Useless charecter", color=0x00ff00)
    myembed.add_field(name="HP:", value="1", inline=False)
    myembed.add_field(name="Height:", value="1cm", inline=False)
    myembed.add_field(name="Weight:", value="6g", inline=False)
    myembed.add_field(name="Speed:", value="too slow", inline=False)
    myembed.add_field(name="Attack:", value="1", inline=False)
    myembed.add_field(name="Defense:", value="none", inline=False)
    myembed.set_footer(text="The complete stats of Celeste")

    await context.message.channel.send(embed=myembed)


@client.event
async def on_ready():
    general_channel = client.get_channel(843932032027197480)
    await general_channel.send("im online bestie")

#run the bot
client.run('NzA0MzkzOTM2OTk0NTY2MTg0.Xqcf-Q.k2nVeGYTwJgIavdLrRf9RqXRwtE')
