import random
import os

from dotenv import load_dotenv

load_dotenv()


# Function to choose a random variant for the prompt
def choose_random_variant() -> str:
    variantPrompt: list[str] = [
        "",
        "Made of electronics",
        "3d wireframe",
        "Artificial lighting",
        "Film noir",
        "Analog film style, 35mm film style",
        "Artificial lighting,",
        "Aerial view",
        "Pinhole camera style",
    ]

    return random.choice(variantPrompt)


# Function to generate the image with Dall-E 3
def dalleGen(client: object) -> str:

    print("[*] Generating the image with Dall-E 3")

    prompt: str = os.environ.get("DALLE_PROMPT")
    size: str = os.environ.get("DALLE_SIZE")
    quality: str = os.environ.get("DALLE_QUALITY")
    model: str = os.environ.get("DALLE_MODEL")

    variantPrompt: str = choose_random_variant()

    response = client.images.generate(
        model=model,
        prompt=f"{prompt}{variantPrompt}",
        size=size,
        quality=quality,
        n=1,
    )

    try:
        image_url = response.data[0].url
    except KeyError:
        print("[!] An error occurred while generating the image")
        return None

    print("[*] Image created, Here the url :")

    print(image_url)

    try:
        with open("dalleLink.txt", "w") as fh:
            fh.write(image_url)
    except FileNotFoundError:
        with open("dalleLink.txt", "x") as fh:
            fh.write(image_url)

    return image_url
