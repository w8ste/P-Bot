import discord
import responses
from discord import app_commands
from itertools import cycle




# Send messages
async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'your token'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    tree = app_commands.CommandTree(client)
    guild_id = your guild_id

    # Handles general bot usage
    @client.event
    async def on_ready():
        await tree.sync(guild=discord.Object(id=guild_id))
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        await send_message(message, user_message)

    # create slash commands
    @tree.command(name="obi", description="The bot says one of Star Wars most famous lines",
                  guild=discord.Object(id=guild_id))
    async def obi_command(interaction):
        await interaction.response.send_message("Hello there!")

    @tree.command(name="turn", description="Tells you, whose turn it is", guild=discord.Object(id=guild_id))
    async def turn_command(interaction):
        await interaction.response.send_message(f'It is {responses.turn()}\'s turn')

    client.run(TOKEN)
