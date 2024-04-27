import os

from modules.dall import dalleGen
from modules.downloadImage import downloadImage
from modules.gptVision import describe_image
from modules.insta import upload_image_to_insta

from openai import OpenAI
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get the OPENAI infos
openai_api_key = os.environ.get("MY_OPENAI_API_KEY")
client = OpenAI(
    api_key=openai_api_key,
)


def main() -> None:
    # Generate the image with Dall-E
    image, variantPrompt = dalleGen(client)

    # Download the image in local dir
    image_path = downloadImage(image, variantPrompt)

    # Get the image : title, description & hashtags with GPT-Vision
    image_info = describe_image(image_path, openai_api_key)

    # Upload everythings to instagram
    upload_image_to_insta(image_path, image_info)


if __name__ == "__main__":
    main()
