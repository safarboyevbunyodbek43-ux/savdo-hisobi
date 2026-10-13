# Ikonka generatori (PIL). Ishlatish: python3 scripts/make_icons.py
from PIL import Image, ImageDraw
def icon(size, pad=0.0, rounded=True):
    S=size*4
    im=Image.new("RGBA",(S,S),(0,0,0,0)); d=ImageDraw.Draw(im)
    if rounded: d.rounded_rectangle([0,0,S-1,S-1],radius=int(S*.22),fill=(15,118,110,255))
    else: d.rectangle([0,0,S,S],fill=(15,118,110,255))
    # ustun diagrammasi + strelka
    u=S*(1-2*pad)/10; ox=S*pad; oy=S*pad
    w=(255,255,255,255)
    for i,(h) in enumerate([3,5,4,7]):
        x=ox+u*(1.6+i*1.75); d.rounded_rectangle([x,oy+u*(8.4-h),x+u*1.2,oy+u*8.4],radius=int(u*.2),fill=w)
    d.line([ox+u*1.6,oy+u*4.2,ox+u*4.2,oy+u*2.6,ox+u*6,oy+u*3.4,ox+u*8.6,oy+u*1.4],fill=(253,224,71,255),width=int(u*.34),joint="curve")
    d.polygon([(ox+u*8.9,oy+u*1.0),(ox+u*8.9,oy+u*2.5),(ox+u*7.4,oy+u*1.5)],fill=(253,224,71,255))
    return im.resize((size,size),Image.LANCZOS)
if __name__=="__main__":
    icon(512).save("www/icon-512.png"); icon(192).save("www/icon-192.png")
    icon(512,pad=0.1,rounded=False).save("www/icon-maskable-512.png")
    icon(256).save("build-icon-256.png")
    icon(256).save("electron/icon.ico",sizes=[(256,256),(128,128),(64,64),(48,48),(32,32),(16,16)])
