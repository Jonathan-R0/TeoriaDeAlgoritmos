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
- [Ejercicio 2](#ejercicio-2)
  - [Parte 1](#parte-1)
  - [Parte 2](#parte-2)
    - [Complejidad Temporal](#complejidad-temporal)
    - [Complejidad Espacial](#complejidad-espacial)
  - [Parte 3](#parte-3)

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

Tenemos que seleccionar el máximo entre `C[0] + min{mejores[2][3], mejores[1][3]} = 7 + min{1,5} = 8` y `C[3] + min{mejores[2][3], mejores[0][1]} = 8 + min{1,7} = 9` ⇒ la carta que nos generó el mayor valor fue `C[3]`; tomamos del extremo derecho (derecho viendo la pila de cartas de forma horizontal en vez de vertical).

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

## Parte 1

Se tiene una red de flujo `G(V,E)` con `s` como fuente y `t` como sumidero: `s` sería la agencia y `t` seria el agente destino. Se remueve cualquier arista saliente de `t` para poder utilizar una red de flujo.

El primer problema que se tiene que resolver es como un vertice (un espia) solo puede ser utilizado una sola vez por la agencia. Lo que queremos encontrar es la cantidad maxima de caminos vertice-disjuntos que hay en el grafo. Este problema se puede pasar facilmente a encontrar la mayor cantidad de caminos arista-disjuntos en un grafo. Lo que debemos hacer es descomponer cada vertice (salvo `s` y `t`) en dos vertices: Un vertice que "reciba" todos los mensajes y otro que "emita" todos los mensajes. Luego, simplemente conectamos estos dos vertices por una arista de capacidad 1, asegurandonos que cada agente solo se pueda utilizar unicamente una vez.

Asignandole una capacidad de 1 a cada arista, al aplicar un algoritmo que nos de el flujo maximo el resultado será la cantidad de caminos arista-disjuntos que hay en el grafo, y dado que reducimos nuestro problema original a este en un paso anterior, podemos determinar que la cantidad maxima de caminos arista-disjuntos equivale a la cantidad maxima de caminos vertice-disjuntos en el grafo. Llamemos a este número `Y`.

Por propiedades del grafo, también sabemos una cota superior de la cantidad posible de caminos vertice-disjuntos entre `s` y `t` es la cantidad de vertices a los que conecta `s`. Llamemos a este numero `Z`.

Siendo `X` el numero minimo de espías a remover para reducir en un 30% la cantidad maxima de mensajes que se le puede mandar a `t` desde `s`, tenemos que:

`X < Y <= Z`

Conociendo la máxima cantidad de mensajes sin repetir que se pueden enviar desde la agencia hasta el agente destino, se calcula cual es el 30% de esa cantidad, siendo esta la cantidad (redondeando para arriba) de mensajes necesarios a suprimir por parte del enemigo.

Conociendo esto, se suprime un agente del grafo y se evalúa cuantos mensajes es posible enviar sin el agente el cuestión. Esto se repite para cada agente de la agencia y el rival eliminara aquel agente que minimice la cantidad de mensajes que puede enviar la agencia al agente T.

Este proceso se repite hasta que la cantidad de mensajes que puede enviar la agencia sea menor al 70% de la cantidad original, minimizando de esta forma la cantidad de agentes a neutralizar por parte del rival y maximizando la cantidad de mensajes que no pueden enviarse al eliminar a un agente de la red.

El pseudocódigo del algoritmo es asi:

```
def minCantidadDeEspias(grafo, agencia, destino):

    grafoAux = transformarAProblemaAristaDisjunto(grafo)
    
    cantidadMaximaDeMensajes = MaximizeFlow(grafo, agencia, destino)
    mensajesPosibles = cantidadMaximaDeMensajes
    agentesEliminados = {}
    
    while mensajesPosibles > (cantidadMaximaDeMensajes * 0.7):
    
        maxPosibilidadesEliminadas = -∞
        agenteEliminado = ∅
        
        for agente in grafoAux.vertices:
            
            g' = grafoAux - {agente}
            
            cantidadPosible = MaximizeFlow(g', agencia, destino)
            posibilidadesEliminadas = cantidadMaximaDeMensajes - cantidadPosible
            
            if posibilidadesEliminadas > maxPosibilidadesEliminadas:
              
                maxPosibilidadesEliminadas = posibilidadesEliminadas
                agenteEliminad = agente
         
        mensajesPosibles -= maxPosibilidadesEliminadas
        agentesEliminados += {agente} 
        grafoAux -= {agenteEliminado}
       
   return size(agentesEliminados)
```

## Parte 2

### Complejidad Temporal

En primer lugar transformamos el problema a uno de arista disjunto. Para eso tenemos que duplicar la cantidad de vértices disponibles tal que para cada vértice `v` tendremos un `e = (v_in, v_out)` de capacidad 1. Esto es `O(|V|)`. Luego computamos el maxflow del grafo con el algorítmo de Edmonds–Karp el cual opera en tiempo `O(|V|*|E|^2)`.

Posteriormente entramos en un while loop en el que iteramos hasta que conseguimos un grafo en el que la cantidad de mensajes reducidos sean menores al 70%. Dentro del mismo ejecutamos otro loop que puede llegar a ejecutarse `|V|` veces. Como computamos `|V|^2` veces el maxflow con Edmonds–Karp llegamos a una complejidad temporal de `O(|V|^3*|E|^2)`. 

Por lo tanto: `T(n) = O(|V|^3*|E|^2) + O(|V|) + O(|V|*|E|^2) = O(|V|^3*|E|^2)`. El tiempo es polinomial, pues es un producto de dos polinomios.

<br><div align="center"><img src="media/itiswhatitis.jpg" style="max-width: 50%;"></div><br>

### Complejidad Espacial

Representando el grafo como una matriz de adyacencia la complejidad de almacenar la misma es `O(|V|^2)`. Almacenar los agentes en la lista es, a lo sumo, `O(|V|)`. Por lo tanto `E(|V|) = O(|V|^2)`. El costo en memoria de la solución es efectivamente polinomial.

## Parte 3

Primero, cada vertice en este grafo, salvo 0 (fuente) y 5 (destino), representa en realidad 2 nodos: Uno para todas las aristas entrantes y otro para todas las aristas salientes. Estos vertices se conectan entre ellos por una arista del vértice entrante al saliente con capacidad 1. Por simplicidad en este gráfico, se representan como un solo vertice.

Sea G(V,E) el grafo que se representa en la imagen. Calculando el Max-Flow podemos observar que la maxima cántidad de caminos vértice disjuntos para este grafo es de 2.

<br><div align="center"><img src="media/0.png" style="max-width: 50%;"></div><br>

En la primera iteración, eliminamos el vértice 1 y calculamos el Max-Flow nuevamente. Como podemos observar, la cantidad máxima de caminos vértice disjuntos sigue siendo 2, por lo que eliminar el vértice 1 no afectó (En lenguaje natural, el mensaje se transmitió por una vía alternativa: 0-2-4-5)
<br><div align="center"><img src="media/1.png" style="max-width: 50%;"></div><br>

En la segunda iteración, eliminamos el vértice 2 y calculamos el Max-Flow. Podemos observar que la cantidad máxima de caminos vértice disjuntos no cambio ya que sigue siendo 2, por lo que eliminar el vértice 2 no afectó.
<br><div align="center"><img src="media/2.png" style="max-width: 50%;"></div><br>

En una tercera iteración, removemos el vértice 3 y, calculando el Max-Flow, podemos observar que la cantidad máxima de caminos vértice disjuntos disminuyó a 1. Por el momento, guardamos a 3 como el vértice óptimo a remover en esta iteración.
<br><div align="center"><img src="media/3.png" style="max-width: 50%;"></div><br>

En la última iteración, removemos el vértice 4 y, tras calcular el Max-Flow, podemos observar que la cantidad máxima de caminos vértice disjuntos disminuyó también a 1.
<br><div align="center"><img src="media/4.png" style="max-width: 50%;"></div><br>

Finalmente, podemos concluir que la cantidad minima de espias a eliminar para reducir en un 30% la cantidad posibles de mensajes posibles al espia destino es 1. Además, nuestro algoritmo nos brinda información de que espias son los que deben ser eliminados. En este caso, podríamos eliminar tanto el vértice 4 como el vértice 3 para obtener el resultado buscado.

# Correcciones

## Ejercicio 2

En las correcciones, se remarcó que el algoritmo presentado no era óptimo ya que calculaba varias veces el flujo maximo en la parte greedy del algoritmo. Para mejorar esto, podemos utilizar el teorema de Menger y las propiedades del corte mínimo. El Teorema de Menger nos dice que la cantidad de vertices a eliminar para desconectar dos vertices no adyacentes es equivalente a la cantidad de caminos vertice-disjuntos entre esos vertices. Nosotros sabemos, como dijimos en la entrega original, que podemos reducir el problema de la cantidad de caminos vertice disjuntos a uno de cantidad de caminos arista disjuntos modificando el grafo para acomodarse a este problema. Luego, con todas las aristas de capacidad 1, calcular el flujo máximo nos da la cantidad de caminos arista disjuntos y a su vez, por como modificamos el grafo, la cantidad de caminos vertice-disjuntos. 

Podemos obtener un corte mínimo que atraviese las aristas "artilugio". Luego, por propiedad, sabemos que si el flujo máximo es f, y sea e una arista que atraviesa el corte mínimo mencionado anteriormente, remover la arista e hace que el flujo maximo posible sea f - C(e). Por lo tanto, remover estas aristas de capacidad 1 efectivamente decrementan la cantidad de mensajes posibles entre la central y el espia destino ya que, como dijimos, el flujo es equivalente a la cantidad de caminos vertice disjuntos que hay en el grafo y esto, a su vez, equivale a la cantidad de mensajes posibles que podemos enviarle al espía. Ademas, remover esta arista "artilugio" es equivalente a eliminar el vertice en el grafo original, ya que por como esta formado el grafo, remover esta arista elimina cualquier posibilidad de que exista un camino que utilize este vertice.

Por lo tanto, podemos calcular el flujo máximo y determinar la cantidad de espias a eliminar utilizando este numero. Los espias a eliminar serían aquellos que se encuentren en el corte mínimo que atraviesen los artilugios creados.

El pseudocódigo es:
```
def minCantidadDeEspias(grafo, agencia, destino):

    grafoAux = transformarAProblemaAristaDisjunto(grafo)
    
    cantidadMaximaDeMensajes = MaximizeFlow(grafoAux, agencia, destino)
    mensajesPosibles = cantidadMaximaDeMensajes
    agentesEliminados = {}
    
    agentesAEliminar = ceil(mensajesPosibles * 0.3)
    
    corteMinimo = obtenerCorteMinimo(grafoAux)
    eliminados = 0
    
    for arista in corteMinimo:
        agente = obtenerAgenteAEliminar(arista)
        agentesEliminados += {agente}
        eliminados += 1
        
        if(eliminados == agentesAEliminar)
          break
          
    return agentesAEliminar, agentesEliminados
   
```   

La complejidad espacial del algoritmo es O(nxn) para almacenar el grafo auxiliar creado.

La complejidad temporal es la complejidad de calcular el flujo máximo: `O(|V|*|E|^2)`

### Paso a Paso

En esta imagen, podemos observar un grafo al que ya se le aplico la modificación para adaptarlo a nuestro problema. Podemos observar cuales son los "caminos" por los cuales el mensaje se transmite. La linea punteada en negro es el corte mínimo que atraviesa las aristas artilugio que creamos previamente. En este caso, el flujo máximo posible es 2, por lo que la cantidad de mensajes a eliminar es ceil(2 * 0,3) = 1. Al remover cualquier arista del corte mínimo, podemos observar que el flujo máximo posible se reduce en la capacidad de la arista que removemos. Como esta arista tiene capacidad 1, al remover esta arista estamos eliminando en 1 la cantidad de mensajes posibles que podemos enviar. En este caso, solo debemos eliminar una sola arista. 

<br><div align="center"><img src="media/xd.png" style="max-width: 50%;"></div><br>

Ahora observemos la siguiente imagen en la cual efectivamente removemos la arista perteneciente al corte mínimo. 
<br><div align="center"><img src="media/xd2.png" style="max-width: 50%;"></div><br>

Como podemos observar, la cantidad maxima posible de mensajes ahora es 1, ya que el flujo maximo se redujo en exactamente la capacidad de la arista que sacamos previamente. 

