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
  - [Parte 2](#parte-2)

# Ejercicio 1

## Parte 1

Tenemos el conjunto de cartas el cual puede ser representado dentro de un vector de elementos, que van de 0 a n. Siendo que `|Cartas| = n`. Hay dos jugadores y cada uno puede sacar cartas de los extremos tal que el ganardor posee la máxima suma de estas.

Podemos usar este ejemplo `6,9,5,2,1,4` en el que se puede ejecutar el siguiente juego (siendo que nosotros somos el `P1`):

``` 
P1 -> 6, 5, 2 ⇒ Score(P1) = 6 + 5 + 2 = 13
P2 -> 9, 4, 1 ⇒ Score(P2) = 9 + 4 + 1 = 14
```

En el cual nosotros perderíamos. La estrategia de tomar el máximo entre los valores de los extremos no funciona. Nuestro problema acá fue que, en el corto plazo, no pudimos evitar que el otro jugador no acceda a la carta con el 9. 

Por lo tanto, como tenemos que elegir el movimiento óptimo a cada paso, podemos expresar así la recurrencia:

```
max_pick(inicio, fin) = max{C[inicio] + predicción(inicio), C[fin] + predicción(fin)}
```

Y solo nos faltaría resolver la predicción. Podemos plantear que la misma es la peor elección disponible que le queda al `P2`, es decir, el mínimo entre los extremos que quedarían. Si generalizamos el vector de cartas:

```
[C[i], C[i+1], ..., C[f-1], C[f]]
```

De los dos casos veamos primero lo que ocurre cuando elegimos el elemento del inicio. Si el oponente elige `C[i+1]` (cosa que implica que este sería el mejor movimiento para nuestro oponente ya que el mismo es igual de inteligente que nosotros) implica que nos tendremos que quedar con lo mejor que podemos llegar a obtener del resto del array que sería `max_pick(C[i+2],C[f])`. Pero como no sabemos si el oponente va a elegir `C[i+1]` o `C[f]` pedimos quedarnos con `min{max_pick(C[i+2],C[f]), max_pick(C[i+1], C[f-1])` para asi asegurarnos de obtener lo mejor posible en función del movimiento que va a realizar el oponente. 

Por lo tanto tenemos que elegir el máximo entre `C[i] + min{max_pick(C[i+2],C[f]), max_pick(C[i+1], C[f-1])}` y `C[f] + min{max_pick(C[i], C[f-2]), max_pick(C[i+1], C[f-1])}` (ya que contemplamos la misma situación, pero cuando nosotros elegimos desde el final).

``` 
MP(i,f) =  max{C[i] + min{MP(C[i+2],C[f]), MP(C[i+1], C[f-1])}, C[j] + min{MP(C[i], C[f-2]), MP(C[i+1], C[f-1])}}
```

## Parte 2

El algoritmo iterativo para resolver el problema es el siguiente:


