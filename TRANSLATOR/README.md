**Proyecto FastAPI para detectar idioma**

Este proyecto utiliza la biblioteca FastAPI para crear una API REST que 
puede detectar el idioma de un texto recibido a través de una solicitud 
HTTP.

**Funcionamiento**

La API tiene una ruta `/detectar` donde se puede enviar un texto en forma 
de JSON para que la API lo analice y devuelva el resultado. La función 
`detectar_idioma` utiliza técnicas de procesamiento de lenguaje natural 
para contar las palabras en español e inglés dentro del texto y calcular 
los porcentajes correspondientes.

**Funcionalidad**

La API tiene las siguientes características:

*   **Detección de idioma**: El proyecto puede detectar si un texto está 
escrito en español o inglés.
*   **Análisis de porcentaje**: La API calcula el porcentaje de palabras 
que están en cada idioma.

**Funciones**

La API tiene la siguiente función principal:

*   `detectar_idioma(texto)`: Esta función toma un texto como entrada, lo 
convierte a minúsculas y analiza las palabras para determinar los 
porcentajes de español e inglés. Si no se encuentran palabras en ninguna 
lista, devuelve un mensaje de error.

**Rutas**

La API tiene una ruta:

*   `/detectar`: Esta ruta acepta solicitudes HTTP POST que contienen un 
texto a detectar.

**Dependencias**

El proyecto depende de las siguientes bibliotecas:

*   `fastapi`
*   `uvicorn` (para ejecutar la API)
*   `re` (para procesamiento de reglas y expresiones regulares)
*   `idiomas.py` es el archivo que contiene las keys a buscar para detectar un idioma

**Instalación e Inicio**

Para instalar el proyecto, es necesario ejecutar los siguientes comandos 
en una terminal o consola:

```bash
pip install fastapi uvicorn
```

Una vez instalado, se puede iniciar la API con el comando `uvicorn`. El 
servidor de desarrollo se ejecuta en el host 0.0.0.0 y el puerto 8000.

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

**Uso**

Para usar la API, es necesario enviar una solicitud HTTP POST a la ruta 
`/detectar` con el texto que se desea detectar en formato JSON.

```json
{
    "texto": "Este es un texto en español para ser analizado"
}
```

La respuesta de la API será:

```json
{
    "idioma": "ESPANISH",
    "porcentaje_espanish": 100,
    "porcentaje_english": 0.0
}
```

Esto indica que el texto está escrito en español y tiene un porcentaje de 
palabras en español del 100%.