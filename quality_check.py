"""Rule-based inspection of ASCII PGM grayscale images."""
import argparse
from pathlib import Path

def load_pgm(path):
    tokens = []
    for line in Path(path).read_text().splitlines():
        tokens.extend(line.split("#", 1)[0].split())
    if len(tokens) < 4 or tokens[0] != "P2":
        raise ValueError("Expected ASCII PGM (P2)")
    w, h, maxval = map(int, tokens[1:4])
    pixels = list(map(int, tokens[4:]))
    if w <= 0 or h <= 0 or maxval <= 0 or len(pixels) != w*h or any(p < 0 or p > maxval for p in pixels):
        raise ValueError("Invalid PGM pixels")
    return w, h, maxval, pixels

def assess(path):
    _, _, maxval, px = load_pgm(path)
    mean = sum(px)/len(px)/maxval
    contrast = (max(px)-min(px))/maxval
    flags = []
    if mean < 0.2:
        flags.append("underexposed")
    if mean > 0.8:
        flags.append("overexposed")
    if contrast < 0.15:
        flags.append("low contrast")
    return {"mean_brightness":round(mean,3), "contrast_range":round(contrast,3), "flags":flags}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image")
    args = parser.parse_args()
    print(assess(args.image))
