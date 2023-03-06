## django-harjoitus
Ensimmäinen Django-harjoitus

# Asennus
1. Tee Python-virtuaaliympäristö
   ```sh
   python3 -m venv venv
   ```
2. Aktivoi virtuaaliympäristö
   - Voit tehdä tämän VSCodessa vastaamalla Yes, kun VSCode kysyy voidaanko virtuaaliympäristö aktivoida. Jos tätä kysymystä ei tule, klikkaa versionumeroa Python-sanan vierestä alapalkista. Python-sana tulee alapalkkiin, kun avaat jonkin py.-tiedoston (esim. manage.py)
   - Vaihtoehtoisesti voit ajaa Linuxissa 'venv/bin/activate' tai Windowsissa 'venv\script\activate.ps1
   - Kun virtuaaliympäristö on aktiivinen, terminaalissa lukee rivin alussa (venv)
3. Asenna tarvittavat Python-paketit
   ```sh
   pip install -r requirements.txt
4. Aja migraatiot:
   ```sh
   python manage.py migrate
   ```
   - Tämä luo SQLite tietokannan db.sqlite3-tiedostoon

5. Luo pääkäyttäjä:
   ```sh
   python manage.py createsuperuser
   ```
   - Käytä käyttäjätunnusta ja salasanaa, jotka muistat helposti
     Esim. "admin" ja "admin"

## Kehitysympäristön käynnistäminen

Aja Djangon runserver-komento:
```sh
python manage.py runserver
```

## Uusien migraatiotiedostojen tekeminen

Kun teet muutoksia models.py-tiedostoon, pitää model-muutokset saada myös tietokantaan. Tähän käytetään migraatiotiedostoja. Tehtyjen muutosten pohjalta voi luoda uuden migraatiotiedoston komennolla:
```sh
python manage.py makemigrations
```