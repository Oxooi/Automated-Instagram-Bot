import time
import os
import logging

from instagrapi import Client
from instagrapi.exceptions import LoginRequired
from dotenv import load_dotenv

load_dotenv()

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
with open("content.txt", "r", encoding="utf-8") as desc_file:
    lines = desc_file.read()

# Upload the media
try:
    media = cl.photo_upload(
        "img/42f17979-f59c-11ee-9b47-50c2e81ad7cc.jpg",
        "Petit chat tout mignon",  # Use the actual content from the file
        extra_data={"disable_comments": 1},
    )
    print(media.model_dump())
except Exception as e:
    logger.error(f"Failed to upload photo: {e}")

time.sleep(3)

# Get the list of all media from your account
user_id = cl.user_id_from_username(ACCOUNT_USERNAME)
media_list = cl.user_medias(user_id, 1)  # Fetch only the most recent media

if not media_list:
    print("No media found on this account.")
else:
    # Get the most recent media
    recent_media = media_list[0]

    # Now you have the media, you can comment on it
    comment_text = "Hey !!! UwU"
    cl.media_comment(recent_media.pk, comment_text)
    print(f"Commented on the last post: {comment_text}")
