# Python moodul koordinaatide teisendamiseks WGS84 ja L-Est97 vahel

See moodul võimaldab teisendada geograafilisi koordinaate WGS84 ja L-Est97 vahel.

## Funktsionaalsus

- Teisendus WGS84 → L-Est97
- Teisendus L-Est97 → WGS84

## Paigaldamine

Mooduli saad installida otse TestPyPi keskkonnast järgmise käsuga:

```bash
pip install --index-url https://test.pypi.org/simple/ transformations-illimarr
```

## Näide kasutamisest

```python
from transformations_illimarr import wgs84_to_lest97, lest97_to_wgs84

# WGS84 -> L-Est97
x, y = wgs84_to_lest97(59.395312, 24.664182)
print(f"X={x}, Y={y}")  # X=6584338.65, Y=537735.47

# L-Est97 -> WGS84
lat, lon = lest97_to_wgs84(6584338.65, 537735.47)
print(f"Lat={lat}, Lon={lon}")  # Lat=59.395312, Lon=24.664182
```

## Viited

- [TestPyPi projektileht](https://test.pypi.org/project/transformations-illimarr/)
- [Github](https://github.com/IllimarR/transformations)
- [Moodulis kasutatud pyproj teek](https://pypi.org/project/pyproj/)
- [L-Est97 EPSG:3301](http://spatialreference.org/ref/epsg/3301/)
- [WGS84 EPSG:4326](http://spatialreference.org/ref/epsg/4326/)

### Lisainfo

Moodul valmis Taltech õppeaines ICS0019 Python edasijõudnutele, 2025. a kevadel, 3. kodutöö
