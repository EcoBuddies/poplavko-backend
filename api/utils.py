import json
import xml.etree.ElementTree as ET
from regions import regions, water_levels


def parseXML(unparsed_xml_data):
    root = ET.fromstring(unparsed_xml_data)

    postaje = []
    meritve = []

    for postaja in root.findall('.//postaja'):
        sifra = int(postaja.get('sifra'))
        ime_kratko = postaja.find('ime_kratko').text if postaja.find('ime_kratko') is not None else None
        long = postaja.get('ge_dolzina')
        lat = postaja.get('ge_sirina')
        datum = postaja.find('datum').text if postaja.find('datum') is not None else None
        pretok = postaja.find('pretok').text if postaja.find('pretok') is not None else None
        pretok_znacilni = postaja.find('pretok_znacilni').text if postaja.find('pretok_znacilni') is not None else None
        vodostaj = postaja.find('vodostaj').text if postaja.find('vodostaj') is not None else None
        vodostaj_znacilni = postaja.find('vodostaj_znacilni').text if postaja.find('vodostaj_znacilni') is not None else None
        visina_valov = postaja.find('znacilna_visina_valov').text if postaja.find('znacilna_visina_valov') is not None else float(0)
        visina_valov_znacilni = 'visoki valovi' if visina_valov is not None and float(visina_valov) > 2.2 else None

        postaja_data = {
            'sifra': sifra,
            'ime_kratko': ime_kratko,
            'regija': water_levels[ime_kratko],
            'long': long,
            'lat': lat,
            'zadnja_sprememba': datum,
            'pretok': pretok,
            'pretok_znacilni': pretok_znacilni,
            'vodostaj': vodostaj,
            'vodostaj_znacilni': vodostaj_znacilni,
            'visina_valov': visina_valov,
            'visina_valov_znacilni': visina_valov_znacilni,
        }
        postaje.append(postaja_data)

        meritev_data = {
            'sifra': sifra,
            'regija': water_levels[ime_kratko],
            'datum': datum,
            'pretok_znacilni': pretok_znacilni,
            'pretok': pretok,
            'vodostaj': vodostaj,
            'vodostaj_znacilni': vodostaj_znacilni,
            'visina_valov': visina_valov,
            'visina_valov_znacilni': visina_valov_znacilni,
        }
        meritve.append(meritev_data)

    return [postaje, meritve]
