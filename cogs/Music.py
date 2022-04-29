# importing the nextcord package
from typing_extensions import Self
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from nextcord import FFmpegPCMAudio
from nextcord import member
from asyncio import queues
from unicodedata import name


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    queues = {}

    def check_queue(ctx, id):
        if queues[id] != []:
            voice = ctx.guild.voice_client
            source = queues[id].pop(0)
            player = voice.play(source)

    # joing voice if user present
    @commands.command(pass_content=True)
    async def join(self, context):
        if (context.author.voice):
            channel = context.message.author.voice.channel
            # play audio using FFmpegPCMAudio
            voice = await channel.connect()
            source = FFmpegPCMAudio('intro.mp3')
            player = voice.play(source)
        else:
            await context.send("You are not in a voice channel")

    # leave
    @commands.command(pass_content=True, name='leave')
    async def leave(self, ctx):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
            await ctx.send("Disconnected")
        else:
            await ctx.send("i aint in no voice channel")

    # pause
    @commands.command(pass_content=True, name='pause')
    async def pause(self, ctx):
        if (ctx.voice_client):
            ctx.voice_client.pause()
            await ctx.send("Paused")
        else:
            await ctx.send("i aint in no voice channel")

    # resume
    @commands.command(pass_content=True, name='resume')
    async def resume(self, ctx):
        if (ctx.voice_client):
            ctx.voice_client.resume()
            await ctx.send("Resumed")
        else:
            await ctx.send("i aint in no voice channel")

    # stop

    @commands.command(pass_content=True, name='stop')
    async def stop(self, ctx):
        if (ctx.voice_client):
            ctx.voice_client.stop()
            await ctx.send("Stopped")
        else:
            await ctx.send("i aint in no voice channel")

    # play
    @commands.command(pass_content=True)
    async def play(self, ctx, arg):
        voice = ctx.guild.voice_client
        source = FFmpegPCMAudio(arg + '.mp3')
        player = voice.play(source, after=lambda x=None: self.check_queue(
            ctx, ctx.message.guild.id))
        await ctx.send("Playing " + '**' + arg + '**')

    # queue
    @commands.command(pass_content=True)
    async def queue(self, ctx, arg):
        if (ctx.voice_client):
            queues[ctx.message.guild.id].append(FFmpegPCMAudio(arg + '.mp3'))
            await ctx.send("Queued")
        else:
            await ctx.send("i aint in no voice channel")

    # clear

    @commands.command(pass_content=True)
    async def clear(self, ctx):
        queues[ctx.message.guild.id] = []
        await ctx.send('Queue cleared')


def setup(client):
    client.add_cog(Music(client))
