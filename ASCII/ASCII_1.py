from PIL import Image

chars = "@%#*+=-:. "

img = Image.open("image.jpg") # your image here  
img = img.resize((100, 50))
img = img.convert("L")

for y in range(img.height):
    line = ""
    for x in range(img.width):
        pixel = img.getpixel((x, y))
        line += chars[pixel * len(chars) // 256]
    print(line)