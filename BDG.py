from PIL import Image, ImageDraw, ImageFont, ImageFilter
from random import randint
import os

ims = [
    Image.open(f"{os.path.dirname(__file__)}\R\A1.png"),
    Image.open(f"{os.path.dirname(__file__)}\R\A2.png"),
    Image.open(f"{os.path.dirname(__file__)}\R\A3.png"),
    Image.open(f"{os.path.dirname(__file__)}\R\A4.png"),
    Image.open(f"{os.path.dirname(__file__)}\R\A5.png"),
    Image.open(f"{os.path.dirname(__file__)}\R\A6.png"),
    Image.open(f"{os.path.dirname(__file__)}\R\A7.png")
]

img = Image.new('RGBA', (400, 400), color = (randint(0,255),randint(0,255),randint(0,255)))
draw = ImageDraw.Draw(img)

def set_img(valor):
    i = 0
    while i <= valor - 1:
        i = i+1
        img.paste(ims[randint(0,6)],(randint(0,290),randint(0,290)))

fnt = [
    ImageFont.truetype(f"{os.path.dirname(__file__)}\F\ARIAL.TTF",randint(60,60)),
    ImageFont.truetype(f"{os.path.dirname(__file__)}\F\Corbel.ttf",randint(60,60)),
    ImageFont.truetype(f"{os.path.dirname(__file__)}\F\ALGER.TTF",randint(60,60)),
    ImageFont.truetype(f"{os.path.dirname(__file__)}\F\ANTQUAB.TTF",randint(60,60)),
    ImageFont.truetype(f"{os.path.dirname(__file__)}\F\ANTQUAI.TTF",randint(60,60)),
    ImageFont.truetype(f"{os.path.dirname(__file__)}\F\BELLI.TTF",randint(60,60)),
    ImageFont.truetype(f"{os.path.dirname(__file__)}\F\BAUHS93.TTF",randint(60,60)),
    ImageFont.truetype(f"{os.path.dirname(__file__)}\F\BRADHITC.TTF",randint(60,60))
]
xy=(
    (50,50),
    (220,50),
    (220,260),
    (50,260)
)

set_img(4)

draw.text((90,180), "Bom Dia", font=fnt[randint(0,7)], fill=(randint(0,250),randint(0,250),randint(0,250)),stroke_width=1)
blurImage = img.filter(ImageFilter.BoxBlur(radius=randint(0,30)))
blurImage = img.filter(ImageFilter.SHARPEN)

img.save(f'{os.path.abspath(__file__)}pil_text.png',quality=100)
img.show()
