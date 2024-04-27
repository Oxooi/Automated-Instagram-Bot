import requests
import uuid
import os
from modules.drawImage import draw_text_on_image


def downloadImage(image: str, variantPrompt: str) -> str:

    print("[*] Downloading the image in local path")

    # Get the url of the image
    url_image: str = image

    # Download the image
    response: str = requests.get(url_image)

    # Specify the image location
    path: str = f"img/{uuid.uuid1()}.jpg"

    # Save the image
    try:
        # Detect if the img folder exists
        with open(path, "wb") as file:
            file.write(response.content)
    except FileNotFoundError:
        # If the folder doesn't exist, create it
        os.mkdir("img")
        with open(path, "wb") as file:
            file.write(response.content)

    print(f"[*] The image has been saved as : {path}")

    draw_text_on_image(path, variantPrompt)

    return path
