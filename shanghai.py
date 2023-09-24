from PIL import Image
from pathlib import Path
from pillow_heif import register_heif_opener

register_heif_opener()



gallery_path = Path(".") / "drive"


for i, im_path in enumerate(gallery_path.glob("**/*")):
    im = Image.open(im_path)

    dest = Path(".") / f"output2/img_{i+1}.jpg"

    im.save(dest)

