import math, random, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops

random.seed(7); np.random.seed(7)
S = 2                       # supersampling
W = 3000 * S
FONTS = sys.argv[1]
OUT = sys.argv[2]
WITH_TEXT = len(sys.argv) > 3 and sys.argv[3] == "texto"

def s(v): return int(round(v * S))
def P(pts): return [(s(x), s(y)) for x, y in pts]

def hexc(h, a=255):
    h = h.lstrip('#'); return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), a)

# ---------- palette ----------
NIGHT_TOP = hexc('#070f1c'); NIGHT_LOW = hexc('#1b3049')
SEA_FAR = hexc('#13283d'); SEA_NEAR = hexc('#0a1726')
MOON = hexc('#efe5cb'); LIME = hexc('#e6dcc3'); ROOF = hexc('#7a3b22')
GOLD = hexc('#d9a441'); GOLD_HOT = hexc('#ffd27a'); OCHRE = hexc('#8a6a3a')
FOREST_FAR = hexc('#14262a'); FOREST_MID = hexc('#0c1a1b'); ROCK = hexc('#090f12')
INK = hexc('#05080b'); RIM = hexc('#9fb3c4')

img = Image.new('RGBA', (W, W), INK)

def layer(): return Image.new('RGBA', (W, W), (0, 0, 0, 0))
def mask(): return Image.new('L', (W, W), 0)

def paste(base, top, m=None):
    if m is None: base.alpha_composite(top)
    else:
        t = top.copy(); a = ImageChops.multiply(t.getchannel('A'), m); t.putalpha(a); base.alpha_composite(t)

def vgrad(y0, y1, c0, c1):
    L = layer(); d = ImageDraw.Draw(L)
    for y in range(s(y0), s(y1)):
        t = (y - s(y0)) / max(1, s(y1) - s(y0))
        c = tuple(int(c0[i] + (c1[i] - c0[i]) * t) for i in range(4))
        d.line([(0, y), (W, y)], fill=c)
    return L

