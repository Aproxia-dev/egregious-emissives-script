from PIL import Image
import glob
from os import makedirs

keywords = ["bloom", "emissive"]
files = []
bad_keywords = []

for kw in keywords:
    files += glob.glob("./src/**/*{}*.png".format(kw), recursive=True)
    bad_keywords.append("_no_{}".format(kw))


for file in files:
    if not any(kw in file for kw in bad_keywords):
        img = Image.open(file)

        blank = Image.new('RGBA', img.size, '#00000000')
        emissive = Image.new('RGBA', img.size, '#000000fe')

        overlay = Image.composite(img.convert("LA"), blank, img.convert("L"))

        folders = file.split("/")
        folders[1] = "dst"
        folders[-1] = folders[-1].replace(".png", "_s.png")
        output = "/".join(folders)
        folders.pop()

        outputImg = Image.composite(emissive, blank, overlay)

        makedirs("/".join(folders), exist_ok=True)
        outputImg.save(output, 'png')
        print(file + " -> " + output)
