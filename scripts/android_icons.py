# Capacitor android loyihasiga ikonkalarni qo'yadi (build paytida avtomatik ishlaydi)
import os, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
from make_icons import icon
res = "android/app/src/main/res"
sizes = {"mdpi":48,"hdpi":72,"xhdpi":96,"xxhdpi":144,"xxxhdpi":192}
for d,s in sizes.items():
    p = f"{res}/mipmap-{d}"
    if not os.path.isdir(p): continue
    icon(s).save(f"{p}/ic_launcher.png"); icon(s).save(f"{p}/ic_launcher_round.png")
    fg = icon(int(s*108/48), pad=0.17, rounded=False)  # adaptive foreground
    fg.save(f"{p}/ic_launcher_foreground.png")
bg = f"{res}/values/ic_launcher_background.xml"
open(bg,"w").write('<?xml version="1.0" encoding="utf-8"?>\n<resources><color name="ic_launcher_background">#0F766E</color></resources>\n')
print("ikonkalar qo'yildi")
