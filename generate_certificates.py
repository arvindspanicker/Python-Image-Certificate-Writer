from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("Certificate/certificate.jpg")
width,height = img.size

draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Font/times-new-roman.ttf", 30)
offset = 10
y_coordinate = int(width/2 - font.getsize("Sample Text")[0]/2) - offset
draw.text((y_coordinate,435),"Sample Text",(255,0,0),font=font)
img.save('sample-out.jpg')