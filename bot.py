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


async def setlang(l):
    responses.language(l)


def run_discord_bot():
    TOKEN = 'your token'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    tree = app_commands.CommandTree(client)
    guild_id = 1118228930160242750

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

    @tree.command(name="langto_german", description="used to set game language to german",
                  guild=discord.Object(id=guild_id))
    async def set_lang_german(interaction):
        await setlang("de")
        await interaction.response.send_message("The language has been set to german")

    @tree.command(name="langto_english", description="used to set game language to english",
                  guild=discord.Object(id=guild_id))
    async def set_lang_english(interaction):
        await setlang("en")
        await interaction.response.send_message("The language has been set to english")

    @tree.command(name="langto_bengali", description="used to set game language to bengali",
                  guild=discord.Object(id=guild_id))
    async def set_lang_english(interaction):
        await setlang("bn")
        await interaction.response.send_message("The language has been set to bengali")

    @tree.command(name="langto_spanish", description="used to set game language to spanish",
                  guild=discord.Object(id=guild_id))
    async def set_lang_english(interaction):
        await setlang("es")
        await interaction.response.send_message("The language has been set to spanish")

    @tree.command(name="langto_french", description="used to set game language to french",
                  guild=discord.Object(id=guild_id))
    async def set_lang_english(interaction):
        await setlang("fr")
        await interaction.response.send_message("The language has been set to french")

    @tree.command(name="langto_pl", description="used to set game language to polish",
                  guild=discord.Object(id=guild_id))
    async def set_lang_english(interaction):
        await setlang("pl")
        await interaction.response.send_message("The language has been set to polish")

    @tree.command(name="langto_italian", description="used to set game language to italian",
                  guild=discord.Object(id=guild_id))
    async def set_lang_english(interaction):
        await setlang("it")
        await interaction.response.send_message("The language has been set to italian")

    @tree.command(name="langto_romanian", description="used to set game language to romanian",
                  guild=discord.Object(id=guild_id))
    async def set_lang_english(interaction):
        await setlang("ro")
        await interaction.response.send_message("The language has been set to romanian")

    @tree.command(name="langto_portuguese", description="used to set game language to portuguese",
                  guild=discord.Object(id=guild_id))
    async def set_lang_english(interaction):
        await setlang("pt")
        await interaction.response.send_message("The language has been set to portuguese")

    client.run(TOKEN)
