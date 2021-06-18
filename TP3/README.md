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
    - [Barcos es NP](#barcos-es-np)
    - [4 Pack](#4-pack)
        - [3SAT a 4SAT](#3sat-a-4sat)
        - [4SAT a Barcos](#4sat-a-barcos)
    - [2 Pack](#2-pack)
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

Tenemos `n` packs que los clientes pueden comprar para sus barcos y `m` restricciones que deben cumplir, tal que cada pack puede activar o desactivar la validez de cierta restricción. Demostraremos en las siguientes partes como diferentes variaciones del problema son NP-C.

## Barcos es NP

La demostración de que este problema es NP es bastante trivial. Si tengo el set de packs que un cliente puede comprar y verificar que todas las restricciones se cumplan y ninguna se desactive (comprobación de los tokens):

```
def validarPacks(packs, restricciones):
    i = 0
    for pack in packs: 
        restricciones[i].activarse(pack) 
        /* Verifica si tengo alguna restricción por cubrir con mi i-ésimo pack. */
        i++
    j = 0
    for pack in packs: 
        restricciones[i].desactivarse(pack) 
        /* Verifica si estoy rompiendo alguna restricción con mi j-ésimo pack. */
        j++  
    for restriccion in restricciones:
        if restriccion.noActivada:
            return False
    return True
```

El pseudocódigo a lo sumo verificará todos los packs y restricciones. Esto resulta ser `O(n+m)` y como esto es polinomial vemos que nuestro problema pertenece a NP.

## 4 Pack 

Para este problema realizaremos el análisis tal que cada restricción a cumplir está atado a 4 packs, donde cada uno puede activarlo o desactivarlo. Para resolver el problema vamos a saltar de 3SAT a 4SAT y finalmente a nuestro problema demostrando que `3SAT <p BARCOS`.

### 3SAT a 4SAT

Primero supongamos que tenemos la siguiente instancia de 3SAT:

``` 
3SAT(X1, X2, ..., Xn) = (Xa || Xb || Xc) && ... && (Xw || Xy || Xz) 
``` 

Donde tengo una gran expresión booleana en su forma conjuntiva, tal que cada `Xi` pertenece a `{X1, X2, ..., Xn, ¬X1, ¬X2, ..., ¬Xn}`.

Podemos analizar la siguiente expresión:

(A || B || C) = (A || B || C || Z) && (A || B || C || ¬Z)
 
Viendo como cada resultado de la expresión izquierda (dentro de su tabla de verdad):

<br><div align="center"><img src="media/tt1.jpg" style="max-width: 50%;"></div><br>

Mappea perfectamente a la expresión derecha (números rojos) independientemente del estado de veracidad de Z: 

<br><div align="center"><img src="media/tt2.jpg" style="max-width: 50%;"></div><br>

Llegamos a que podemos expresar nuestra función original como: 

``` 
(Xa || Xb || Xc) && ... && (Xw || Xy || Xz) = (Xa || Xb || Xc || Z) && (Xa || Xb || Xc || ¬Z) && ... && (Xw || Xy || Xz || T) && (Xw || Xy || Xz || ¬T) 
``` 

Por lo que nuestra función general de 3SAT es una instancia del problema de 4SAT donde la cuarta variable booleana de nuestra ecuación en forma conjuntiva tiene la restricción de siempre aparecer simétricamente sumando en un término (or) y sumando el negado en el otro (or not). Y habiendo demostrado que las expresiones booleanas matchean por tablas de verdad, cualquier solución de mi sistema de 3SAT puede resolver esta instancia particular de 4SAT y por lo tanto: `3SAT <p 4SAT` pues 4SAT es tan o más difícil que 3SAT.

Por lo tanto 4SAT pertenece a NP-Hard y obviamente pertenece a NP (pues la verificación de la solución consiste en reemplazar los valores en la función y ver que evalue en True, algo que se resuelve en tiempo polinómico) por lo que es NP-C.

### 4SAT a Barcos

## 2 Pack

# Ejercicio 3