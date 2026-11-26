from pathlib import Path
from urllib.request import Request, urlopen
from concurrent.futures import ThreadPoolExecutor

BASE = Path(__file__).resolve().parent
IMAGENES = {'assets/frambuesa.jpg': 'https://commons.wikimedia.org/wiki/Special:FilePath/Raspberries%20(Rubus%20idaeus).jpg', 'assets/zarzamora.jpg': 'https://commons.wikimedia.org/wiki/Special:FilePath/Blackberry%20fruit.jpg', 'assets/ayrampo.jpg': 'https://imgmedia.buenazo.pe/1200x660/buenazo/original/2026/06/04/6a21b6a72766a31b1f034f7b.jpg', 'assets/sanky.jpg': 'https://3.bp.blogspot.com/-_4_BF1mfguc/VS43AbsPHTI/AAAAAAAAAEs/wXr9i7UF7G4/s1600/SANKY.jpg', 'assets/aguaymanto.jpg': 'https://commons.wikimedia.org/wiki/Special:FilePath/Physalis%20peruviana%20fruits%20close-up.jpg', 'assets/cereza.jpg': 'https://commons.wikimedia.org/wiki/Special:FilePath/Cherry%20cherries%20fruit.jpg', 'assets/mango.jpg': 'https://commons.wikimedia.org/wiki/Special:FilePath/Mango%20fruit.jpg', 'assets/cosecha.jpg': 'https://agraria.pe/imgs/a/lx/sumate-la-reconocida-iniciativa-de-hortifrut-peru-que-incluy-32490.jpg', 'assets/campo.jpg': 'https://www.findevcanada.ca/sites/default/files/styles/max_1300x1300/public/2024-04/Danper%20ALV.png.webp?itok=j9HLlVeF', 'assets/frutos-rojos.jpg': 'https://extension.psu.edu/programs/master-gardener/counties/tioga/news/what-is-the-difference-between-a-raspberry-and-a-blackberry/@@images/image', 'assets/zarzamora-planta.jpg': 'https://commons.wikimedia.org/wiki/Special:FilePath/Blackberry%20Patch%20on%20Private%20Property%20in%20Woodstock%20IL%20Produces%20a%20Delicious%20Crop%20-%20panoramio.jpg', 'assets/lavado.jpg': 'https://www.solutionbuggy.com/_next/image?q=75&url=%2Fassets%2FFoodPagesImages%2FGEO%2Fservices%2Ffruit_vegetable_processing_v2.png&w=3840', 'assets/maquinaria.jpg': 'https://www.aquatreat.in/assets/images/food-processing-equipment.jpg', 'assets/procesamiento.jpg': 'https://arkhstroyproekt.ru/assets/img/projects/yagodokhranilische/fragariya_18.JPG', 'assets/llenado.jpg': 'https://hirotaka-jam.shop/cdn/shop/files/DSC_0216_d2720629-5f10-4e95-9fac-b425730517d2.jpg?v=1708050243&width=3840', 'assets/envasado.jpg': 'https://image.made-in-china.com/203f0j00kfpeyACmyGqM/Fresh-Fruit-Cocktail-Processing-Equipment-Canned-Pineapple-Packaging-Machinery.webp', 'assets/carga-aerea.jpg': 'https://www.ibcinc.com/hubfs/ibc-ty-4-max-min.jpg', 'assets/avion.jpg': 'https://commons.wikimedia.org/wiki/Special:FilePath/Airplane-in-flight.jpg', 'assets/berlin-puerta.jpg': 'https://commons.wikimedia.org/wiki/Special:FilePath/Brandenburg%20Gate%20at%20night.jpg', 'assets/sanky-planta.jpg': 'https://commons.wikimedia.org/wiki/Special:FilePath/Corryocactus%20brevistylus.jpg', 'assets/reutilizacion.jpg': 'https://www.bigw.com.au/medias/sys_master/images/images/ha1/h7f/115418645692446.jpg', 'assets/reciclaje.jpg': 'https://www.verpackungsregister.org/fileadmin/files/Echtbilder/8653-Glas_PK.jpg'}

def descargar(item):
    ruta, url = item
    destino = BASE / ruta
    destino.parent.mkdir(parents=True, exist_ok=True)
    if destino.exists() and destino.stat().st_size > 0:
        return ruta + ' : existente'
    try:
        req = Request(url, headers={'User-Agent': 'MiskiKusiWebsite/1.0 (educational project; image retrieval)'})
        with urlopen(req, timeout=35) as respuesta:
            if not respuesta.headers.get_content_type().startswith('image/'):
                raise ValueError('La respuesta no es una imagen')
            datos = respuesta.read()
        destino.write_bytes(datos)
        return ruta + ' : descargada'
    except Exception as e:
        return ruta + ' : ERROR - ' + str(e)

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3) as pool:
        for resultado in pool.map(descargar, IMAGENES.items()):
            print(resultado)
