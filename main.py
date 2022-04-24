# importing the discord package
from unicodedata import name
import discord
from discord import FFmpegPCMAudio
from discord.ext import commands

# getting token
from apikeys import *

intents = discord.Intents.default()
intents.members = True

#client / bot
client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    print('Bot is ready.')
    print('---------------------')
    bot_channel = client.get_channel(843932032027197480)
    await bot_channel.send("im online bestie")

# user joined
@client.event
async def on_member_join(member):
    channel = client.get_channel(843932032027197480)
    await channel.send(f"Welcome {member.mention} to the server!")


# user left
@client.event
async def on_member_remove(member):
    channel = client.get_channel(843932032027197480)
    await channel.send(f"{member.mention} has left the server!")

# embed message
@client.command(name='stats')
async def stats(context):
    myembed = discord.Embed(title="ste", description="Useless charecter", color=0x00ff00)
    myembed.add_field(name="HP:", value="1", inline=False)
    myembed.add_field(name="Height:", value="1cm", inline=False)
    myembed.add_field(name="Weight:", value="6g", inline=False)
    myembed.add_field(name="Speed:", value="too slow", inline=False)
    myembed.add_field(name="Attack:", value="1", inline=False)
    myembed.add_field(name="Defense:", value="none", inline=False)
    myembed.set_footer(text="The complete stats of Celeste")

    await context.message.channel.send(embed=myembed)

# joing voice if user present
@client.command(pass_content=True)
async def join(context):
    if (context.author.voice):
        channel = context.message.author.voice.channel
        # play audio using FFmpegPCMAudio
        voice = await channel.connect()
        source = FFmpegPCMAudio('intro.mp3')
        player = voice.play(source)
    else:
        await context.send("You are not in a voice channel")

# leave
@client.command(pass_content=True, name='leave')
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Disconnected")
    else:
        await ctx.send("i aint in no voice channel")


#pause 
@client.command(pass_content=True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_playing():
        voice.pause()
        await ctx.send('Paused')
    else:
        await ctx.send('Nothing playing')

#resume
@client.command(pass_content=True)
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_paused():
        voice.resume()
        await ctx.send('Resumed')
    else:
        await ctx.send('Nothing paused')

#stop
@client.command(pass_content=True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_playing():
        voice.stop()
        await ctx.send('Stopped')
    else:
        await ctx.send('Nothing playing')

#play
@client.command(pass_content=True)
async def play(ctx, arg):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio(arg + '.mp3')
    player = voice.play(source)


#run the bot
client.run(BOTTOKEN)
