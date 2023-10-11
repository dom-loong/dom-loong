from PIL import Image
from pathlib import Path

import shutil
import os

gallery_path = Path(".") / "gallery"

for im_path in gallery_path.glob("**/*"):
    im = Image.open(im_path)
    dest_path = Path(".") / f"output/{im_path.name}"
    quality = 100

    print(f"Now compressing {im_path.name}")

    if os.path.getsize(im_path) > 16000000:
        im.save(dest_path, optimize=True, quality=quality)
        while os.path.getsize(dest_path) > 16000000:
            quality -= 1
            im.save(dest_path, optimize=True, quality=quality)

        print(f"Compressed with quality {quality}")
    else:
        print(f"{im_path.name} does not need compressing")
        shutil.copyfile(im_path, dest_path)

    print(f"Saved {im_path.name} at size: {os.path.getsize(dest_path)}")
