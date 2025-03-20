import os

def read_file():
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, 'dataset.ini')

    with open(file_path, 'r') as file:
        data = file.read()
    return data

contenido = read_file()

def obtainer(row, col):
    return (row * 8 + col) % 32


row = 1
col = 8
print("Valor en coordenadas :", row, col, hex(obtainer(row, col)))