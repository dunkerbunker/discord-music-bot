import nextcord
from nextcord.ext import commands


class Greetings(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(843932032027197480)
        await channel.send(f"Welcome {member.mention} to the server!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.client.get_channel(843932032027197480)
        await channel.send(f"{member.mention} has left the server!")


def setup(client):
    client.add_cog(Greetings(client))
