import os
import discord
from dotenv import load_dotenv

# Load the .env file
load_dotenv()


def format_the_message(message: str, variantPrompt: str, link: str) -> str:

    if variantPrompt == "":
        variantPrompt = "No Variant"

    title = message.split("\n", 1)[0]
    description = message.split("\n", 1)[1]

    msg = f"""
# __Title__ : {title}
**__Variant Prompt__** : {variantPrompt}

## __Description__ : 
```{description}```


# [The Post Link]({link})"""

    return msg


async def send_message_to_discord(
    image_path: str, message: str, variantPrompt: str, link: str
) -> None:
    # Grab the token of your discord bot token & channel ID
    DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))

    intents = discord.Intents.default()
    intents.message_content = True

    # We create a client instance
    client = discord.Client(intents=intents)

    # Grab the formated message
    formated_msg = format_the_message(message, variantPrompt, link)

    # Function to send the message
    async def send_message():
        channel = client.get_channel(int(CHANNEL_ID))
        with open(image_path, "rb") as f:
            image = discord.File(f)
            await channel.send(content=formated_msg, file=image)

    # Login discord bot event
    @client.event
    async def on_ready():
        print(f"🟢 {client.user} Connected")
        await send_message()
        await client.close()  # Close the connection after send the message

    # Login to discord serveur
    await client.start(DISCORD_TOKEN)
