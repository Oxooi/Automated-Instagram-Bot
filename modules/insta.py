import os
import logging

from instagrapi import Client
from instagrapi.exceptions import LoginRequired
from dotenv import load_dotenv

load_dotenv()


def upload_image_to_insta(image: str, info: str) -> None:

    # Setup logging
    logging.basicConfig(level=logging.INFO)
    logger: str = logging.getLogger(__name__)

    # Get the account's info from the .env file
    ACCOUNT_USERNAME = os.environ.get("INSTA_ACCOUNT_USERNAME")
    ACCOUNT_PASSWORD = os.environ.get("INSTA_ACCOUNT_PASSWORD")

    cl: object = Client(request_timeout=7)
    # cl.load_settings("session.json")
    cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
    cl.dump_settings("session.json")
    # cl.get_timeline_feed()  # check session
    cl.delay_range = [1, 3]

    # Upload the media
    try:
        media = cl.photo_upload(
            image,
            info,
            extra_data={"disable_comments": 1, "disable_like": 1},
        )
        print(media.model_dump())
        print("[*] Image uploaded & Post created ")
    except Exception as e:
        logger.error(f"Failed to upload photo: {e}")
