**Proyecto de Análisis de Palabras**

Este proyecto utiliza Node.js y las bibliotecas `fs` (File System) y 
`path` para leer un archivo `data.txt`, contar la frecuencia de cada 
palabra única y mostrar las 10 palabras más frecuentes.

**Funcionamiento**

El proyecto tiene tres funciones principales:

*   `readIni()`: Lee el contenido del archivo `data.txt` y devuelve la 
información como cadena de texto.
*   `countWords(text)`: Divide el texto en palabras individuales, crea un 
mapa que almacena cada palabra con su frecuencia correspondiente y 
devuelve el mapa resultante.
*   `ToptenWords(wordCount)`: Utiliza el mapa de frecuencias para ordenar 
las palabras en función de su conteo en descenso, toma las 10 primeras 
palabras y devuelve un arreglo asociativo que contiene la palabra y su 
frecuencia.

**Funcionalidad**

La API tiene las siguientes características:

*   **Lectura de archivo**: El proyecto puede leer el contenido de un 
archivo llamado `data.txt` ubicado en la misma ruta donde se ejecuta el 
script.
*   **Análisis de palabras**: La API puede contar cuántas veces aparece 
cada palabra única en el texto.
*   **Muestra top 10**: La API muestra las 10 palabras más frecuentes y su 
respectivo conteo.

**Funciones**

La API tiene las siguientes funciones principales:

*   `readIni()`: Lectura del archivo `data.txt`
*   `countWords(text)`: Conteo de palabras en el texto
*   `ToptenWords(wordCount)`: Mostrado de las 10 palabras más frecuentes

**Dependencias**

El proyecto depende de las siguientes bibliotecas:

*   `fs` (File System)
*   `path`
