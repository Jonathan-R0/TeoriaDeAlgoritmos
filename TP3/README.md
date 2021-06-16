# Teoría de Algoritmos
## Trabajo Práctico 2 

| Padrón | Alumno                    |
|--------|---------------------------|
| 104105 | Jonathan David Rosenblatt |
| 103924 | Joaquín Fontela           |
| 104330 | Agustín Ghersi            |
| 104429 | Thiago Kovnat             |

# Tabla de Contenidos

- [Ejercicio 1](#ejercicio-1)
    - [Mudanza es NP](#mudanza-es-np)
    - [Bin-Packing](#bin-packing)
    - [Bin-Packing es NP](#bin-packing-es-np)
    - [Bin-Packing es NP-Hard](#bin-packing-es-np-hard)
    - [Mudanza es NP-Completo](#mudanza-es-np-completo)
- [Ejercicio 2](#ejercicio-2)
- [Ejercicio 3](#ejercicio-3)

# Ejercicio 1

Vamos a demostrar que el problema es NP-Completo demostrando que Bin-Packing se puede reducir polinomialmente a nuestro problema. Con esto obtendremos que el problema a analizar es NP-Hard y solo faltaría demostrar que el mismo es NP.

## Mudanza es NP

Tenemos que mover, dentro de recipientes de volumen `V` una cantidad `n` elementos y podemos usar como máximo `r` recipientes tal que hagamos hasta `k` viajes. Debemos decidir si este problema es NP-Completo.

Primero tenemos que verificar que el problema es NP. Esto se realiza facilmente ya que la verificación consiste en:
- Tomar los elementos asignados a cada bin y verificar que sus correspondientes sumas no superen `V` (`O(n)`).
- No tener más de `r*k` de estos (`O(n)`).
- Ver que en cada viaje no se lleven más de `r` contenedores (`O(n)`). 

Como la verificación es polinomial llegamos a que el problema es NP.

## Bin-Packing

El problema de Bin-Packing consiste de tener una serie de items los cuales deben ser divididos en `m` cajas de volumen `V` y queremos ver si se puede asignar los elementos para que entren en las cajas. 

Con esto en mente podemos reducir Bin-Packing a nuestro problema, teniendo `m := r*k` cajas y un solo viaje.

Por lo tanto falta demostrar que Bin-Packing es NP-Completo.

### Bin-Packing es NP

Sea el set `X = {X[0], X[1], ..., X[n]}` de elementos. Debemos realizar algo muy parecido al caso anterior; pensemos que en la verificación recibimos `Y = {{Y_0[0], Y_0[1], ..., Y_0[z]}, ..., {Y_m[0], Y_m[1], ..., Y_m[z']}}` siendo que el i-ésimo elemento de Y es un set de los elementos de X que está asignado al i-ésimo bin. Por lo tanto la verificación consiste en verificar que la sumatoria de los elementos de cada subset no supere la capacidad máxima y que la cantidad total de subsets no supere la cantidad máxima de bins totales. Esto se hace en tiempo polinomial y por lo tanto es NP.

### Bin-Packing es NP-Hard

Vamos a demostrar que Bin-Packing es NP-Hard reduciendo al Partition Problem como una instancia de Bin-Packing. El problema de 2-partition se pregunta si puedo separar un set de números en un set dos elementos que sumen lo mismo y podemos reducir el problema a Bin-Packing con dos bins de `(b[0] + ... + b[n])/2` de volumen, siendo `{b[0], ..., b[n]}` el set de valores del problema de 2-partition (ajustamos a ese volumen pues es el la mitad de elementos que asignaremos a cada bin). Por lo tanto `2-PARTITION <p BIN-PACKING` y 2-Partition es un problema NP-Hard ⇒ Bin-Packing es igual o más complicado que 2-Partition ⇒ Bin-Packing es NP-Hard.

Por lo tanto, como Bin-Packing es un problema que pertenece a NP y NP-Hard, es NP-Completo.

## Mudanza es NP-Completo

Como `BIN-PACKING <p MUDANZA` y el problema de la mudanza es NP-Hard ⇒ Entonces es NP-Completo (Pues `NP-C = NP ∩ NP-Hard`).

# Ejercicio 2

# Ejercicio 3