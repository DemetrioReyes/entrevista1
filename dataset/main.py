import os

def read_file():
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, 'dataset.ini')

    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def obtainer(row, col, data):
    # Convertir la fila en índice de lista (0-based)
    row_index = row - 1
    # Convertir la columna en índice de lista (0-based)
    col_index = col - 1

    # Obtener la fila correspondiente
    row_data = data[row_index].strip().split()
    
    # Obtener el valor en la columna correspondiente
    value = row_data[col_index]
    
    return value

data = read_file()

row = 1
col = 8
print("Valor en coordenadas :", row, col, obtainer(row, col, data))