import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import os

# getting token
from apikeys import *

intents = nextcord.Intents.default()
intents.members = True

#client / bot
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    # await client.change_presence(status=nextcord.Status.dnd, activity=nextcord.Streaming(name='single mom in your area', url='https://www.twitch.tv/singlemom'))
    print('Bot is ready.')
    print('---------------------')
    # bot_channel = client.get_channel(843827377901142049)
    # await bot_channel.send("m!")

testServerId = 843827377901142046

@client.slash_command(name='test', description='test', guild_ids=[843827377901142046])
async def test(interaction: Interaction):
    await interaction.response.send_message("test") 

initial_extensions = []
for filename in os.listdir('cola_test_bot\cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)

# run the bot
client.run(BOTTOKEN)
