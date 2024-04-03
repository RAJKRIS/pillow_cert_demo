import os

from PIL import Image, ImageFont, ImageDraw
from dotenv import load_dotenv

load_dotenv(".env", override=True)

# get and set the config vars from .env
FONT_PATH, FONT_SIZE, FONT_COLOR_CODE = os.environ.get("FONT_PATH"), os.environ.get("FONT_SIZE", 200), os.environ.get("FONT_COLOR_CODE", "#324868")
TEXT = os.environ.get("TEXT", "John Doe")
INPUT_IMAGE_PATH, OUTPUT_IMAGE_PATH = os.environ.get("INPUT_IMAGE_PATH"), os.environ.get("OUTPUT_IMAGE_PATH")
TEXT_X, TEXT_Y = int(os.environ.get("TEXT_X", 2600)), int(os.environ.get("TEXT_Y", 2000))
QR_PATH = os.environ.get("QR_PATH", "qr.png")
QR_X, QR_Y = int(os.environ.get("QR_X", 2600)), int(os.environ.get("QR_Y", 2500))
# open input image
im1 = Image.open(INPUT_IMAGE_PATH)

# Drawing the text on the picture
font = ImageFont.truetype(FONT_PATH, size=FONT_SIZE)
draw = ImageDraw.Draw(im1)
draw.text((TEXT_X, TEXT_Y), TEXT, FONT_COLOR_CODE, font=font)

# qr image
qr = Image.open(QR_PATH)
# resize image
qr = qr.resize((350, 350))
# attach the qr image
print(QR_X, QR_Y)
im1.paste(qr, (QR_X, QR_Y))

# Save the image with a new name
im1.save(OUTPUT_IMAGE_PATH)