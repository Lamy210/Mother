import fitz
from PIL import Image
with fitz.open('./rsy2023sem1_GP21A122-5.pdf') as pdf:
    page = pdf[0]
    rect = page.rect
    width = int(rect.width)
    height = int(rect.height)
    x1, y1 = 1, 1
    x2, y2 = width, height
    rotation = int(page.rotation)
    clip = fitz.Rect(x1, y1, x2, y2)
    pix = page.get_pixmap(matrix=fitz.Matrix().preRotate(90), clip=clip)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    img.save('a.png')
