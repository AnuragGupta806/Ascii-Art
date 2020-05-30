from PIL import Image, ImageDraw, ImageFont
import math

# function to get the respective ascii character of the pixel value 
def getSomeChar(h):
    chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-  _+~<>i!lI;:,\"^`'. "[::-1]
    charArr = list(chars)
    l = len(charArr)
    mul = l / 256
    return charArr[math.floor(h * mul)]


image = Image.open("minion.jpg")
scaleFac = 0.8              # Scaling down the image size to reduce computational power consumption
charWidth = 12
charHeight = 18
w, h = image.size
image = image.resize((int(scaleFac * w), int(scaleFac * h * (charWidth / charHeight))), Image.NEAREST)     # resizing the output image
w, h = image.size
pixels = image.load()

font = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)                  # extracting font style for characters from windows fonts,can be anything
outputImage = Image.new('RGB', (charWidth * w, charHeight * h), color=(25, 25, 25))    # preparing a blank canvas on which the new image is drawn 
draw = ImageDraw.Draw(outputImage)

for i in range(h):
    for j in range(w):
        r, g, b = pixels[j, i]
        grey = int((r / 3 + g / 3 + b / 3))
        pixels[j, i] = (grey, grey, grey)
        draw.text((j * charWidth, i * charHeight), getSomeChar(grey), font=font, fill=(r, g, b))           # drawing characters on the canvas

outputImage.save("ascii_art.jpg")                      

