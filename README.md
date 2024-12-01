# Ayah Recognizer

Librería Python para reconocimiento de versículos del Sagrado Qur'an en textos que usen cualquier idioma, alfabeto o transliteración.

## Prerequisitos

- Instalación de dependencias:
```bash
python -m pip install -r requirements.txt
```

- En el fichero `./assistant_config/API.txt` pega tu API key de OpenAI.

## Uso

En tu script de python añade el import:
```python
import AyahRecognizer
```

Y pásale el texto como parámetro a la función `recognize_ayaat`:
```python
response = AyahRecognizer.recognize_ayaat("Bua hermano el otro dia iba caminando y escuche: allahu la ilaha illah huwa al hayul qayum, sabes que versiculo es?? tambien ya ayuha al kafirun la abudu ma ta budun. Me gustaron mucho.")
if (response != None):
for match in response:
    print(match)
```

### Output

    2:255 | allahu la ilaha illah huwa al hayul qayum  
    109:1-2 | ya ayuha al kafirun la abudu ma ta budun
