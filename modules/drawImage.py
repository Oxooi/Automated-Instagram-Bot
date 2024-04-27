from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import time


def draw_text_on_image(image_location: str, variant_prompt: str) -> None:
    print("[*] Writing the watermarks")
    time.sleep(1)

    try:
        font = ImageFont.truetype("modules/jersey.ttf", 25)
        font3 = ImageFont.truetype("modules/jersey.ttf", 25)

        img = Image.open(image_location)
        draw = ImageDraw.Draw(img)

        # draw.text((↔, ↕️), "TEXT TO WRITE", (r,g,b), font=font)
        draw.text((10, 950), "@liminalaidays\nDall-E3, GPT", (255, 255, 255), font=font)
        draw.text((10, 10), variant_prompt, (255, 255, 255), font=font3)

        img.save(image_location)
        print("[*] Watermak writted")
    except Exception as e:
        print(f"[!] Error: {e}")
        print("[!] Failed to write the watermarks")
        exit(1)


def main():
    draw_text_on_image("img/test.png", "TEST")


if __name__ == "__main__":
    main()
