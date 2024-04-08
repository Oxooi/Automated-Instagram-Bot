import requests
import uuid
import os


def downloadImage(image):

    print("[*] Downloading the image in local path")

    # Get the url of the image
    url_image = image

    # Download the image
    response = requests.get(url_image)

    # Specify the image location
    path = f"img/{uuid.uuid1()}.jpg"

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

    return path
