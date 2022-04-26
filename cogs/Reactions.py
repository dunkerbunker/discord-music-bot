import discord
from discord.ext import commands

class Reactions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == '💩':
            channel = self.client.get_channel(843827377901142049)
            await channel.send(f"{user.mention} has been shrunk!")


def setup(client):
    client.add_cog(Reactions(client))