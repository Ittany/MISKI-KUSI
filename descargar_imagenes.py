from pathlib import Path
from urllib.request import Request, urlopen
import time

ASSETS = Path(__file__).resolve().parent / "assets"
ASSETS.mkdir(exist_ok=True)
IMAGES = {'frambuesa': 'https://commons.wikimedia.org/wiki/Special:FilePath/Raspberries%20(Rubus%20idaeus).jpg', 'zarzamora': 'https://commons.wikimedia.org/wiki/Special:FilePath/Blackberry%20fruit.jpg', 'ayrampo': 'https://imgmedia.buenazo.pe/1200x660/buenazo/original/2026/06/04/6a21b6a72766a31b1f034f7b.jpg', 'sanky': 'https://3.bp.blogspot.com/-_4_BF1mfguc/VS43AbsPHTI/AAAAAAAAAEs/wXr9i7UF7G4/s1600/SANKY.jpg', 'preparacion': 'https://images.unsplash.com/photo-1600271886742-f049cd451bba?w=900&q=80', 'aguaymanto': 'https://commons.wikimedia.org/wiki/Special:FilePath/Physalis%20peruviana%20fruits%20close-up.jpg', 'mango': 'https://commons.wikimedia.org/wiki/Special:FilePath/Mango%20fruit.jpg', 'peru': 'https://images.unsplash.com/photo-1526392060635-9d6019884377?w=600&q=80', 'puerto': 'https://images.unsplash.com/photo-1494412574643-ff11b0a5c1c3?w=600&q=80', 'hamburgo': 'https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=600&q=80', 'berlin': 'https://images.unsplash.com/photo-1560969184-10fe8719e047?w=600&q=80', 'consumidor': 'https://images.unsplash.com/photo-1542838132-92c53300491e?w=600&q=80', 'sostenibilidad': 'https://images.unsplash.com/photo-1466692476868-aef1dfb1e735?w=900&q=80'}

for name, url in IMAGES.items():
    target = ASSETS / (name + ".jpg")
    if target.exists() and target.stat().st_size > 0:
        print("Ya existe:", target.name)
        continue
    try:
        req = Request(url, headers={"User-Agent": "MiskiKusiSite/1.0 (image asset retrieval)", "Accept": "image/jpeg,image/*"})
        with urlopen(req, timeout=25) as response:
            data = response.read()
        if not data.startswith(b"\xff\xd8\xff"):
            raise ValueError("La respuesta no es un JPEG; guarda una foto JPG manualmente")
        target.write_bytes(data)
        print("OK:", target.name)
    except Exception as exc:
        print("FALTA:", target.name, "-", exc)
    time.sleep(1)

missing = [name + ".jpg" for name in IMAGES if not (ASSETS / (name + ".jpg")).exists()]
missing += [name for name in ("logo.jpeg", "producto.jpeg") if not (ASSETS / name).exists()]
if missing:
    print("Archivos pendientes:", ", ".join(missing))
    print("Agrega fotografias propias o con licencia adecuada antes del deploy.")
    raise SystemExit(1)
print("Archivos presentes. Revisa las licencias y ejecuta git add assets index.html.")
