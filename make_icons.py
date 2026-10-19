from PIL import Image, ImageDraw, ImageFont
import pathlib
HERE = pathlib.Path(__file__).parent

def make_icon(size, out):
    # Red rounded square with white blood drop + "10"
    img = Image.new("RGBA", (size, size), (185, 28, 28, 255))
    d = ImageDraw.Draw(img)
    # white circle badge
    pad = int(size * 0.12)
    d.ellipse([pad, pad, size - pad, size - pad], fill=(255, 255, 255, 255))
    # red drop (simple triangle+circle approx)
    cx, cy, r = size // 2, int(size * 0.44), int(size * 0.16)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(185, 28, 28, 255))
    d.polygon([(cx, cy - r * 2.2), (cx - r * 1.1, cy), (cx + r * 1.1, cy)], fill=(185, 28, 28, 255))
    # text "10"
    try:
        font = ImageFont.truetype("arial.ttf", int(size * 0.22))
    except Exception:
        font = ImageFont.load_default()
    txt = "10"
    bbox = d.textbbox((0, 0), txt, font=font)
    tw = bbox[2] - bbox[0]
    d.text(((size - tw) / 2, size * 0.62), txt, fill=(185, 28, 28, 255), font=font)
    img.convert("RGB").save(out, "PNG")
    print(f"wrote {out} ({size}x{size})")

make_icon(192, HERE / "icon-192.png")
make_icon(512, HERE / "icon-512.png")
print("Done - icons generated for manifest PWA")
