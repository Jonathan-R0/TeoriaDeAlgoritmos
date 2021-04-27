# Teoría de Algoritmos
## Trabajo Práctico 1 

| Padrón | Alumno                    |
|--------|---------------------------|
| 104105 | Jonathan David Rosenblatt |
| 103924 | Joaquín Fontela           |
| 104330 | Agustín Ghersi            |
| 104429 | Thiago Kovnat             |

# Tabla de Contenidos

- [Ejercicio 1](#ejercicio-1)
  - [Parte 1](#parte-1)
  - [Parte 3](#parte-3)
    - [Complejidad Temporal](#complejidad-temporal)
    - [Complejidad Espacial](#complejidad-espacial)
  - [Parte 4](#parte-4)
- [Ejercicio 2](#ejercicio-2)

# Ejercicio 1

## Parte 1

1) Primero vamos a demostrar lo pedido con un contraejemplo. La solución propuesta por la administración no es óptima, pues siguiendo el algorítmo introducido podriamos llegar a la siguiente situación:

Si tenemos la siguiente distribución de contratos:

- Contrato A: Lunes 9am hasta la 1pm (duración 4 hs)
- Contrato B: Lunes 2pm hasta las 6pm (duración 4 hs)
- Contrato C: Lunes 7am hasta las 12am (duración 5 hs)
- Contrato D: Lunes 12am hasta las 5pm (duración 6 hs)
- Contrato E: Lunes 5pm hasta las 10pm (duración 5 hs)

El algorítmo tomaría primero el contrato A pues es el que comienza antes que dura menos. Por lo tanto luego podrá elegir entre B y E para continuar (el resto no, pues se superponen y son incompatibles). Terminará eligiendo el contrato B pues dura menos que el contrato E y luego terminará la ejecución del algoritmo pues no tendrá más tareas compatibles para aceptar.

Esta aplicación del algoritmo resulta no devolver la solución óptima, pues elegir los contratos C, D y E brindaría un total de contratos (y horas) mayor al que brinda A y B.

```
+---------------------------------------------------------------+
             |     Lunes     |    |     Lunes     |            
             |   9am hasta   |    |   2pm hasta   |  
             |    la  1pm    |    |    las 6pm    |
+---------------------------------------------------------------+
        |    Lunes     |     Lunes     |      Lunes      |
        |  7am  hasta  |  12am  hasta  |   5pm  hasta    |  
        |   las 12am   |    las 5pm    |    las 10pm     |
+---------------------------------------------------------------+
```

Por lo tanto, como existe una solución mejor, podemos afirmar que el algorítmo no devuelve siempre la solución óptima. □

## Parte 3

### Complejidad Temporal

Para analizar la complejidad temporal podemos ver lo que ocurre en el pseudocódigo del algoritmo:

- Primero ordenamos el conjunto de pedidos. Esto, con un buen algorítmo de ordenado, será `O(n*log(n))`
- Luego entramos en un ciclo donde loopeamos por cada elemento del conjunto de pedidos de tamaño `n`, (y todas las operaciones interna al mismo son `O(1)`) lo cual hace que el mismo sea `O(n)`
- Por lo tanto la complejidad temporal total del algoritmo será `O(n*log(n)) + O(n)` lo cual se reduce a `O(n*log(n))` por propiedades de la cota [_Big O_](https://en.wikipedia.org/wiki/Big_O_notation).

### Complejidad Espacial

Analizar la complejidad espacial del algoritmo no resulta muy complicado, pues el set de soluciones, en el peor caso, tendrá tantos elemenos como pedidos ingresados. Esto podría ocurrir si, por ejemplo, todos los pedidos son consecutivos unos a otros y estos son todos compatibles entre si. Por lo tanto, la complejidad espacial es de `O(n)`.

## Parte 4

Aquí demostraremos que la solución programada por nosotros es óptima.

Para esto diremos que nuestro conjunto de pedidos es `P` tal que `|P| = n`, y al ejecutar nuestro algoritmo el resultado del mismo nos devuelve `A = {A[1], ..., A[k]}` tal que `|A| = k`. También diremos que la solución óptima al problema se denominará `O = {O[1], ..., O[m]}` tal que `|O| = m`.

Nosotros queremos demostrar que `A = O`, que es equivalente a `|A| = |O|` (ya que nuestro objetivo es maximizar la cantidad de pedidos compatibles que podemos agrupar). 

También tendremos una función `F`, la cual recibe un pedido y devuelve el horario en el que este finaliza y la función `S` que hace lo mismo que su contraparte pero para el horario de inicio del pedido.

En particular pedimos que el tiempo de finalización de cada tarea que elige nuestro algoritmo sea mejor o igual al que da la solución óptima ⇒ Pedir que `|A| = |O|` es equivalente a pedir `F(A[w]) <= F(O[w])` para todo `w in [1,k]`. 

El resto de la demostración se realizará con inducción. Primero empezamos con `r = 1`. Acá sabemos que `A[1]` (es decir, la primera tarea de nuestro resultado) terminá antes o a la vez que `O[1]` por la naturaleza de nuestro algoritmo ⇒ `F(A[1]) <= F(O[1])`.

Ahora asumimos que con `r-1 in [2,k]` la condición se cumple, es decir, `F(A[r-1]) <= F(O[r-1])` (hipótesis inductiva).

Si `F(A[r-1]) <= F(O[r-1])` y `F(O[r-1]) <= S(O[r])` ⇒ `F(A[r-1]) <= S(O[r])`.

Esta última inecuación significa que cuando nuestro algorítmo elige el pedido `A[r]` también estaba disponible para elegir al `O[r]`. Eso implica que, como el algorítmo seleccionó a `A[r]`, este "le convenía", es decir, finalizaba antes que `O[r]` ⇒ `F(A[r]) <= F(O[r])`. 

Podemos hacer el cambio de variables `r = w` ⇒ `F(A[w]) <= F(O[w])` para todo `w in [1,k]` ⇒ `|A| = |O|` ⇒ `A = O` ⇒ Nuestra solución es óptima. □

# Ejercicio 2

## Datos

Conocemos que tenemos una superficie de `n*n` metros cuadrados, donde podemos cubrir con baldosas la superficie del mismo. `n` es potencia de 2. Estas balosas tienen forma de 'L' y están compuestas por 3 bloques de un metro cuadrado. Debemos plantear un algorítmo óptimo que pueda llenar la superficie, dado que que en una posición `x,y` se encuentra un bloque de un metro cuadrado que no debe ser tapado. Es conveniente pensar a la superficie a cubrir como una matriz de baldosas.

## Recubrimiento

Antes de presentar el algorítmo que busque una solución, debemos demostrar que esta puede existir. Esto se logrará demostrando que los metros cuadrados de la superficie dada permiten posicionar baldosas sin dejar espacios libres y sin hacer cortes entre baldosas.

La demostración seguirá los siguientes pasos:

- Primero sabemos que como la superficie tiene `n*n` metros cuadrados, necesitaremos `n*n` baldosas de un metro cuadrado ⇒ Necesitamos que `n*n mod 3 ≡ 0` (ya que si esto cumple, cualquier superficie dada podrá ser recubierta de baldosas en 'L'). Utilizamos el operador `%` para reemplazar al módulo.

- Como `n` es una potencia de 2 ⇒ `n = 2^k` siendo `k` un número natural ⇒ tendremos que recubrir la superficie con `(n*n) - 1 = (2^k * 2^k) - 1 = 2^2k - 1` baldosas (el -1 aparece por la posición que no tenemos en cuenta por el sumidero). 

- Por lo tanto tenemos que demostrar que `2^2k - 1 % 3 = 0`. Lo podemos hacer por _inducción_:
  - _Con `k = 0`_ tenemos que `2^(2*0) - 1 % 3 = 1 - 1 % 3 = 0 % 3 = 0` se cumple la propiedad.
  - _Con `k = r`_ asumimos que la propiedad se cumple (hipótesis inductiva) ⇒ `2^2r - 1 % 3 = 0`
  - _Con `k = r+1`_ podemos ver que `2^(2*(r+1)) - 1 % 3 = 2^2r * 2^2 - 1 % 3 = 4*2^2r - 1 % 3 = (4*2^2r - 4 + 3) % 3 = (4(2^2r - 1) + 3) % 3 = (4(2^2r - 1) % 3 + 3 % 3) % 3` y como para `k = r` la propiedad se cumple, `(4 * 0 + 3 % 3) % 3 = (0 + 3 % 3) % 3 = 0 % 3 = 0`.

- Entonces, como se cumple la propiedad para `k = r` y `k = r+1` ⇒ La propiedad se cumple para todo `k`.

- Como `(2^2k - 1) % 3 = 0`, podemos cubrir toda nuestra superficie de `n*n` metros cuadrados con baldosas de 'L' sin realizar cortes ⇒ Existe la solución al algorítmo. □

