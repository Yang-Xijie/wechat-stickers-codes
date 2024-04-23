import PIL.Image

for l in range(14):
    stickers = PIL.Image.open(f"./images-screenshots/L{l}.png")
    for i in range(8 if l != 13 else 5):
        a = 72
        # (left, upper, right, lower)
        sticker = stickers.crop((i * a, 0, (i + 1) * a, a))
        sticker.save(f"./images-stickers/{l * 8 + i}.png")
