import os
import discord

TOKEN = os.getenv("DISCORD_TOKEN")
MESG_CHANNEL = 1380161525418819594

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_voice_state_update(member, before, after):
    mesg_channel = client.get_channel(MESG_CHANNEL)

    # 入退室以外はreturn.
    if before.channel == after.channel:
        return

    if before.channel is None: #VCへの入室.
        await mesg_channel.send(f'{member.display_name} joined voice channel {after.channel.name}.')
    elif after.channel is None: #VCからの退出.
        await mesg_channel.send(f'{member.display_name} left voice channel {before.channel.name}.')
    else: #VC間の移動.
        await mesg_channel.send(f'{member.display_name} moved from {before.channel.name} to {after.channel.name}.')
    

    

client.run(TOKEN)