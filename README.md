
# Resultados del Taller: Decodificador 7 Segmentos

## 1. Diseño de la Tabla (Justificación de Patrones)

**Números 0-9**: Se utilizaron los patrones estándar.

* El **1** se dibujó a la **derecha** (segmentos b y c) por ser la convención de mayor legibilidad.
* El **6** se dibujó **cerrado** (segmento superior 'a' encendido) para evitar confusión con la letra 'b'.
* El **9** se dibujó **cerrado** (segmento inferior 'd' encendido) para diferenciarlo claramente de la letra 'q'.

**Valores 10-15 (Patrones Personalizados)**:

* **10 (1001001 - a, d, g)**: Tres líneas horizontales paralelas. Representa un símbolo de "menú" o una lista de niveles.
* **11 (0110110 - b, c, e, f)**: Dos barras verticales paralelas. Símbolo universal de "pausa" (como en controles multimedia).
* **12 (0011101 - c, d, e, g)**: Forma de cuenco o 'u' inferior. Representa un contenedor vacío o estado de espera de datos.
* **13 (1100011 - a, b, f, g)**: Círculo en la parte superior. Funciona como indicador de temperatura (grados) o posición superior.
* **14 (0011100 - c, d, e)**: Soporte o base en la mitad inferior. Indica el límite inferior o "suelo" en un nivel de medición.
* **15 (1001000 - a, d)**: Línea superior e inferior simultáneas. Representa visualmente los límites extremos (máximo y mínimo a la vez).

---

## 2. Resultados de Simulación

* **¿Qué verifica el Testbench?**: Las pruebas unitarias iteran sobre los 16 valores binarios posibles. En cada ciclo, inyectan el valor al decodificador y comparan que la salida coincida exactamente con la tabla `.txt`.
* **¿Por qué no hay errores?**: No hay mensajes de ERROR porque el decodificador es estrictamente combinacional. La lógica mapea directa e inmediatamente cada índice de la señal de entrada (`bcd`) a la fila respectiva de la tupla.
* **¿Qué representan los 7 bits?**: La señal `sseg` controla físicamente los LEDs del display. Cada bit corresponde al estado de encendido (1) o apagado (0) de los segmentos en el orden secuencial `a b c d e f g`.

---

## 3. Código HDL Generado

La herramienta `myhdl` transforma la tupla de búsqueda (LUT) en código VHDL. Esta estructura se sintetiza puramente como lógica combinacional en el hardware (tradicionalmente construida como un bloque de casos de enrutamiento múltiple o múltiplexores), lo que permite que transistores individuales activen las luces basándose en las entradas de 4 bits sin depender de un reloj.

---

## Ejecución del Proyecto

Para correr las pruebas unitarias y generar el código HDL, asegúrese de tener instaladas las dependencias:

```bash
pip install myhdl pytest
```
