from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageFont
from PIL import ImageDraw


image = Image.open("stinkbug.png").convert("RGBA")
watermark_image = Image.new('RGBA', image.size, (255,255,255,0))
width, height = image.size

draw = ImageDraw.Draw(watermark_image)
font = ImageFont.truetype("Ubuntu-Regular.ttf", 35)

draw.text((width/23, height/2.25), "Mohammad Hossein Khademi", 
          (255, 255, 255, 50), font=font)
combined = Image.alpha_composite(image, watermark_image)

combined.show()

combined_rgb = combined.convert('RGB')

combined_rgb.save('watermarked.jpg')
