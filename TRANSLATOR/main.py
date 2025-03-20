from fastapi import FastAPI
import re
import uvicorn
from idiomas import SPANISH, ENGLISH  # Importa directamente desde el archivo idiomás.py


app = FastAPI()

def detectar_idioma(texto):
    # aqui separamos las palabras del texto y las pasamos a minúsculas
    palabras = re.findall(r'\b\w+\b', texto.lower())
    
    # Contar palabras que aparecen en las listas de referencia
    conteo_spanish = sum(1 for palabra in palabras if palabra in SPANISH)
    conteo_english = sum(1 for palabra in palabras if palabra in ENGLISH)

    
    total = conteo_spanish + conteo_english
    if total == 0:
        return {"mensaje": "No se pudo determinar el idioma"} # si no se encontraron palabras en ninguna lista, no se puede determinar el idioma
    
    porcentaje_es = (conteo_spanish / total) * 100 # se calcula el porcentaje de palabras en español
    porcentaje_en = (conteo_english / total) * 100 # se calcula el porcentaje de palabras en inglés
    
    resultado = "ESPANISH" if porcentaje_es > porcentaje_en else "ENGLISH" # si el porcentaje de palabras en español es mayor, se determina que el idioma es español, de lo contrario, se determina que es inglés
    return {"idioma": resultado, "porcentaje_espanish": porcentaje_es, "porcentaje_english": porcentaje_en} # se regresa el resultado

@app.post("/detectar")  # ruta para detectar el idioma
async def detectar(texto: str): 
    return detectar_idioma(texto) # se llama a la función detectar_idioma con el texto que se recibe en la petición

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
