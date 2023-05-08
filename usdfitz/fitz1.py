import fitz

# PDFファイルを開く
with fitz.open('./rsy2023sem1_GP21A122-5.pdf') as pdf:
    # 1ページ目を取得する
    page = pdf[0]
    # ページの矩形を取得する
    #rect = page.rect
    # ページの幅と高さを取得する
    width =int(page.rect.width)
    height =int(page.rect.height)
    # 切り抜く領域を決定する
    x1,y1 = 0,0
    x2,y2 = width,height
    # 切り抜いたイメージを取得する
    
    print("width:"+str(width)+"height:"+str(height))
    print("\nx1:"+str(x1)+"y1:"+str(y1))
    print("\nx2:"+str(x2)+"y2:"+str(y2)+"\n")
    clip = fitz.Rect(x1, y1, x2, y2)
    pix = page.get_pixmap(matrix=fitz.Matrix(), clip=clip)
    #pix.set_dpi(72,72)
    pix.save('a.png')
    

