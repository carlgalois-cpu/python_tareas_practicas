# POO-Java-Depositos

## Objetivo del Programa
El objetivo de este proyecto es simular un sistema de gestión de depósitos de agua (Laboratorio y Taller) utilizando Java. El programa permite añadir o servir agua de los depósitos siguiendo reglas estrictas de validación.

## Conceptos de POO Utilizados
- **Clases y Objetos:** Se definió la clase `DepositoAgua` para instanciar los depósitos.
- **Encapsulamiento:** El estado del depósito (`nivelActual`, `capacidadMaxima`) es privado y solo se puede alterar a través de métodos seguros (`agregarAgua`, `servirAgua`).

## Responsabilidad de cada clase
- **`DepositoAgua`**: Mantiene el estado del depósito, valida las operaciones solicitadas (añadir/servir) garantizando que no se rompan las reglas de negocio (ej. no desbordar ni quedar en negativo).
- **`Main`**: Gestiona la interfaz por consola, lee la entrada del usuario, la valida y despacha las acciones correspondientes a los objetos.
- **`TestDepositoAgua`**: Ejecuta aserciones para asegurar que el comportamiento de la clase `DepositoAgua` es el esperado bajo diversas circunstancias (pruebas unitarias locales).

## Atributos y Métodos de `DepositoAgua`
- **Atributos (privados):**
  - `ubicacion`: Nombre/Lugar del depósito (String).
  - `capacidadMaxima`: Límite máximo de litros que soporta (double).
  - `nivelActual`: Cantidad de litros actuales en el depósito (double).
- **Métodos:**
  - `agregarAgua(double litros)`: Incrementa el nivel si la cantidad es válida y no supera la capacidad máxima.
  - `servirAgua(double litros)`: Disminuye el nivel si la cantidad es válida y hay suficiente agua.
  - *Getters* para consultar cada atributo y `mostrarEstado()` para imprimir información por pantalla.

## Reglas de Validación
- Las cantidades a sumar o restar deben ser numéricas, positivas, finitas (no Infinito ni NaN).
- El nivel del agua siempre debe mantenerse en el rango: `0 <= nivelActual <= capacidadMaxima`.
- Operaciones inválidas retornan `false` y conservan el estado intacto.

## Compilar el Programa
Asegúrate de estar en el directorio raíz del proyecto (`POO-Java-Depositos`) y ejecuta:
```bash
javac -d out src/*.java pruebas/*.java
```

## Ejecutar el Programa Principal
```bash
java -cp out src.Main
```

## Ejecutar las Pruebas
Para correr las aserciones, es imprescindible habilitarlas con el flag `-ea` (enable assertions):
```bash
java -ea -cp out pruebas.TestDepositoAgua
```

## Ejemplo de uso (Ejecución Interactiva)
```text
=== SISTEMA DE GESTIÓN DE DEPÓSITOS DE AGUA ===

Operación 1 de 4
Seleccione el depósito:
1. Laboratorio (Capacidad: 10L)
2. Taller (Capacidad: 6L)
Opción: 1
Seleccione la acción:
1. Agregar agua
2. Servir agua
Opción: 1
Ingrese la cantidad de litros: 7
Resultado: true. Se han agregado 7.0 litros al depósito de Laboratorio.
...
```
