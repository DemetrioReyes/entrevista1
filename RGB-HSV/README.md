
Este script proporciona funciones para convertir entre el espacio RGB a 
HSV.

La función `rgb_to_hsv` toma como entrada un array de tres valores 
numéricos entre 0 y 255 que representan los componentes R, G y B de una 
imagen. La salida es un array con tres componentes: el Hue (tono), la 
Saturation (saturnidad) y la Valor (valor).

La función `hsv_to_rgb` toma como entrada un array de tres valores 
numéricos que representan el Hue, la Saturación y el Valor en el espacio 
HSV. La salida es un array con tres componentes: R, G y B.

Fuente : https://en.wikipedia.org/wiki/HSL_and_HSV

**Funciones**

* `rgb_to_hsv(rgb)`: convierte un color RGB a HSV
* `hsv_to_rgb(hsv)`: convierte un color HSV a RGB

**Ejemplo de Uso**

```python
rgb_input = np.array([180, 53, 89])  # Color RGB en formato int entre 0 y 
255
hsv = rgb_to_hsv(rgb_input)
rgb_output = hsv_to_rgb(hsv)

print('RGB to HSV', hsv)
print('RGB', rgb_output)
```
