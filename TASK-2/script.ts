import * as fs from 'fs';
import * as path from 'path';

// ● lectura del archivo data.txt

function readIni(): string {
    const currentDirectory = __dirname;
    const filePath = path.join(currentDirectory, 'data.txt');

    const data = fs.readFileSync(filePath, 'utf-8');
    return data;
}

const contenido = readIni();
// console.log(contenido);

// ● Cuenta cuántas veces aparece cada palabra única en el archivo (ya sabes, para que te des cuenta de cuántas veces se repite "the").

function countWords(text: string): Map<string, number> {
    const words = text.split(' ');
    const wordCount = new Map<string, number>();
    
    for (const word of words) {
        const currentCount = wordCount.get(word) || 0;
        wordCount.set(word, currentCount + 1);
    }

    return wordCount;
}

const wordCount = countWords(contenido);
console.log(wordCount);

// ● Muestra las 10 palabras más frecuentes y sus respectivos conteos

function ToptenWords(wordCount: Map<string, number>): [string, number][] {
    const sortedWords = Array.from(wordCount.entries()).sort((a, b) => b[1] - a[1]);
    return sortedWords.slice(0, 10);
}

const topTen = ToptenWords(wordCount);
console.log(topTen);



