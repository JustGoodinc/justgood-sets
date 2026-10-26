"""Make the 180x180 iPhone home-screen icon from the logo embedded in the page.
Usage: make_icon.py <pylibs> <page.html> <out.png>"""
import base64
import io
import re
import sys

sys.path.insert(0, sys.argv[1])
from PIL import Image, ImageDraw, ImageFilter  # noqa: E402

page = open(sys.argv[2], encoding="utf-8").read()
logo = Image.open(io.BytesIO(base64.b64decode(re.search(r'data:image/webp;base64,([A-Za-z0-9+/=]+)', page)[1]))).convert("RGBA")

S = 180 * 4  # draw large, shrink at the end for smooth edges
bg = Image.new("RGBA", (S, S), "#06050c")  # --room
glow = Image.new("RGBA", (S, S), (0, 0, 0, 0))
ImageDraw.Draw(glow).ellipse((S * .1, S * .2, S * .9, S * .8), fill="#2a1d5c")  # --room-glow, a little brighter
bg.alpha_composite(glow.filter(ImageFilter.GaussianBlur(S * .12)))

w = int(S * .86)
logo = logo.resize((w, round(logo.height * w / logo.width)), Image.LANCZOS)
bg.alpha_composite(logo, ((S - logo.width) // 2, (S - logo.height) // 2))
bg.convert("RGB").resize((180, 180), Image.LANCZOS).save(sys.argv[3], optimize=True)
print(sys.argv[3])
