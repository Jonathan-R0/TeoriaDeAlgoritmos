# Teoría de Algoritmos
## Trabajo Práctico 1 

| Padrón | Alumno                    |
|--------|---------------------------|
| 104105 | Jonathan David Rosenblatt |
| 103924 | Joaquín Fontela           |
| 104330 | Agustín Ghersi            |
| 104429 | Thiago Kovnat             |

# Tabla de Contenidos

- [Parte 1](#parte-1)
- [Parte 3](#parte-3)
  - [Complejidad Temporal](#complejidad-temporal)
  - [Complejidad Espacial](#complejidad-espacial)
- [Parte 4](#parte-4)

# Parte 1

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

# Parte 3

## Complejidad Temporal

Para analizar la complejidad temporal podemos ver lo que ocurre en el pseudocódigo del algoritmo:

- Primero ordenamos el conjunto de pedidos. Esto, con un buen algorítmo de ordenado, será `O(n*log(n))`
- Luego entramos en un ciclo donde loopeamos por cada elemento del conjunto de pedidos de tamaño `n`, (y todas las operaciones interna al mismo son `O(1)`) lo cual hace que el mismo sea `O(n)`
- Por lo tanto la complejidad temporal total del algoritmo será `O(n*log(n)) + O(n)` lo cual se reduce a `O(n*log(n))` por propiedades de la cota [_Big O_](https://en.wikipedia.org/wiki/Big_O_notation).

## Complejidad Espacial

Analizar la complejidad espacial del algoritmo no resulta muy complicado, pues el set de soluciones, en el peor caso, tendrá tantos elemenos como pedidos ingresados. Esto podría ocurrir si, por ejemplo, todos los pedidos son consecutivos unos a otros y estos son todos compatibles entre si. Por lo tanto, la complejidad espacial es de `O(n)`.

# Parte 4

Aquí demostraremos que la solución programada por nosotros es óptima.