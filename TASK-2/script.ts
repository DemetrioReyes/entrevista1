import * as fs from 'fs';
import * as path from 'path';

// Lectura del archivo data.txt
function leerArchivo(): string {
    const directorioActual = __dirname;
    const rutaArchivo = path.join(directorioActual, 'data.txt');

    return fs.readFileSync(rutaArchivo, 'utf-8');
}

const contenido = leerArchivo();

// Función para contar la frecuencia de las palabras en el texto
function contarPalabras(texto: string): Map<string, number> {
    const palabras = texto.toLowerCase().replace(/[^a-záéíóúüñ\s]/gi, '').split(/\s+/);
    const conteoPalabras = new Map<string, number>();
    
    for (const palabra of palabras) {
        if (!palabra) continue;
        if (conteoPalabras.has(palabra)) {
            conteoPalabras.set(palabra, (conteoPalabras.get(palabra) as number) + 1);
        } else {
            conteoPalabras.set(palabra, 1);
        }
    }
    return conteoPalabras;
}

const conteo = contarPalabras(contenido);

// Mostrar las 10 palabras más frecuentes
function palabrasMasFrecuentes(conteo: Map<string, number>): [string, number][] {
    return Array.from(conteo.entries())
        .sort((a, b) => b[1] - a[1])
        .slice(0, 10);
}

const topDiez = palabrasMasFrecuentes(conteo);
console.log(topDiez);
