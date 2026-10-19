from PIL import Image
import pathlib
HERE = pathlib.Path(__file__).parent
BOTTOM_CUT = 0.22  # cut 22% from bottom where cell name label sits
TOP_CUT = 0.04     # cut 4% from top
for i in range(1, 11):
    src = HERE / f"real{i}.webp"
    if not src.exists():
        print(f"missing {src}"); continue
    im = Image.open(src).convert("RGB")
    w, h = im.size
    top = int(h * TOP_CUT)
    bottom = int(h * (1 - BOTTOM_CUT))
    cropped = im.crop((0, top, w, bottom))
    # backup original once
    bak = HERE / f"real{i}_orig.webp"
    if not bak.exists():
        im.save(bak)
        print(f"backup {bak.name}")
    cropped.save(src, "WEBP", quality=90)
    print(f"cropped real{i}.webp: {w}x{h} -> {cropped.size[0]}x{cropped.size[1]}")
print("Done - bottom labels removed from real1-real10.webp")
