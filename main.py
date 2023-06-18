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
        overlay = Image.open(file).convert('LA')
        folders = file.split("/")
        folders[1] = "dst"
        folders[-1] = folders[-1].replace(".png", "_s.png")
        output = "/".join(folders)
        folder.pop()

        ne = Image.new('RGBA', overlay.size, '#00000000')
        em = Image.new('RGBA', overlay.size, '#ff0000fe')

        outputImg = Image.composite(em, ne, overlay)

        makedirs("/".join(folders), exist_ok=True)
        outputImg.save(output, 'png')
        print(file + " -> " + output)
