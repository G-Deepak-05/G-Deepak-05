"""
Prep a straight-out-of-camera photo for ASCII conversion:
 1. Cut the subject out of the background with a matting model (u2net via
    rembg). GrabCut was tried first and could not separate this shot -- the
    rooftop water tanks and trees sit at the same luminance as the hair and
    got merged into the subject, which is what turned the portrait into a
    dark blob. A learned matte handles it cleanly.
 2. Crop: FRAME="full" keeps the whole subject (person + guitar, i.e. the
    original photo's composition); FRAME="head" crops to head-and-shoulders.
    The head is located from the matte itself -- the top of the alpha is the
    top of the hair -- so no coordinates are hardcoded to one photo.
 3. CLAHE on luminance only, kept gentle: pushing it harder equalizes noise
    in the flat shirt/hair regions into speckle that reads as static once
    it lands on the character ramp.
 4. Composite onto white so the background sits at the empty end of the ramp.

Run locally when the source photo changes; the daily workflow does not run this.
"""
import os

import cv2
import numpy as np

SRC = "assets/source.jpg"
OUT = "assets/photo-ready.png"

FRAME = os.environ.get("FRAME", "full")   # "full" | "head"
CLAHE_CLIP = 3.0
HEAD_W_MULT = 1.95      # crop width as a multiple of head width, FRAME="head"
HEAD_H_MULT = 1.16
HEAD_UP = 0.16          # headroom above the hair, as a fraction of head width


def cutout_alpha(bgr):
    """Subject alpha, 0-255. Learned matte, with GrabCut as a degraded fallback."""
    try:
        from rembg import new_session, remove
    except ImportError:
        print("rembg not installed -- falling back to GrabCut (expect background bleed)")
        return grabcut_alpha(bgr)
    from PIL import Image
    rgb = Image.fromarray(cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB))
    out = remove(rgb, session=new_session("u2net"))
    return np.array(out)[..., 3]


def grabcut_alpha(bgr):
    h, w = bgr.shape[:2]
    rect = (int(w * 0.03), int(h * 0.22), int(w * 0.94), int(h * 0.76))
    mask = np.zeros((h, w), np.uint8)
    bgd = np.zeros((1, 65), np.float64)
    fgd = np.zeros((1, 65), np.float64)
    cv2.grabCut(bgr, mask, rect, bgd, fgd, 8, cv2.GC_INIT_WITH_RECT)
    fg = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 255, 0).astype("uint8")
    return cv2.morphologyEx(fg, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))


def head_box(alpha):
    """Top of the matte is the top of the hair; the head's span is measured just below it."""
    h, w = alpha.shape
    rows = (alpha > 20).sum(axis=1)
    hits = np.where(rows > w * 0.004)[0]
    if len(hits) == 0:
        raise SystemExit("empty matte -- is assets/source.jpg the right photo?")
    top = int(hits[0])
    band = alpha[top:top + int(h * 0.11)]
    xs = np.where(band.max(axis=0) > 20)[0]
    x0, x1 = int(xs.min()), int(xs.max())
    hw = x1 - x0
    cx = (x0 + x1) / 2.0
    cw = hw * HEAD_W_MULT
    ch = cw * HEAD_H_MULT
    left = max(0, int(round(cx - cw / 2)))
    topc = max(0, int(round(top - hw * HEAD_UP)))
    return left, topc, min(w, int(round(left + cw))), min(h, int(round(topc + ch)))


def subject_box(alpha):
    ys, xs = np.where(alpha > 20)
    return int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())


def main():
    img = cv2.imread(SRC)
    if img is None:
        raise SystemExit(f"could not read {SRC}")
    alpha = cutout_alpha(img)

    box = head_box(alpha) if FRAME == "head" else subject_box(alpha)
    x0, y0, x1, y1 = box
    img_c, mask_c = img[y0:y1, x0:x1], alpha[y0:y1, x0:x1]

    lab = cv2.cvtColor(img_c, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    l2 = cv2.createCLAHE(clipLimit=CLAHE_CLIP, tileGridSize=(8, 8)).apply(l)
    img_eq = cv2.cvtColor(cv2.merge((l2, a, b)), cv2.COLOR_LAB2BGR)

    al = (cv2.GaussianBlur(mask_c, (5, 5), 0).astype(np.float32) / 255.0)[..., None]
    white = np.full_like(img_eq, 255)
    composited = (img_eq.astype(np.float32) * al + white.astype(np.float32) * (1 - al)).astype(np.uint8)

    cv2.imwrite(OUT, composited)
    print(f"wrote {OUT} {composited.shape[1]}x{composited.shape[0]} (FRAME={FRAME}, box={box})")


if __name__ == "__main__":
    main()
