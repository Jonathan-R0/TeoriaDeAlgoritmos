1) Primero vamos a demostrar lo pedido con un contraejemplo. La solución propuesta por la administración no es óptima, pues siguiendo el algorítmo introducido podriamos llegar a la siguiente situación:

Si tenemos la siguiente distribución de contratos:

- Contrato A: Lunes 9am hasta la 1pm (duración 4 hs)
- Contrato B: Lunes 2pm hasta las 6pm (duración 4 hs)
- Contrato C: Lunes 7am hasta las 5pm (duración 10 hs)
- Contrato D: Lunes 5pm hasta las 10pm (duración 5 hs)

El algorítmo tomaría primero el contrato A pues es el que dura menos. Eso hace que quiera luego tomar el contrato B por sobre el contrato C (pues este ya arrancó antes) y el D (pues este dura más que el B) y finalizará ya que no posee más contratos para adquirir.

Esta aplicación del algoritmo resulta no devolver la solución óptima pues 

```
+---------------------------------------------------------------+
             |     Lunes     | |     Lunes     |            
             |   9am hasta   | |   2pm hasta   |  
             |    la  1pm    | |    las 6pm    |
+---------------------------------------------------------------+
        |          Lunes          |       Lunes      |
        |        7am hasta        |    5pm  hasta    |  
        |         las 5pm         |     las 10pm     |
+---------------------------------------------------------------+
```

