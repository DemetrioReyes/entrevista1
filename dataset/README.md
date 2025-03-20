**README**

**Calculo de Coordenadas en Matriz 2D**

Este script proporciona una función para calcular la coordenada (x, y) de 
un elemento en una matriz 2D de 8x8.

La función `obtainer` toma como entrada el valor de una coordenada x 
(`row`) y una coordenada y (`col`). La salida es el valor correspondiente 
en la matriz, calculado utilizando la fórmula:

`valor = (row * 8 + col) % 32`

La función utiliza la propiedad de que un 2D de 8x8 se puede representar 
como un único número entero mediante una serie de operaciones aritméticas 
y módulos.

**Función**

* `obtainer(row, col)`: calcula el valor correspondiente en la matriz 2D 
de coordenadas (x, y)


**Nota**

* La matriz se representa como un espacio continuo con indices x e y que 
van del 0 al 7.
* El operador `%` se utiliza para obtener el resto de la división entre el 
valor calculado y 32, lo cual permite obtener el valor correspondiente en 
la matriz.

**Requisitos**

* Python 3.x
* Biblioteca `os` para obtener la ruta del archivo
