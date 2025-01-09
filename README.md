# Ayah Recognizer

Módulo de Python para reconocimiento de versículos del Sagrado Qur'an en textos que usen cualquier idioma, alfabeto o transliteración.

## Prerequisitos

> **IMPORTANTE:** El contenido del módulo está pensado para estar dentro de un directorio llamado `AyahRecognizer` y que el script donde llamemos en a este contenido esté en el directorio padre.

> Si en tu caso no quieres que sea así:
> - Haz los cambios pertinentes en las rutas que muestro a continuación.
> - Modifica también la variable `CONF_DIR` del fichero `AyaRecognizerUtils.py` e introduce ahí la ruta.

- Instalación de dependencias:
```bash
python -m pip install -r ./AyaRecognizer/requirements.txt
```

- En el fichero `./AyaRecognizer/assistant_config/API.txt` pega tu API key de OpenAI.

## Uso

En tu script de python añade el import:
```python
from AyahRecognizer.AyahRecognizer import AyahRecognizer
```

E inicializa el objeto:
```python
ayah_recognizer = AyahRecognizer()
```

Y pásale el texto como parámetro a la función `recognize_ayaat`:

---
### Ejemplo texto en árabe

```python
response = ayah_recognizer.recognize_ayaat("انا احبك كثيرا الايه الله قال تبارك الذي بيده الملك وهو على كل شيء قدير ودني الايه الله قال الذين كفروا وصدوا عن سبيل الله اضل اعمالهم وثاني والضحى والليل اذا سجى انا احبهن كثيرا")
if (response != None):
    print(response)
```
    
### Output

    67:1 | تبارك الذي بيده الملك وهو على كل شيء قدير
    47:1 | الذين كفروا وصدوا عن سبيل الله اضل اعمالهم
    93:1-2 | والضحى والليل اذا سجى
---
### Ejemplo texto transliterado

```python
response = ayah_recognizer.recognize_ayaat("Hermano, el otro dia iba caminando y escuche: allahu la ilaha illah huwa al hayul qayum, sabes que versiculo es?? tambien ya ayuha al kafirun la abudu ma ta budun. Me gustaron mucho.")
if (response != None):
    print(response)
```

### Output

    2:255 | allahu la ilaha illah huwa al hayul qayum  
    109:1-2 | ya ayuha al kafirun la abudu ma ta budun
---
### Ejemplo texto en español

```python
response = ayah_recognizer.recognize_ayaat("Dice que luego vuelve la vista por segunda vez y tu mirada volverá a ti cansada y derrotada. Este versiculo me gusta mucho")
if (response != None):
    print(response)
```

### Output

    67:4 | vuelve la vista por segunda vez y tu mirada volverá a ti cansada y derrotada.