def hatch(m, spacing, angle, color, width=1.0, jitter=0.6, broken=0.0, seed=0):
    rnd = random.Random(seed)
    L = layer(); d = ImageDraw.Draw(L)
    a = math.radians(angle); ca, sa = math.cos(a), math.sin(a)
    diag = W * 1.5; n = int(diag * 2 / s(spacing))
    for i in range(-n // 2, n // 2):
        off = i * s(spacing) + rnd.uniform(-jitter, jitter) * S
        cx, cy = W / 2 - sa * off, W / 2 + ca * off
        x0, y0 = cx - ca * diag, cy - sa * diag
        x1, y1 = cx + ca * diag, cy + sa * diag
        if broken:
            segs = int(diag * 2 / s(40));
            for k in range(segs):
                if rnd.random() < broken: continue
                t0, t1 = k / segs, (k + rnd.uniform(0.55, 0.95)) / segs
                d.line([(x0 + (x1 - x0) * t0, y0 + (y1 - y0) * t0), (x0 + (x1 - x0) * t1, y0 + (y1 - y0) * t1)], fill=color, width=max(1, s(width)))
        else:
            d.line([(x0, y0), (x1, y1)], fill=color, width=max(1, s(width)))
    paste(img, L, m)

def ridge(x0, x1, base, amp, octaves, seed, step=6):
    rnd = random.Random(seed); ph = [rnd.uniform(0, 6.28) for _ in octaves]
    pts = []
    for x in range(int(x0), int(x1) + 1, step):
        y = base(x)
        for (f, a), p in zip(octaves, ph): y += amp * a * math.sin(x * f + p)
        pts.append((x, y))
    return pts

def glow(cx, cy, r, color, strength=1.0):
    L = layer(); d = ImageDraw.Draw(L)
    for k in range(40, 0, -1):
        rr = r * k / 40; al = int(color[3] * strength * (1 - k / 40) ** 2 / 3)
        d.ellipse([s(cx - rr), s(cy - rr), s(cx + rr), s(cy + rr)], fill=color[:3] + (al,))
    img.alpha_composite(L.filter(ImageFilter.GaussianBlur(s(r / 12))))

# ---------- frame geometry ----------
M = 96                     # inner image margin (frame width)
HOR = 1640                 # horizon

# ---------- sky ----------
sky = mask(); ImageDraw.Draw(sky).rectangle([0, 0, W, s(HOR)], fill=255)
img.alpha_composite(vgrad(0, HOR, NIGHT_TOP, NIGHT_LOW))
MX, MY, MR = 860, 1395, 215
# moon halo
for i, rr in enumerate(range(MR + 40, MR + 560, 52)):
    L = layer(); d = ImageDraw.Draw(L)
    al = int(34 * (1 - i / 10) ** 1.6)
    d.ellipse([s(MX - rr), s(MY - rr), s(MX + rr), s(MY + rr)], outline=(214, 205, 176, al), width=s(1.6))
    paste(img, L, sky)
glow(MX, MY, 900, (120, 150, 175, 120), 1.0)
# engraved sky lines: horizontal, slightly broken, denser to top
for band, (y0, y1, sp, al) in enumerate([(0, 600, 7, 70), (600, 1200, 9, 55), (1200, HOR, 11, 40)]):
    m = mask(); ImageDraw.Draw(m).rectangle([0, s(y0), W, s(y1)], fill=255)
    m = ImageChops.multiply(m, sky)
    hatch(m, sp, 0, (70, 92, 122, int(al * .55)), width=1.3, jitter=1.0, broken=0.10, seed=10 + band)
# stars (sparse, tiny)
L = layer(); d = ImageDraw.Draw(L); rnd = random.Random(3)
for _ in range(170):
    x, y = rnd.uniform(M + 20, 2900), rnd.uniform(M + 20, 1250)
    if math.hypot(x - MX, y - MY) < 650: continue
    r = rnd.choice([1.2, 1.4, 1.8, 2.4]); al = rnd.randint(90, 200)
    d.ellipse([s(x - r), s(y - r), s(x + r), s(y + r)], fill=(232, 224, 200, al))
paste(img, L, sky)

# moon disc with engraved rings
L = layer(); d = ImageDraw.Draw(L)
d.ellipse([s(MX - MR), s(MY - MR), s(MX + MR), s(MY + MR)], fill=MOON)
img.alpha_composite(L)
mm = mask(); ImageDraw.Draw(mm).ellipse([s(MX - MR), s(MY - MR), s(MX + MR), s(MY + MR)], fill=255)
L = layer(); d = ImageDraw.Draw(L)
for rr in range(12, MR, 13):
    d.ellipse([s(MX - rr + 18), s(MY - rr + 10), s(MX + rr + 18), s(MY + rr + 10)], outline=(170, 150, 112, 34), width=s(1.4))
for (ox, oy, r) in [(-70, -40, 52), (55, 45, 38), (-20, 90, 30), (80, -80, 24)]:
    d.ellipse([s(MX + ox - r), s(MY + oy - r), s(MX + ox + r), s(MY + oy + r)], fill=(190, 174, 138, 60))
paste(img, L, mm)

# morning star, low near horizon
SX, SY = 1265, 1535
glow(SX, SY, 120, (255, 230, 170, 160), 1.0)
L = layer(); d = ImageDraw.Draw(L)
for ang, ln, w in [(0, 58, 2.2), (90, 58, 2.2), (45, 22, 1.4), (135, 22, 1.4)]:
    a = math.radians(ang); dx, dy = math.cos(a) * ln, math.sin(a) * ln
    d.line([(s(SX - dx), s(SY - dy)), (s(SX + dx), s(SY + dy))], fill=(255, 244, 214, 230), width=s(w))
d.ellipse([s(SX - 6), s(SY - 6), s(SX + 6), s(SY + 6)], fill=(255, 248, 228, 255))
img.alpha_composite(L)

# ---------- distant headlands on the left horizon ----------
far = ridge(0, 760, lambda x: HOR - 70 + (x / 760) ** 2 * 70, 24, [(0.006, 1), (0.019, .4)], 4)
L = layer(); ImageDraw.Draw(L).polygon(P(far + [(760, HOR), (0, HOR)]), fill=(38, 58, 76, 255)); img.alpha_composite(L)

# ---------- sea ----------
SEA_BOTTOM = 2300
sea = mask(); ImageDraw.Draw(sea).rectangle([0, s(HOR), W, s(SEA_BOTTOM)], fill=255)
paste(img, vgrad(HOR, SEA_BOTTOM, SEA_FAR, SEA_NEAR), sea)
hatch(sea, 7, 0, (66, 92, 118, 70), width=1.4, jitter=1.4, broken=0.2, seed=21)
# moon path: stacked short strokes widening toward viewer
L = layer(); d = ImageDraw.Draw(L); rnd = random.Random(5)
y = HOR + 6
while y < SEA_BOTTOM - 10:
    t = (y - HOR) / (SEA_BOTTOM - HOR)
    half = 30 + 210 * t
    for _ in range(2 + int(5 * t)):
        cx = MX + rnd.gauss(0, half * 0.45); ln = rnd.uniform(14, 60) * (0.6 + t)
        al = int(210 * (1 - 0.55 * t) * rnd.uniform(.5, 1))
        d.line([(s(cx - ln / 2), s(y)), (s(cx + ln / 2), s(y))], fill=(236, 226, 196, al), width=s(2.2))
    y += 7 + 9 * t
paste(img, L, sea)
# wave crests across the sea
L = layer(); d = ImageDraw.Draw(L); rnd = random.Random(8)
for _ in range(900):
    y = rnd.uniform(HOR + 10, SEA_BOTTOM - 10); t = (y - HOR) / (SEA_BOTTOM - HOR)
    x = rnd.uniform(0, W / S); ln = rnd.uniform(8, 34) * (0.5 + t)
    d.arc([s(x - ln), s(y - 4), s(x + ln), s(y + 4)], 200, 340, fill=(130, 158, 182, int(55 + 40 * t)), width=s(1.2))
paste(img, L, sea)

# boat procession: lanterns like loose beads on a gentle arc
boats = []
for i in range(13):
    t = i / 12
    x = 300 + 1180 * t; y = 1965 - 150 * math.sin(math.pi * t * 0.9) - 40 * t
    boats.append((x, y))
for (x, y) in boats:
    glow(x, y - 16, 70, (255, 190, 90, 150), 1.0)
L = layer(); d = ImageDraw.Draw(L)
for (x, y) in boats:
    d.polygon(P([(x - 26, y), (x + 26, y), (x + 17, y + 11), (x - 17, y + 11)]), fill=(6, 10, 14, 255))
    d.line([(s(x), s(y)), (s(x), s(y - 20))], fill=(6, 10, 14, 255), width=s(2))
    d.ellipse([s(x - 6), s(y - 30), s(x + 6), s(y - 18)], fill=GOLD_HOT)
    for k in range(1, 6):   # reflection
        d.line([(s(x - 5 + k), s(y + 12 + k * 6)), (s(x + 5 - k), s(y + 12 + k * 6))], fill=(255, 200, 110, 150 - k * 24), width=s(2))
img.alpha_composite(L)

# ---------- coastal flat + beach ----------
shore = ridge(0, 1760, lambda x: SEA_BOTTOM - 12 + 30 * math.sin(x / 300), 6, [(0.03, 1)], 9)
land = shore + [(1760, 3000), (0, 3000)]
L = layer(); ImageDraw.Draw(L).polygon(P(land), fill=(15, 26, 26, 255)); img.alpha_composite(L)
L = layer(); d = ImageDraw.Draw(L)
d.line(P(shore), fill=(200, 188, 150, 200), width=s(5))
d.line(P([(x, y + 9) for x, y in shore]), fill=(150, 140, 110, 90), width=s(3))
img.alpha_composite(L)
landm = mask(); ImageDraw.Draw(landm).polygon(P(land), fill=255)
hatch(landm, 8, -8, (44, 62, 58, 80), width=1.4, jitter=1.2, broken=0.15, seed=31)

# ---------- the town: praça over the old ocara ----------
PX, PY, PRX, PRY = 800, 2540, 175, 64
L = layer(); d = ImageDraw.Draw(L)
d.ellipse([s(PX - PRX - 30), s(PY - PRY - 12), s(PX + PRX + 30), s(PY + PRY + 12)], fill=(48, 50, 40, 255))
d.ellipse([s(PX - PRX), s(PY - PRY), s(PX + PRX), s(PY + PRY)], fill=(196, 184, 150, 255))
d.ellipse([s(PX - PRX + 22), s(PY - PRY + 8), s(PX + PRX - 22), s(PY + PRY - 8)], fill=(176, 162, 128, 255))
img.alpha_composite(L)
# the older trace: a dotted gold ring (the ocara) under the stone
L = layer(); d = ImageDraw.Draw(L)
for k in range(64):
    a = 2 * math.pi * k / 64
    x = PX + (PRX - 60) * math.cos(a); y = PY + (PRY - 22) * math.sin(a)
    d.ellipse([s(x - 4), s(y - 2.4), s(x + 4), s(y + 2.4)], fill=(150, 108, 46, 210))
# chafariz
d.ellipse([s(PX - 26), s(PY - 10), s(PX + 26), s(PY + 10)], fill=(120, 112, 92, 255))
d.ellipse([s(PX - 16), s(PY - 6), s(PX + 16), s(PY + 6)], fill=(46, 70, 86, 255))
d.rectangle([s(PX - 3), s(PY - 26), s(PX + 3), s(PY - 4)], fill=(212, 202, 172, 255))
d.ellipse([s(PX - 8), s(PY - 32), s(PX + 8), s(PY - 22)], fill=(222, 212, 182, 255))
img.alpha_composite(L)

def house(d, x, y, w, h, lit=False, rnd=None):
    d.rectangle([s(x), s(y - h), s(x + w), s(y)], fill=LIME)
    d.rectangle([s(x + w * .62), s(y - h), s(x + w), s(y)], fill=(170, 162, 140, 255))   # shaded side
    d.polygon(P([(x - 5, y - h), (x + w + 5, y - h), (x + w * .5, y - h - h * .55)]), fill=ROOF)
    d.line(P([(x - 5, y - h), (x + w + 5, y - h)]), fill=(50, 26, 16, 255), width=s(2))
    dw = max(5, w * .16)
    d.rectangle([s(x + w * .25), s(y - h * .55), s(x + w * .25 + dw), s(y - h * .2)], fill=(GOLD_HOT if lit else (40, 44, 46, 255)))

# houses on an ellipse around the praça (back row smaller, front row larger)
rnd = random.Random(12)
L = layer(); d = ImageDraw.Draw(L)
spots = []
for k in range(26):
    a = math.pi + math.pi * k / 25          # back arc (toward sea)
    spots.append((PX + (PRX + 70) * math.cos(a), PY + (PRY + 40) * math.sin(a) - 4, 0.8))
for k in range(1, 9):
    for side in (-1, 1):
        spots.append((PX + side * (PRX + 130 + k * 62), PY - 40 + k * 6 + rnd.uniform(-12, 12), 0.85))
for k in range(34):
    a = math.pi * k / 33
    spots.append((PX + (PRX + 75) * math.cos(a) * -1 if False else PX + (PRX + 75) * math.cos(a), PY + (PRY + 52) * math.sin(a) + 30, 1.0))
tries = 0
while tries < 4000 and len(spots) < 260:
    tries += 1
    x = rnd.uniform(150, 1650); y = rnd.uniform(2350, 2930)
    if ((x - PX) / (PRX + 120)) ** 2 + ((y - PY) / (PRY + 95)) ** 2 < 1: continue
    dist = math.hypot((x - PX) / 1.6, y - PY)
    if rnd.random() > math.exp(-dist / 420): continue
    spots.append((x, y, 0.75 + (y - 2350) / 580 * 0.55))
spots.sort(key=lambda t: t[1])
church_x = PX - 12
for x, y, sc in spots:
    if abs(x - church_x) < 70 and y < PY - 60: continue
    w = rnd.uniform(36, 56) * sc; h = rnd.uniform(26, 40) * sc
    house(d, x - w / 2, y, w, h, lit=rnd.random() < 0.18)
img.alpha_composite(L)

# church at the head of the praça, facing the square, tower to the left
L = layer(); d = ImageDraw.Draw(L)
cx, cy = church_x, PY - PRY - 38
d.rectangle([s(cx - 60), s(cy - 120), s(cx + 70), s(cy)], fill=LIME)
d.polygon(P([(cx - 66, cy - 120), (cx + 76, cy - 120), (cx + 5, cy - 168)]), fill=(214, 204, 178, 255))
d.polygon(P([(cx - 66, cy - 120), (cx + 76, cy - 120), (cx + 5, cy - 168)]), outline=(120, 106, 80, 255), width=s(2))
d.rectangle([s(cx - 14), s(cy - 58), s(cx + 22), s(cy)], fill=(58, 40, 28, 255))   # door
d.ellipse([s(cx - 6), s(cy - 112), s(cx + 14), s(cy - 92)], fill=(150, 128, 90, 255))  # oculus
# tower
tx = cx - 112
d.rectangle([s(tx), s(cy - 230), s(tx + 54), s(cy)], fill=LIME)
d.rectangle([s(tx + 32), s(cy - 230), s(tx + 54), s(cy)], fill=(178, 170, 148, 255))
d.rectangle([s(tx + 15), s(cy - 205), s(tx + 39), s(cy - 172)], fill=(30, 26, 22, 255))   # bell opening
d.ellipse([s(tx + 19), s(cy - 196), s(tx + 35), s(cy - 178)], fill=GOLD)           # the bell
d.polygon(P([(tx - 6, cy - 230), (tx + 60, cy - 230), (tx + 27, cy - 292)]), fill=(214, 204, 178, 255))
d.line([(s(tx + 27), s(cy - 292)), (s(tx + 27), s(cy - 322))], fill=(214, 204, 178, 255), width=s(3))
d.line([(s(tx + 17), s(cy - 310)), (s(tx + 37), s(cy - 310))], fill=(214, 204, 178, 255), width=s(3))
img.alpha_composite(L)
glow(tx + 27, cy - 188, 60, (255, 200, 110, 120), 0.8)

# ---------- the serra: mid slope and forest ----------
CRAG_TOP = (2385, 1268)
slope_edge = [(1180, 3000), (1260, 2700), (1420, 2480), (1560, 2300), (1700, 2080), (1860, 1880),
              (2000, 1700), (2120, 1540), (2240, 1400), (2330, 1300)]
mid_ridge = ridge(1500, 3000, lambda x: 1180 + (3000 - x) * -0.02 + max(0, (1900 - x)) * 1.2, 30, [(0.004, 1), (0.013, .5), (0.04, .15)], 13)
# back range behind the crag (paler, farther)
back = ridge(1350, 3000, lambda x: 1020 + max(0, 1900 - x) * 1.05, 40, [(0.003, 1), (0.011, .45), (0.035, .12)], 17)
L = layer(); ImageDraw.Draw(L).polygon(P(back + [(3000, HOR + 200), (1350, HOR + 200)]), fill=(22, 40, 46, 255)); img.alpha_composite(L)
bm = mask(); ImageDraw.Draw(bm).polygon(P(back + [(3000, HOR + 200), (1350, HOR + 200)]), fill=255)
hatch(bm, 7, 6, (52, 80, 88, 80), width=1.3, jitter=1.2, broken=0.15, seed=41)
L = layer(); ImageDraw.Draw(L).line(P(back), fill=(80, 108, 120, 150), width=s(2.5)); img.alpha_composite(L)

serra = slope_edge + [(3000, 1200), (3000, 3000)]
L = layer(); ImageDraw.Draw(L).polygon(P(serra), fill=FOREST_MID); img.alpha_composite(L)
sm = mask(); ImageDraw.Draw(sm).polygon(P(serra), fill=255)
hatch(sm, 7, -9, (40, 64, 64, 70), width=1.3, jitter=1.0, broken=0.15, seed=51)
# forest crowns: small dome marks with moonlit tops
L = layer(); d = ImageDraw.Draw(L); rnd = random.Random(61)
for _ in range(2600):
    x = rnd.uniform(1150, 3000); y = rnd.uniform(1300, 3000)
    if sm.getpixel((min(W - 1, s(x)), min(W - 1, s(y)))) == 0: continue
    r = rnd.uniform(9, 22) * (0.6 + (y - 1300) / 1700 * 0.8)
    d.ellipse([s(x - r), s(y - r * .8), s(x + r), s(y + r * .8)], fill=(14, 30, 30, 255))
    d.arc([s(x - r), s(y - r * .8), s(x + r), s(y + r * .8)], 200, 290, fill=(70, 100, 104, 150), width=s(1.6))
paste(img, L, sm)
# moonlit rim of the slope
L = layer(); ImageDraw.Draw(L).line(P(slope_edge), fill=(120, 146, 160, 170), width=s(3)); img.alpha_composite(L)

# ---------- the road: hairpins down the serra, beads at each turn ----------
def lerp_edge(edge, y):
    for (x0, y0), (x1, y1) in zip(edge, edge[1:]):
        lo, hi = sorted((y0, y1))
        if lo <= y <= hi and y1 != y0: return x0 + (x1 - x0) * (y - y0) / (y1 - y0)
    return edge[-1][0]
left_edge = sorted(slope_edge, key=lambda p: p[1])
right_edge = [(2000, 1560), (2080, 1800), (2180, 2200), (2250, 2600), (2350, 3000)]
pts = [(2030, 1640)]
y = 1640; side = 0
for i in range(7):
    y += 98 + i * 10
    Lx = lerp_edge(left_edge, y) + 45; Rx = lerp_edge(right_edge, y) - 40
    pts.append((Lx if side == 0 else Rx, y)); side ^= 1
pts.append((1330, 2640)); pts.append((PX + PRX + 70, PY + 34))
# smooth with Chaikin
def chaikin(p, it=4):
    for _ in range(it):
        q = [p[0]]
        for a, b in zip(p, p[1:]):
            q += [(a[0] * .75 + b[0] * .25, a[1] * .75 + b[1] * .25), (a[0] * .25 + b[0] * .75, a[1] * .25 + b[1] * .75)]
        q.append(p[-1]); p = q
    return p
rp = chaikin(pts)
L = layer(); d = ImageDraw.Draw(L)
d.line(P(rp), fill=(30, 26, 18, 255), width=s(15), joint='curve')
d.line(P(rp), fill=(120, 98, 62, 255), width=s(8), joint='curve')
d.line(P(rp), fill=(170, 146, 100, 140), width=s(2.5), joint='curve')
img.alpha_composite(L)
# beads at turns (the terço): pale stones with small glow
beads = [min(rp, key=lambda q: (q[0] - x) ** 2 + (q[1] - y) ** 2) for (x, y) in pts[1:-2]]
for (x, y) in beads:
    glow(x, y, 40, (230, 214, 170, 120), 0.8)
L = layer(); d = ImageDraw.Draw(L)
for (x, y) in beads:
    d.ellipse([s(x - 9), s(y - 9), s(x + 9), s(y + 9)], fill=(236, 226, 196, 255))
    d.ellipse([s(x - 9), s(y - 9), s(x + 9), s(y + 9)], outline=(90, 74, 50, 255), width=s(1.5))
img.alpha_composite(L)

# ---------- the crag ----------
crag = [(1960, 1420), (2080, 1352), (2200, 1318), CRAG_TOP, (2470, 1262), (2560, 1290),
        (2680, 1270), (2800, 1300), (3000, 1280), (3000, 3000), (2350, 3000), (2250, 2600),
        (2180, 2200), (2080, 1800), (2000, 1560)]
L = layer(); ImageDraw.Draw(L).polygon(P(crag), fill=ROCK); img.alpha_composite(L)
cm = mask(); ImageDraw.Draw(cm).polygon(P(crag), fill=255)
hatch(cm, 6, -30, (54, 70, 80, 110), width=1.3, jitter=1.0, broken=0.18, seed=71)
hatch(cm, 13, 60, (2, 4, 6, 120), width=1.6, jitter=1.0, broken=0.25, seed=72)
# rock planes: a few long fissures
L = layer(); d = ImageDraw.Draw(L)
for f in [[(2080, 1360), (2120, 1620), (2190, 1900), (2230, 2260)], [(2470, 1268), (2440, 1520), (2480, 1800), (2440, 2200)],
          [(2700, 1275), (2760, 1600), (2720, 1980)], [(2250, 1330), (2300, 1500), (2280, 1700)]]:
    d.line(P(chaikin(f, 3)), fill=(1, 2, 3, 255), width=s(4))
img.alpha_composite(L)
# moonlit rim on the crag top (light comes from the left)
L = layer(); ImageDraw.Draw(L).line(P(crag[:9]), fill=(150, 172, 186, 220), width=s(3.5)); img.alpha_composite(L)
L = layer(); ImageDraw.Draw(L).line(P(crag[:5] + [(2000, 1560)][:0]), fill=(150, 172, 186, 140), width=s(2)); img.alpha_composite(L)

# ---------- the figure (seen from behind, face never visible) ----------
FX, FY = 2390, 1272          # feet
H = 470                      # figure height ~ 1/6 of canvas
sil = (5, 8, 11, 255)
def fy(t): return FY - H * t
L = layer(); d = ImageDraw.Draw(L)
# subtle long shadow cast by the lantern, falling right, a little too long and curved
sh = chaikin([(FX + 20, FY - 2), (FX + 160, FY + 10), (FX + 320, FY + 34), (FX + 450, FY + 78), (FX + 520, FY + 120)], 3)
d.line(P(sh), fill=(0, 0, 0, 150), width=s(30), joint='curve')
img.alpha_composite(L.filter(ImageFilter.GaussianBlur(s(9))))
L = layer(); d = ImageDraw.Draw(L)
# body: one smoothed outline (seen from behind), right arm hanging
body = [(-52, 0.0), (-40, 0.22), (-44, 0.46), (-74, 0.555), (-60, 0.70), (-44, 0.785), (-17, 0.815),
        (17, 0.815), (46, 0.785), (62, 0.70), (76, 0.56), (68, 0.545), (72, 0.47), (68, 0.425),
        (56, 0.43), (52, 0.50), (44, 0.47), (40, 0.22), (50, 0.0), (17, 0.0), (5, 0.31), (-5, 0.31), (-19, 0.0)]
outline = chaikin([(FX + dx, fy(t)) for dx, t in body] + [(FX - 52, fy(0.0))], 2)
d.polygon(P(outline), fill=sil)
# cape: a slightly lighter cloth over the shoulders, with two folds
cape = chaikin([(FX - 44, fy(0.785)), (FX - 60, fy(0.70)), (FX - 74, fy(0.555)), (FX - 20, fy(0.535)),
                (FX + 24, fy(0.54)), (FX + 76, fy(0.56)), (FX + 62, fy(0.70)), (FX + 46, fy(0.785))], 2)
d.polygon(P(cape), fill=(11, 15, 19, 255))
for fx0 in (-30, 8, 40):
    d.line(P(chaikin([(FX + fx0, fy(0.77)), (FX + fx0 - 4, fy(0.66)), (FX + fx0 + 2, fy(0.55))], 2)), fill=(4, 6, 8, 255), width=s(2))
# feet
d.ellipse([s(FX - 60), s(fy(0) - 9), s(FX - 20), s(fy(0) + 5)], fill=sil)
d.ellipse([s(FX + 12), s(fy(0) - 9), s(FX + 54), s(fy(0) + 5)], fill=sil)
# head, hat crown and wide brim
d.ellipse([s(FX - 22), s(fy(0.925)), s(FX + 22), s(fy(0.80))], fill=sil)
d.ellipse([s(FX - 94), s(fy(0.915) - 13), s(FX + 94), s(fy(0.915) + 13)], fill=sil)
d.polygon(P(chaikin([(FX - 36, fy(0.915)), (FX - 31, fy(0.985)), (FX - 10, fy(1.005)), (FX + 12, fy(1.005)), (FX + 31, fy(0.985)), (FX + 36, fy(0.915))], 2)), fill=sil)
# left arm (viewer's left) raised forward with the lantern: tapered, bent at the elbow
ax, ay = FX - 168, fy(0.86)
arm = chaikin([(FX - 40, fy(0.785)), (FX - 96, fy(0.805)), (ax + 6, ay - 10), (ax, ay + 10), (FX - 98, fy(0.765)), (FX - 46, fy(0.735))], 1)
d.polygon(P(arm), fill=sil)
d.ellipse([s(ax - 12), s(ay - 11), s(ax + 12), s(ay + 11)], fill=sil)
img.alpha_composite(L)
# moonlit rim: hat brim and the left contour only (the moon is to the left)
L = layer(); d = ImageDraw.Draw(L)
d.arc([s(FX - 94), s(fy(0.915) - 13), s(FX + 94), s(fy(0.915) + 13)], 170, 230, fill=(150, 172, 186, 210), width=s(2.2))
d.line(P(chaikin([(FX - 36, fy(0.915)), (FX - 31, fy(0.985)), (FX - 12, fy(1.004))], 2)), fill=(150, 172, 186, 170), width=s(1.8))
d.line(P(chaikin([(FX - 60, fy(0.70)), (FX - 74, fy(0.555)), (FX - 44, fy(0.46)), (FX - 40, fy(0.22)), (FX - 52, fy(0.0))], 2)), fill=(130, 152, 168, 140), width=s(1.8))
img.alpha_composite(L)
# key in the right hand: iron with a gold glint
L = layer(); d = ImageDraw.Draw(L)
kx, ky = FX + 64, fy(0.425)
d.line([(s(kx), s(ky)), (s(kx + 2), s(ky + 36))], fill=(188, 146, 70, 255), width=s(2.6))
d.ellipse([s(kx - 6), s(ky - 10), s(kx + 6), s(ky + 1)], outline=(200, 156, 76, 255), width=s(2.4))
d.line([(s(kx + 2), s(ky + 31)), (s(kx + 11), s(ky + 31))], fill=(188, 146, 70, 255), width=s(2.4))
d.line([(s(kx + 2), s(ky + 25)), (s(kx + 9), s(ky + 25))], fill=(188, 146, 70, 255), width=s(2.4))
# terço around the wrist: tiny pale beads
for k in range(9):
    a = 2 * math.pi * k / 9
    bx, by = FX + 61 + 13 * math.cos(a), fy(0.475) + 5 * math.sin(a)
    d.ellipse([s(bx - 2.6), s(by - 2.6), s(bx + 2.6), s(by + 2.6)], fill=(214, 202, 172, 255))
d.line([(s(FX + 61), s(fy(0.47))), (s(FX + 58), s(fy(0.40)))], fill=(214, 202, 172, 200), width=s(1.4))
d.polygon(P([(FX + 55, fy(0.40)), (FX + 61, fy(0.40)), (FX + 58, fy(0.385))]), fill=(214, 202, 172, 230))
img.alpha_composite(L)
# lantern hanging from the raised hand
LX, LY = ax - 2, ay + 58
glow(LX, LY, 360, (255, 176, 70, 230), 1.0)
glow(LX, LY, 90, (255, 214, 140, 230), 1.0)
L = layer(); d = ImageDraw.Draw(L)
d.line([(s(ax), s(ay + 8)), (s(LX), s(LY - 34))], fill=(30, 24, 16, 255), width=s(2.5))
d.arc([s(LX - 16), s(LY - 50), s(LX + 16), s(LY - 26)], 180, 360, fill=(60, 46, 26, 255), width=s(3))
d.polygon(P([(LX - 22, LY - 28), (LX + 22, LY - 28), (LX + 18, LY - 36), (LX - 18, LY - 36)]), fill=(46, 36, 22, 255))
d.rectangle([s(LX - 19), s(LY - 28), s(LX + 19), s(LY + 22)], fill=(255, 196, 96, 235))
d.rectangle([s(LX - 19), s(LY - 28), s(LX + 19), s(LY + 22)], outline=(60, 44, 24, 255), width=s(3))
d.line([(s(LX), s(LY - 28)), (s(LX), s(LY + 22))], fill=(70, 50, 26, 220), width=s(2))
d.ellipse([s(LX - 6), s(LY - 8), s(LX + 6), s(LY + 12)], fill=(255, 250, 220, 255))
d.rectangle([s(LX - 24), s(LY + 22), s(LX + 24), s(LY + 30)], fill=(46, 36, 22, 255))
img.alpha_composite(L)
# warm light catching the underside of the hat brim and the raised arm
L = layer(); d = ImageDraw.Draw(L)
d.arc([s(FX - 92), s(fy(0.915) - 14), s(FX + 92), s(fy(0.915) + 14)], 120, 175, fill=(222, 150, 70, 210), width=s(3))
d.line(P(chaikin([(FX - 98, fy(0.765)), (ax, ay + 10)], 1)), fill=(222, 150, 70, 170), width=s(2.6))
img.alpha_composite(L)

# ---------- wood grain + varnish ----------
g = np.random.normal(0, 1, (W // 8, W // 64)).astype(np.float32)
grain = Image.fromarray(((g - g.min()) / (g.max() - g.min()) * 255).astype(np.uint8)).resize((W, W), Image.BICUBIC)
grain = grain.filter(ImageFilter.GaussianBlur(s(1.5)))
ga = np.asarray(grain).astype(np.float32) / 255.0
base = np.asarray(img.convert('RGB')).astype(np.float32)
base *= (0.84 + 0.20 * ga)[..., None]
fine = np.random.normal(0, 4.0, base.shape[:2]).astype(np.float32)[..., None]
base += fine
# varnish: warm the highlights a touch, cool the deepest shadows
lum = base.mean(axis=2, keepdims=True) / 255.0
base[..., 0:1] += 10 * lum ** 2; base[..., 1:2] += 5 * lum ** 2; base[..., 2:3] -= 6 * lum ** 2
img = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8)).convert('RGBA')

# ---------- vignette ----------
yy, xx = np.mgrid[0:W, 0:W].astype(np.float32) / W
v = 1 - 0.38 * (((xx - .5) ** 2 + (yy - .48) ** 2) * 2.2) ** 1.4
arr = np.asarray(img.convert('RGB')).astype(np.float32) * np.clip(v, 0.55, 1)[..., None]
img = Image.fromarray(arr.astype(np.uint8)).convert('RGBA')

# ---------- ex-voto frame: dark wood with a gilded fillet ----------
L = layer(); d = ImageDraw.Draw(L)
d.rectangle([0, 0, W - 1, W - 1], outline=(14, 10, 8, 255), width=s(M))
img.alpha_composite(L)
fm = mask(); fd = ImageDraw.Draw(fm); fd.rectangle([0, 0, W, W], fill=255); fd.rectangle([s(M), s(M), W - s(M), W - s(M)], fill=0)
hatch(fm, 5, 0, (40, 28, 18, 140), width=1.6, jitter=1.6, broken=0.2, seed=91)
L = layer(); d = ImageDraw.Draw(L)
for inset, w, c in [(M - 14, 4, (184, 140, 64, 255)), (M - 26, 1.6, (150, 112, 52, 200)), (34, 1.6, (120, 90, 44, 170))]:
    d.rectangle([s(inset), s(inset), W - s(inset), W - s(inset)], outline=c, width=s(w))
# small gilded corner beads
for cx_, cy_ in [(M - 14, M - 14), (3000 - M + 14, M - 14), (M - 14, 3000 - M + 14), (3000 - M + 14, 3000 - M + 14)]:
    d.ellipse([s(cx_ - 9), s(cy_ - 9), s(cx_ + 9), s(cy_ + 9)], fill=(200, 156, 72, 255))
img.alpha_composite(L)

# ---------- optional title ----------
if WITH_TEXT:
    L = layer(); d = ImageDraw.Draw(L)
    f1 = ImageFont.truetype(f"{FONTS}/ArsenalSC-Regular.ttf", s(62))
    f2 = ImageFont.truetype(f"{FONTS}/ArsenalSC-Regular.ttf", s(40))
    def spaced(text, font, tracking):
        widths = [d.textlength(ch, font=font) for ch in text]
        return sum(widths) + tracking * (len(text) - 1), widths
    def draw_spaced(text, font, tracking, cy, color):
        total, widths = spaced(text, font, tracking)
        x = (W - total) / 2
        for ch, w in zip(text, widths):
            d.text((x, cy), ch, font=font, fill=color, anchor='lm'); x += w + tracking
    draw_spaced("SOZINHO EM PROCISSÃO", f1, s(26), s(330), (230, 220, 192, 235))
    d.line([(W / 2 - s(46), s(400)), (W / 2 + s(46), s(400))], fill=(196, 152, 72, 220), width=s(2))
    draw_spaced("CAÔ", f2, s(30), s(460), (210, 196, 160, 220))
    img.alpha_composite(L)

img = img.convert('RGB').resize((3000, 3000), Image.LANCZOS)
img.save(OUT, quality=95)
print("ok", OUT)
