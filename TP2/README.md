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
    - [Memoización](#memoización)
    - [Traceback](#traceback)
  - [Parte 3](#parte-3)
  - [Parte 4](#parte-4)
    - [Complejidad Temporal](#complejidad-temporal)
    - [Complejidad Espacial](#complejidad-espacial)
  - [Parte 5](#parte-5)
  - [Parte 6](./Comparaciones.ipynb)


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

El análisis del pseudocódigo y su respectiva presentación se dividirá en dos partes. Primero veremos como encontrar la máxima suma de cartas que podemos conseguir utilizando [_memoización_](https://en.wikipedia.org/wiki/Memoization) y luego, utilizando este recurso, generaremos el set de movimientos que realizó cada jugador.

### Memoización

Habiendo llegado a la relación de recurrencia pedida, nos damos cuenta de que para cada jugada debemos recorrer el árbol de decisiones que se forma en función de las jugadas futuras. Esto representa un costo temporal terrible pero afortunadamente lo podemos resolver con memoización. Computaremos en la matriz `mejores[i][j]` el resultado de `MP(i,j)` para evitar realizar cálculos ya previamente hechos en otras ramas del árbol de decisiones. 

El algoritmo iterativo para resolver el problema es el siguiente:

```
def max_pick(cartas):

    l = len(cartas)
    mejores = [[0 for _ in range(l)] for _ in range(l)]

    for resto in range(l):
        for f in range(resto, l):
            i = f - resto

            a = mejores[i + 2][f] if i + 2 <= f else 0
            b = mejores[i + 1][f - 1] if i + 1 <= f - 1 else 0
            c = mejores[i][f - 2] if i <= f - 2 else 0

            mejores[i][f] = max(cartas[i] + min(a, b), cartas[f] + min(b, c))
```

Donde la memoización ocurre guardando los datos de `MP(i,j)` en `mejores[i][j]`. Como la matriz se va llenando desde la diagonal hacia el tope superior derecho, la suma de las cartas que vamos a elegir es el elemento (`mejores[0][len(cartas) - 1]`) que representa `MP(0,len(cartas) - 1)`.

### Traceback

Tenemos el algorítmo de memoización, por lo que simplemente falta recorrer la matriz para llegar a obtener las jugadas.

```
def generarMisJugadas(cartas, mejores):
    i = 0
    f = len(cartas) - 1
    picks = []
    while f - i >= 2:
        seleccionInicial = cartas[i] + min(mejores[i + 2][f], mejores[i + 1][f - 1])
        seleccionFinal = cartas[f] + min(mejores[i + 1][f - 1], mejores[i][f - 2])
        picks.append(i if seleccionInicial > seleccionFinal else f)
        if seleccionInicial > seleccionFinal:
            if mejores[i + 2][f] < mejores[i + 1][f - 1]:
                i += 1
            else:
                f -= 1
            i += 1
        else:
            if mejores[i + 1][f - 1] < mejores[i][f - 2]:
                i += 1
            else:
                f -= 1
            f -= 1
    if f - i == 1:
        picks.append(i if cartas[i] > cartas[f] else f)
    else:
        picks.append(i)

    return [cartas[i] for i in picks]
```

En cada iteración del while vamos ingresando los índices de las cartas que son seleccionadas según el algorítmo de `MP(i,j)`. Si nos conviene más tomar del extremo `C[i]` agregamos `i` a la lista de resultados. ídem para `j`. Esto se calcula en función de [nuestra heurística antes analizada](#parte-1). Finalmente en el último condicional verificamos el caso base donde las carta posterior a `C[i]`es `C[j]`.

## Parte 3

Veremos como se ejecuta el ejemplo con las cartas `7,5,1,8`. Primero el algorítmo genera la matriz de datos:

```
[[ 7  7  8 13]
 [ 0  5  5  9]
 [ 0  0  1  8]
 [ 0  0  0  8]]
```

Donde la diagonal es el mazo y para cada posición guardamos la mejor jugada que podemos realizar en función de las coordenadas que evaluamos. Luego podemos ir viendo paso a paso como se ejecuta el algorítmo de generación de jugadas:

Empezamos con `i := 0` y `f := len(cartas) - 1`. Siguiendo el algorítmo vemos que punta nos conviene tomar. 

Tenemos que seleccionar el máximo entre `C[0] + min{mejores[2][3], mejores[1][3]} = 7 + min{1,5} = 8` y `C[3] = min{mejores[2][3], mejores[0][1]} = 8 + min{1,7} = 9` ⇒ la carta que nos generó el mayor valor fue `C[3]`; tomamos del extremo derecho (derecho viendo la pila de cartas de forma horizontal en vez de vertical).

Ahora nos quedamos con `7,5,1` pero como en la iteración anterior (donde llegamos a que elegimos el extremo derecho) dentro de la predicción tuvimos que elegir entre `min{mejores[2][3], mejores[0][1]} = min{1,7}` ya que sabemos que el oponente nos dejará la peor pila de cartas posibles. Por lo tanto, como `mejores[0][1] = 7` resulta ser mejor que `mejores[2][3] = 1` para el oponente, vemos que el mismo eligirá `C[0]`. 

Llegamos a la siguiente pila de cartas `5,1` donde nuestra selección es trivial y finalmente ganamos el juego. Nuestra selección de cartas fue `8,5` y el oponente jugó `7,1`. Sumamos `13`, el oponente `8` por lo que ganamos en nuestro ejemplo.

## Parte 4
 
### Complejidad Temporal

Para la complejidad temporal arrancamos viendo la parte de memoización. En las primeras dos lineas de este podemos suponer que las operaciones ocurren en `O(1)` (y aun si ocurre en `O(n^2)` no afectará a lo que le sigue).

La sección importante a analizar es el nested loop. Loopeamos la cantidad de veces necesarias como para realizar (n*n)/2 (siendo que `n := len(cartas)`) escrituras dentro de la matriz de datos dinámicos. Por lo tanto `T1(n) = O((n^2)/2) = O(n^2)/2 = O(n^2)`.

Dentro de la generación de las jugadas recorremos la matriz. Tenemos un loop que comienza con `i := 0, f := len(cartas) - 1`, donde vamos actualizando `i := i + 1` ó `f := f - 1` tal que estas dos variables se van acercando cada vez mas. El ciclo corta cuando son casi el mismo número (pues su diferencia debe ser mayor a dos) por lo que loopeamos `T2(n) = O(n)` veces.

Finalmente el tiempo total es `T(n) = T1(n) + T2(n) = O(n^2)`.

### Complejidad Espacial

Por lo mismo que se dijo en la [sección anterior](#complejidad-temporal) de que realizamos (n*n)/2 escrituras concluimos que necesitamos una matriz de n^2 posiciones ⇒ `E1(n) = O((n*2)/2) = O(n^2)/2 = O(n^2)`. 

En la función que genera los movimientos solamente tenemos los contadores y la lista de cartas. Esta lista tendrá la mitad (o mitad más uno si tenemos una cantidad de cartas impares) de cartas del mazo, lo cual es tamaño lineal `E2(n) = O(n/2) = O(n)`.

Por lo tanto nuestro tiempo es cuadrático: `E(n) = E1(n) + E2(n) = O(n^2)`.

## Parte 5

```
$ python .\main.py ./TestCases/mazo.txt
Jugador 1:
Cartas elegidas: 4,9,1
Puntos sumados: 14

Jugador 2:
Cartas elegidas: 6,5
Puntos sumados: 11

$ python .\main.py ./TestCases/cartas.txt
Jugador 1:
Cartas elegidas: 8,5
Puntos sumados: 13

Jugador 2:
Cartas elegidas: 7,1
Puntos sumados: 8
```

# Ejercicio 2

Se tiene una red de flujo $G(V,E)$ con $s$ como fuente y $t$ como sumidero.

Por la propiedad de corte de grafo, sabemos que una cota superior de mensajes a enviar hasta el agente T es la cantidad de mensajes que se pueden enviar desde la agencia S.

Conociendo la máxima cantidad de mensajes sin repetir agentes que se pueden enviar desde la agencia hasta el agente destino, se calcula cual es el 30% de esa cantidad, siendo esta la cantidad (redondeando para arriba) de mensajes necesarios a suprimir por parte del enemigo.

Conociendo esto, se suprime un agente del grafo y se evalúa cuantos mensajes es posible enviar sin el agente el cuestión. Esto se repite para cada agente de la agencia y el rival eliminara aquel agente que minimice la cantidad de mensajes que puede enviar la agencia al agente T.

Este proceso se repite hasta que la cantidad de mensajes que puede enviar la agencia sea menor al 70% de la cantidad original, minimizando de esta forma la cantidad de agentes a neutralizar por parte del rival y maximizando la cantidad de mensajes que no pueden enviarse al eliminar a un agente de la red.
