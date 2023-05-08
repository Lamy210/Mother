from PIL import Image
import fitz

with fitz.open('./rsy2023sem1_GP21A122-5.pdf') as pdf:
    page = pdf[0]
    width = int(page.rect.width)
    height = int(page.rect.height)
    x1, y1 = 1, 1
    x2, y2 = width/10, height/10
    clip = fitz.Rect(x1, y1, x2, y2)
    pix = page.get_pixmap(matrix=fitz.Matrix(), clip=clip)

    # Convert to PIL Image
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    img = img.resize((width, height))

    # Save with PIL
    img.save('a.jpg', 'JPEG')
