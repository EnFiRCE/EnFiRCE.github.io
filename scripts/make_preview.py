"""Make a 1200x630 social preview from the hooked-rod result figure."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

root = Path(__file__).resolve().parents[1]
src = Image.open(root / "static" / "images" / "video_forces.png").convert("RGB")

W, H = 1200, 630
canvas = Image.new("RGB", (W, H), "#0f172a")
draw = ImageDraw.Draw(canvas)

# Place the plot on the right with a white panel.
panel = Image.new("RGB", (720, 470), "white")
src_ratio = src.width / src.height
target_w, target_h = 700, 430
if src_ratio > target_w / target_h:
    new_w = target_w
    new_h = int(target_w / src_ratio)
else:
    new_h = target_h
    new_w = int(target_h * src_ratio)
src = src.resize((new_w, new_h), Image.Resampling.LANCZOS)
px = (panel.width - new_w) // 2
py = (panel.height - new_h) // 2
panel.paste(src, (px, py))
canvas.paste(panel, (440, 90))

try:
    title_font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 72)
    sub_font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 26)
    small_font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 20)
except OSError:
    title_font = ImageFont.load_default()
    sub_font = title_font
    small_font = title_font

draw.text((56, 150), "FiRCE", font=title_font, fill="#f8fafc")
draw.text(
    (56, 240),
    "Friction-informed\nRod Contact\nEstimation",
    font=sub_font,
    fill="#93c5fd",
    spacing=8,
)
draw.text(
    (56, 430),
    "Sparse shape + environment\nconstraints  ·  GT 2026",
    font=small_font,
    fill="#cbd5e1",
    spacing=6,
)
draw.rectangle((56, 118, 180, 124), fill="#f97316")

out = root / "static" / "images" / "social_preview.png"
canvas.save(out, "PNG", optimize=True)
print(f"wrote {out} {out.stat().st_size} bytes")

# PNG favicon fallback
icon = Image.new("RGBA", (256, 256), (15, 23, 42, 255))
d = ImageDraw.Draw(icon)
d.arc((40, 20, 210, 230), start=200, end=320, fill=(147, 197, 253, 255), width=18)
d.line((150, 58, 210, 36), fill=(249, 115, 22, 255), width=14)
d.line((210, 36, 198, 88), fill=(249, 115, 22, 255), width=14)
d.ellipse((118, 42, 142, 66), fill=(248, 250, 252, 255))
icon.save(root / "static" / "images" / "favicon.png")
icon.resize((32, 32), Image.Resampling.LANCZOS).save(
    root / "static" / "images" / "favicon.ico", format="ICO"
)
print("wrote favicon.png and favicon.ico")
