import os

from dotenv import load_dotenv

load_dotenv()


def dalleGen(client: object) -> str:

    print("[*] Generating the image with Dall-E 3")

    prompt = os.environ.get("DALLE_PROMPT")
    size = os.environ.get("DALLE_SIZE")
    quality = os.environ.get("DALLE_QUALITY")
    model = os.environ.get("DALLE_MODEL")

    response = client.images.generate(
        model=model,
        prompt=prompt,
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
