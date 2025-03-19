import * as fs from 'fs';
import * as path from 'path';

function readIni(): string {
    const currentDirectory = __dirname;
    const filePath = path.join(currentDirectory, 'dataset.ini');

    const data = fs.readFileSync(filePath, 'utf-8');
    return data;
}

const contenido = readIni();

function getValue(row: number, col: number): number {
    return (row * 8 + col) % 32;
}

function findDuplicates(data: string): Set<string> {
    const values = data.split(/\s+/);
    const duplicates = new Set<string>();
    const seen = new Set<string>();

    for (const value of values) {
        if (seen.has(value)) {
            duplicates.add(value);
        } else {
            seen.add(value);
        }
    }

    return duplicates;
}

const duplicados = findDuplicates(contenido);
const conteoDuplicados = duplicados.size;
console.log("Cantidad de valores duplicados:", conteoDuplicados);
console.log("Valores duplicados en dataset.ini:", Array.from(duplicados));

const row = 1;
const col = 8;
console.log("Valor en coordenadas:", row, col, getValue(row, col).toString(16));