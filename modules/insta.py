import time
import os
import logging

from instagrapi import Client
from instagrapi.exceptions import LoginRequired
from dotenv import load_dotenv

load_dotenv()


def upload_image_to_insta(image, info):
    # Setup logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Get the account's info from the .env file
    ACCOUNT_USERNAME = os.environ.get("INSTA_ACCOUNT_USERNAME")
    ACCOUNT_PASSWORD = os.environ.get("INSTA_ACCOUNT_PASSWORD")

    cl = Client(request_timeout=7)
    # cl.load_settings("session.json")
    cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
    cl.delay_range = [1, 3]
    # cl.get_timeline_feed()  # check session

    # FOR TEST PURPOSE ONLY
    # Get the content of the "content.txt" file, which is the description text
    # with open("content.txt", "r", encoding="utf-8") as desc_file:
    #     lines = desc_file.read()

    # Upload the media
    try:
        media = cl.photo_upload(
            image,
            info,  # Use the actual content from the file
            extra_data={"disable_comments": 1},
        )
        print(media.model_dump())
        print("[*] Image uploaded & Post created ")
    except Exception as e:
        logger.error(f"Failed to upload photo: {e}")
