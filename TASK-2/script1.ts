import * as fs from 'fs';
import * as path from 'path';
import { Worker, isMainThread, parentPort, workerData } from 'worker_threads';

function countWords(text: string): Map<string, number> {
    const words = text.split(/\s+/);
    const wordCount = new Map<string, number>();
    
    for (const word of words) {
        const currentCount = wordCount.get(word) || 0;
        wordCount.set(word, currentCount + 1);
    }

    return wordCount;
}

function topTenWords(wordCount: Map<string, number>): [string, number][] {
    const sortedWords = Array.from(wordCount.entries()).sort((a, b) => b[1] - a[1]);
    return sortedWords.slice(0, 10);
}

if (isMainThread) {
    const currentDirectory = __dirname;
    const files = ['data.txt'];
    const results: Map<string, number>[] = [];
    let completedWorkers = 0;

    files.forEach((file) => {
        const filePath = path.join(currentDirectory, file);
        const worker = new Worker(__filename, {
            workerData: filePath,
            execArgv: ['-r', 'ts-node/register']
        });

        worker.on('message', (wordCount: Map<string, number>) => {
            results.push(wordCount);
            completedWorkers++;

            if (completedWorkers === files.length) {
                const combinedWordCount = new Map<string, number>();
                results.forEach((result) => {
                    result.forEach((count, word) => {
                        const currentCount = combinedWordCount.get(word) || 0;
                        combinedWordCount.set(word, currentCount + count);
                    });
                });

                const topTen = topTenWords(combinedWordCount);
                console.log(topTen);
            }
        });

        worker.on('error', (err) => {
            console.error(`Worker error: ${err}`);
        });

        worker.on('exit', (code) => {
            if (code !== 0) {
                console.error(`Worker stopped with exit code ${code}`);
            }
        });
    });
} else {
    const filePath = workerData;
    const readStream = fs.createReadStream(filePath, { encoding: 'utf-8' });
    let fileContent = '';

    readStream.on('data', (chunk) => {
        fileContent += chunk;
    });

    readStream.on('end', () => {
        const wordCount = countWords(fileContent);
        parentPort?.postMessage(wordCount);
    });

    readStream.on('error', (err) => {
        console.error(`Error reading file: ${err}`);
    });
}