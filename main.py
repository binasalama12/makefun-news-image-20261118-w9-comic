"""make.fun news-image-20261118 entry, wallet 9: comic panels.

The bundled picture tells Wednesday 18 November 2026 as six comic
panels with speech-bubble headlines: BOOM in the Gulf, CRACK at the
Kerch Bridge, summit meetings in Shenzhen and Manila, a health
alert pairing Ebola in Congo with the US measles reversal, a Cat-5
cyclone, and falling markets beside the Siberia crash. The program
streams the panel page to /output/entry.png in fixed-size chunks.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
CHUNK = 32768


def stream_copy(src, dst):
    total = 0
    with open(src, "rb") as fin, open(dst, "wb") as fout:
        while True:
            block = fin.read(CHUNK)
            if not block:
                break
            fout.write(block)
            total += len(block)
    return total


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    panel_count = 6
    total = stream_copy(SOURCE, os.path.join(out_dir, "entry.png"))
    print("comic page panels:", panel_count)
    if total != os.path.getsize(SOURCE):
        raise IOError("comic page copy incomplete")
    print("w9 comic panels published:", total, "bytes")


PANELS_W9 = [
    ("BOOM! GULF", "Qeshm strike; drones over Bahrain and Kuwait"),
    ("CRACK! CRIMEA", "Kerch Bridge span drops into the sea"),
    ("SUMMITS!", "Shenzhen APEC plus the Manila Quad meeting"),
    ("ALERT! HEALTH", "Ebola doubles; US measles status lost"),
    ("STORM!", "Cyclone Xavier Cat5 and a PNG quake at 6.0"),
    ("MARKETS DOWN!", "Stocks slide; Siberia crash kills 19"),
]


def panel_script():
    script = []
    for title, caption in PANELS_W9:
        script.append(title + " -- " + caption)
    return script


def panel_stats(path):
    size = os.path.getsize(path)
    return {"panels": len(PANELS_W9), "bytes": size, "chunk": CHUNK}


if __name__ == "__main__":
    for line in panel_script():
        print(line)
    print(panel_stats(SOURCE))
    main()
