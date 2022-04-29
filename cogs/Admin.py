import nextcord
from nextcord.ext import commands


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    # detect and remove words
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.content.startswith('!remove'):
            await message.delete()
            await message.channel.send('Removed')
        if message.content.startswith('!shutdown'):
            await message.channel.send('Shutting down...')
            await self.client.close()
        if message.content.startswith('!restart'):
            await message.channel.send('Restarting...')
            await self.client.close()
        if message.content.startswith('!clear'):
            await message.channel.purge(limit=10)
            await message.channel.send('Cleared')
        if message.content.startswith('!ping'):
            await message.channel.send('Pong!')
        if message.content.startswith('baby lock the door') or message.content.contains('BABY LOCK THE DOOR'):
            await message.delete()
            await message.channel.send('shush')


def setup(client):
    client.add_cog(Admin(client))


# embed message
# @client.command(name='stats')
# async def stats(context):
#     myembed = nextcord.Embed(
#         title="ste", description="Useless charecter", color=0x00ff00)
#     myembed.add_field(name="HP:", value="1", inline=False)
#     myembed.add_field(name="Height:", value="1cm", inline=False)
#     myembed.add_field(name="Weight:", value="6g", inline=False)
#     myembed.add_field(name="Speed:", value="too slow", inline=False)
#     myembed.add_field(name="Attack:", value="1", inline=False)
#     myembed.add_field(name="Defense:", value="none", inline=False)
#     myembed.set_footer(text="The complete stats of Celeste")
#     await context.message.channel.send(embed=myembed)

# # embed 2
# @client.command()
# async def embed(ctx):
#     theembed = nextcord.Embed(title="Your profile", url='https://www.youtube.com/', description="about you", color=0x00ff00)
#     theembed.set_author(name=ctx.author.display_name, url='https://www.youtube.com/', icon_url=ctx.author.avatar_url)
#     theembed.set_thumbnail(url=ctx.author.avatar_url)
#     theembed.add_field(name="HP:", value="1", inline=True)
#     theembed.add_field(name="Height:", value="1cm", inline=False)
#     theembed.add_field(name="Weight:", value="6g", inline=True)
#     theembed.add_field(name="Speed:", value="too slow", inline=True)
#     theembed.set_footer(text="ur mom")
#     await ctx.message.channel.send(embed=theembed)
