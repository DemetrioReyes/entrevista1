import os

def read_ini():
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, 'dataset.ini')

    with open(file_path, 'r') as file:
        data = file.read()
    return data

contenido = read_ini()

def get_value(row, col):
    return (row * 8 + col) % 32

def find_duplicates(data):
    values = data.split()
    duplicates = set()
    seen = set()
    
    for value in values:
        if value in seen:
            duplicates.add(value)
        else:
            seen.add(value)
    
    return duplicates

duplicados = find_duplicates(contenido)
conteo_duplicados = len(duplicados)
print("Cantidad de valores duplicados:", conteo_duplicados)
print("Valores duplicados en dataset.ini:", duplicados)
row = 1
col = 8
print("Valor en coordenadas :", row, col, hex(get_value(row, col)))