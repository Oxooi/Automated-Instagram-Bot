import asyncio
import os

from modules.dall import dalleGen
from modules.downloadImage import downloadImage
from modules.gptVision import describe_image
from modules.insta import upload_image_to_insta
from modules.discordBot import send_message_to_discord

from openai import OpenAI
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get the OPENAI infos
openai_api_key = os.environ.get("MY_OPENAI_API_KEY")
client = OpenAI(
    api_key=openai_api_key,
)


async def main() -> None:
    # Generate the image with Dall-E
    image, variantPrompt = dalleGen(client)

    # Download the image in local dir
    image_path = downloadImage(image, variantPrompt)

    # Get the image : title, description & hashtags with GPT-Vision
    image_info = describe_image(image_path, openai_api_key)

    # Upload everythings to instagram & get the post's url
    link = upload_image_to_insta(image_path, image_info)

    # Send a message in discord channel
    await send_message_to_discord(
        image_path,
        image_info,
        variantPrompt,
        link,
    )


if __name__ == "__main__":
    asyncio.run(main())
