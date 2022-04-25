# importing the discord package
from asyncio import queues
from unicodedata import name
import discord
from discord import FFmpegPCMAudio
from discord.ext import commands


# getting token
from apikeys import *

intents = discord.Intents.default()
intents.members = True

queues = {}


def check_queue(ctx, id):
    if queues[id] != []:
        voice = ctx.guild.voice_client
        source = queues[id].pop(0)
        player = voice.play(source)


#client / bot
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Streaming(name='single mom in your area', url='https://www.twitch.tv/singlemom'))
    print('Bot is ready.')
    print('---------------------')
    # bot_channel = client.get_channel(843827377901142049)
    # await bot_channel.send("my owner shrunk, HELP!")

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

# pause
@client.command(pass_content=True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_playing():
        voice.pause()
        await ctx.send('Paused')
    else:
        await ctx.send('Nothing playing')

# resume
@client.command(pass_content=True)
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_paused():
        voice.resume()
        await ctx.send('Resumed')
    else:
        await ctx.send('Nothing paused')


# stop
@client.command(pass_content=True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_playing():
        voice.stop()
        await ctx.send('Stopped')
    else:
        await ctx.send('Nothing playing')

# play
@client.command(pass_content=True)
async def play(ctx, arg):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio(arg + '.mp3')
    player = voice.play(source, after=lambda x=None: check_queue(
        ctx, ctx.message.guild.id))

# queue
@client.command(pass_content=True)
async def queue(ctx, arg):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio(arg + '.mp3')
    guild_id = ctx.message.guild.id
    if guild_id in queues:
        queues[guild_id].append(source)
    else:
        queues[guild_id] = [source]
    await ctx.send('Added to queue')


# clear
@client.command(pass_content=True)
async def clear(ctx):
    queues[ctx.message.guild.id] = []
    await ctx.send('Queue cleared')



# embed message
@client.command(name='stats')
async def stats(context):
    myembed = discord.Embed(
        title="ste", description="Useless charecter", color=0x00ff00)
    myembed.add_field(name="HP:", value="1", inline=False)
    myembed.add_field(name="Height:", value="1cm", inline=False)
    myembed.add_field(name="Weight:", value="6g", inline=False)
    myembed.add_field(name="Speed:", value="too slow", inline=False)
    myembed.add_field(name="Attack:", value="1", inline=False)
    myembed.add_field(name="Defense:", value="none", inline=False)
    myembed.set_footer(text="The complete stats of Celeste")
    await context.message.channel.send(embed=myembed)

# embed 2
@client.command()
async def embed(ctx):
    theembed = discord.Embed(title="Your profile", url='https://www.youtube.com/', description="about you", color=0x00ff00)
    theembed.set_author(name=ctx.author.display_name, url='https://www.youtube.com/', icon_url=ctx.author.avatar_url)
    theembed.set_thumbnail(url=ctx.author.avatar_url)
    theembed.add_field(name="HP:", value="1", inline=True)
    theembed.add_field(name="Height:", value="1cm", inline=False)
    theembed.add_field(name="Weight:", value="6g", inline=True)
    theembed.add_field(name="Speed:", value="too slow", inline=True)
    theembed.set_footer(text="ur mom")
    await ctx.message.channel.send(embed=theembed)

# # detect and remove words
# @client.event
# async def on_message(message):
#     if message.content == "ok":
#         await message.delete()
#         await message.channel.send("no u")

# run the bot
client.run(BOTTOKEN)
