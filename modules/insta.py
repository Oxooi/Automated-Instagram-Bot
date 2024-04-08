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
    cl.load_settings("session.json")
    cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
    cl.get_timeline_feed()  # check session
    cl.delay_range = [1, 3]

    # Upload the media
    try:
        media = cl.photo_upload(
            image,
            info,  # Use the actual content from the file
            # extra_data={"disable_comments": 1},
        )
        print(media.model_dump())
        print("[*] Image uploaded & Post created ")
    except Exception as e:
        logger.error(f"Failed to upload photo: {e}")


    #### This part is here for debugging purposes only ####

    # # Get the list of all media from your account
    # user_id = cl.user_id_from_username(ACCOUNT_USERNAME)
    # media_list = cl.user_medias(user_id, 1)  # Fetch only the most recent media

    # # Get the media id from the most recent media
    # media_id = media_list[0].id

    # # Add a comment to the media
    # try:
    #     cl.media_comment(media_id, info)
    #     print("[*] Comment added to the post")
    # except Exception as e:
    #     logger.error(f"Failed to add comment to the post: {e}")

    # # Change the caption of the media
    # try:
    #     cl.media_edit(media_id, info)
    #     print("[*] Caption updated")
    # except Exception as e:
    #     logger.error(f"Failed to update caption: {e}")

