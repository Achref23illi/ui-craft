"""Build contact sheets: 6 screens per sheet (3 x 2), labelled with app name and index."""
import json, os, sys, glob
from PIL import Image, ImageDraw, ImageFont
apps = {str(a['id']): a['name'] for a in json.load(open('apps.json'))}
os.makedirs('sheets', exist_ok=True)
S = 0.62; W, H = int(488*S), int(1057*S); PAD = 10; LBL = 26; COLS, ROWS = 3, 2
try: font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 16)
except Exception: font = ImageFont.load_default()
only = sys.argv[1:]  # optional app ids
made = 0
for appdir in sorted(glob.glob('screens/*'), key=lambda p:int(os.path.basename(p))):
    app = os.path.basename(appdir)
    if only and app not in only: continue
    files = sorted(glob.glob(f'{appdir}/*.jpg'))
    files = [f for f in files if os.path.getsize(f) > 1000]
    for si in range(0, len(files), COLS*ROWS):
        out = f'sheets/{int(app):03d}-{apps.get(app, app).replace("/", "-")[:20]}-{si//(COLS*ROWS)+1:02d}.jpg'
        if os.path.exists(out): continue
        sheet = Image.new('RGB', (COLS*(W+PAD)+PAD, ROWS*(H+PAD+LBL)+PAD), (28,28,30))
        d = ImageDraw.Draw(sheet)
        for k, f in enumerate(files[si:si+COLS*ROWS]):
            try: im = Image.open(f).convert('RGB').resize((W, H))
            except Exception: continue
            x = PAD + (k % COLS)*(W+PAD); y = PAD + (k // COLS)*(H+PAD+LBL)
            sheet.paste(im, (x, y+LBL))
            d.text((x, y+4), f'{apps.get(app, app)} · {si+k+1}', fill=(235,235,235), font=font)
        sheet.save(out, quality=82); made += 1
print('sheets made', made, 'total', len(glob.glob('sheets/*.jpg')))
