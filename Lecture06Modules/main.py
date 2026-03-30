from rembg import remove
from PIL import Image

input = Image.open('p2.jpeg')
output = remove(input)
output.save('output.png')