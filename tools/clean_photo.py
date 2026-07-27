"""
Prep a straight-out-of-camera photo for ASCII conversion:
 1. Segment the subject out from the background with GrabCut (classical CV,
    no model download needed -- keeps this sandbox-network-friendly).
 2. Crop to the subject with a little padding.
 3. CLAHE (adaptive histogram equalization) to pull real shadow/highlight
    detail out of what would otherwise print as flat mid-gray.
 4. Composite onto a plain white canvas so the background lands at the
    light/empty end of the character ramp instead of a dark blob.
"""
import sys
import cv2
import numpy as np

SRC = "assets/source.jpg"
OUT = "assets/photo-ready.png"


def main():
    img = cv2.imread(SRC)
    h, w = img.shape[:2]

    # Rough rect around the subject -- generous margins on all sides, GrabCut
    # refines the rest. Photo is subject-in-lower-2/3, so trim empty sky more
    # aggressively from the top.
    rect = (int(w * 0.03), int(h * 0.22), int(w * 0.94), int(h * 0.76))

    mask = np.zeros((h, w), np.uint8)
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)
    cv2.grabCut(img, mask, rect, bgd_model, fgd_model, 8, cv2.GC_INIT_WITH_RECT)
    fg_mask = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 255, 0).astype("uint8")

    # clean up mask a touch
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))
    fg_mask = cv2.GaussianBlur(fg_mask, (5, 5), 0)

    ys, xs = np.where(fg_mask > 20)
    if len(xs) == 0:
        print("GrabCut found nothing -- falling back to full frame")
        x0, y0, x1, y1 = 0, 0, w, h
    else:
        pad_x, pad_y = int(w * 0.03), int(h * 0.03)
        x0, x1 = max(xs.min() - pad_x, 0), min(xs.max() + pad_x, w)
        y0, y1 = max(ys.min() - pad_y, 0), min(ys.max() + pad_y, h)

    img_c = img[y0:y1, x0:x1]
    mask_c = fg_mask[y0:y1, x0:x1]

    # CLAHE on luminance channel only, so colors don't shift weirdly
    lab = cv2.cvtColor(img_c, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    l2 = clahe.apply(l)
    lab2 = cv2.merge((l2, a, b))
    img_eq = cv2.cvtColor(lab2, cv2.COLOR_LAB2BGR)

    # composite onto white using the (feathered) foreground mask as alpha
    alpha = (mask_c.astype(np.float32) / 255.0)[..., None]
    white = np.full_like(img_eq, 255)
    composited = (img_eq.astype(np.float32) * alpha + white.astype(np.float32) * (1 - alpha)).astype(np.uint8)

    cv2.imwrite(OUT, composited)
    print(f"wrote {OUT} {composited.shape[1]}x{composited.shape[0]}")


if __name__ == "__main__":
    main()
