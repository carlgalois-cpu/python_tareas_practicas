# Reporte de Casos de Prueba

| ID | Descripción | Datos de entrada | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| 01 | Un depósito recién creado tiene nivel 0. | `new Deposito("Test", 10.0)` | `0.0` | `0.0` | **Aprobado** |
| 02 | Se puede agregar una cantidad positiva válida. | `agregarAgua(5.0)` | `true`, nivel `5.0` | `true`, nivel `5.0` | **Aprobado** |
| 03 | No se puede agregar cantidad que supere la capacidad. | nivel inicial `0`, `agregarAgua(11.0)` | `false`, nivel `0.0` | `false`, nivel `0.0` | **Aprobado** |
| 04 | No se puede agregar cero. | `agregarAgua(0.0)` | `false` | `false` | **Aprobado** |
| 05 | No se puede agregar cantidad negativa. | `agregarAgua(-5.0)` | `false` | `false` | **Aprobado** |
| 06 | No se puede agregar NaN ni infinito. | `agregarAgua(Double.NaN)`, `agregarAgua(Double.POSITIVE_INFINITY)` | `false` | `false` | **Aprobado** |
| 07 | Se puede extraer agua cuando hay suficiente. | nivel inicial `8.0`, `servirAgua(5.0)` | `true`, nivel `3.0` | `true`, nivel `3.0` | **Aprobado** |
| 08 | No se puede extraer más agua de la disponible. | nivel inicial `5.0`, `servirAgua(6.0)` | `false`, nivel `5.0` | `false`, nivel `5.0` | **Aprobado** |
| 09 | No se puede extraer cero ni negativo. | `servirAgua(0.0)`, `servirAgua(-2.0)` | `false` | `false` | **Aprobado** |
| 10 | Una operación rechazada no modifica el nivel. | nivel `5.0`, fallar `agregar(20)` | `false`, nivel `5.0` | `false`, nivel `5.0` | **Aprobado** |
| 11 | El nivel nunca queda por debajo de cero. | nivel `10.0`, servir `10.0` | `>= 0` | `>= 0` | **Aprobado** |
| 12 | El nivel nunca supera la capacidad máxima. | nivel `10.0` en cap `10` | `<= 10` | `<= 10` | **Aprobado** |
| 13 | Los dos depósitos mantienen estados independientes. | D1 agrega `5.0`, D2 nivel `0` | D2 nivel `0` | D2 nivel `0` | **Aprobado** |
| 14 | El programa permite completar 4 operaciones. | (Prueba manual de ciclo while) | Iterar 4 veces | Iterar 4 veces | **Aprobado** |
| 15 | Los estados finales se muestran correctamente. | Llamar a `mostrarEstado()` | Formato impreso ok | Formato impreso ok | **Aprobado** |

> *Nota: Todas las pruebas programáticas fueron ejecutadas con éxito empleando la clase `TestDepositoAgua.java`.*
