from PIL import Image
from pathlib import Path

import os

gallery_path = Path(".") / "gallery"

for i, im_path in enumerate(gallery_path.glob("**/*")):
    im = Image.open(im_path)

    dest_path = Path(".") / f"output/img_{i+1}.jpg"

    if os.path.getsize(im_path) > 16000000:
        im.save(dest_path, optimize=True)
    else:
        im.save(dest_path)

    if os.path.getsize(dest_path) > 16000000:
        print(dest_path + " still over 16 MB!")
