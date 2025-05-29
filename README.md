# GamerZone

## Descripció

GamerZone sembla ser una aplicació web construïda amb el framework Django, probablement funcionant com un blog o plataforma de contingut centrada en el món dels videojocs. Segons l'estructura dels fitxers, inclou funcionalitats per gestionar i mostrar publicacions, autors i etiquetes.

## Estructura del Projecte

El projecte està estructurat segons el format estàndard de Django dins del directori `my_site/`:

-   **`my_site/`**: Directori arrel que conté els fitxers principals del projecte.
    -   **`manage.py`**: Eina de línia de comandes de Django per gestionar el projecte.
    -   **`my_site/`**: Directori principal de configuració del projecte que conté `settings.py`, `urls.py`, etc.
    -   **`blog/`**: Aplicació de Django que probablement gestiona el contingut principal (publicacions, autors, etiquetes). Conté models, vistes, plantilles, migracions, fitxers estàtics i proves.
    -   **`db.sqlite3`**: Fitxer de base de dades SQLite predeterminat utilitzat durant el desenvolupament.
    -   **`static/`**: Directori per als fitxers estàtics recollits.
    -   **`run.bat`**: Script de Windows per executar el servidor de desenvolupament.

## Funcionalitats Principals (Inferides)

*   Mostrar publicacions del blog amb els seus detalls.
*   Veure informació dels autors.
*   Navegar pel contingut mitjançant etiquetes.
*   Servei bàsic de fitxers estàtics (CSS, imatges).
*   Esquema de base de dades gestionat amb migracions de Django.
*   Script per omplir dades inicials del blog (`poblate_blog.py`).

## Com Començar

Per executar aquest projecte localment, segueix aquests passos generals:

1.  **Clona el repositori:**
    ```bash
    git clone <repository_url>
    cd my_site
    ```
    Substitueix `<repository_url>` per l’URL real del repositori.

2.  **Crea un entorn virtual de Python (Recomanat):**
    ```bash
    python -m venv venv
    # A Windows:
    .\venv\Scripts\activate
    # A macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instal·la les dependències:**
    Aquest projecte utilitza Django. No hi ha un fitxer `requirements.txt` a la llista proporcionada, així que potser hauràs d’instal·lar Django manualment o crear un fitxer `requirements.txt` segons les necessitats del projecte.
    ```bash
    # Si tens requirements.txt
    pip install -r requirements.txt
    # O instal·la Django manualment (la versió pot variar)
    pip install Django
    ```
    *Nota: No s’ha especificat la versió concreta de Django. Pot ser necessari revisar el codi del projecte o inferir-la del bytecode de Python.*

4.  **Aplica les migracions de la base de dades:**
    ```bash
    python manage.py migrate
    ```

5.  **Crea un superusuari (Opcional, però necessari per l’Admin de Django):**
    ```bash
    python manage.py createsuperuser
    ```
    Segueix les instruccions per crear un compte d’administrador.

6.  **Omple dades inicials (Opcional):**
    Hi ha un script anomenat `poblate_blog.py`. El seu ús no és l’estàndard de Django. Pot ser un script independent o pensat per executar-se com una comanda personalitzada. Revisa el seu contingut per veure com s’ha d’executar.

7.  **Executa el servidor de desenvolupament:**
    ```bash
    python manage.py runserver
    ```
    Alternativament, a Windows pots utilitzar l’script `run.bat`.

## Ús

Un cop el servidor estigui en funcionament, obre el navegador i ves a `http://127.0.0.1:8000/` (o l’adreça que es mostri al terminal) per accedir a l’aplicació.

## Tecnologies Utilitzades

*   Python  
*   Django  
*   SQLite (Base de dades per defecte)  
*   HTML  
*   CSS

## Contribució

Les contribucions són benvingudes! No dubtis a obrir incidències o enviar *pull requests*.

## Llicència

Aquest projecte està llicenciat sota la Llicència MIT.
