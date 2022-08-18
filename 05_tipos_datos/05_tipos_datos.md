# Tipos de datos

Una de las cosas fundamentales y que debemos entender, son los tipos de datos que se pueden usar con Python. Eso es muy relevante para analizar el diseño de los programas que generemos y qúe y cómo vamos a usar los datos.

Los tipos de datos son bastante diversos, pero podemos agruparlos en:

- Numéricos
- Secuencias
- Mapas
- Clases
- Instancias
- Excepciones


Vamos a ir por partes, pues este tema es extenso y no tan simple en algunos casos. Pero es significativo el comprenderlos y saber cómo administrarlos, úes eso puede determinar mucho el buen desempeño de nustro código y soluciones.

De todas formas, en la [documentación oficial de Python](https://docs.python.org/es/3/library/stdtypes.html) hacen un análisis bastante detallado de los tipos de datos. Si quieres profundizar más, te aconsejo darle una lectura después de leer y estudiar este artículo.

Al final, el intérprete lo que hace es traducir el código de alto nivel que escribimos a código computador, que son básicamente puros 0 y 1 ordenados de tal forma que el computador los pueda entender. 

Puedes entender un poco mejor del código binario (esos unos y ceros) en el siguiente video:

[![Código binario](http://img.youtube.com/vi/f9b0wwhTmeU/hqdefault.jpg)](https://youtu.be/f9b0wwhTmeU)


## Datos numéricos

Acá encontramos:
- int (integer o enteros)
- float (coma flotante o decimales)
- complex (complejos)

Es importante entender la diferencia entre enteros y decimales, más allá de lo evidente, que es tener o no la separación de decimales. Para efectos prácticos, en Python (y para muchos lenguajes de programación, a verdad) la separación entre la parte entera y la decimal es con un punto (.) y con una coma (,). Esto que parece algo vanal, en realidad es super importante tenerlo en mente, pues muchos datasets (cunjuntos de datos) vienen con una coma como separador, y en latinomamérica es más común usar la coma que el punto. Esto  de usar puntos en vez de comas puede generar problemas a la hora de interpretar los datos. 

No solo eso, sino que desde el punto de vista del uso de la memoria del computador, almacenar un número entero es muy distinto a almacenar uno decimal. El computador hace un proceso muy distinto para guardar uno u otro dato. Suena loco, pero es así. Los almacena de forma distinta y ocupan un espacio de memora distinto. 

2 no es lo mismo que 2.0 para efecto del uso de los recursos computacionales. En poca cantidad, eso no debería importarte mucho, pero cuando el volumen es alto, esta diferencia puede ser muy relevante para no sobrepasar las capacidades de memoria. 

Pero una pregunta básica y que parece obvia, pero que no lo es tanto, es saber qué son los números.

[![¿Qué son los números?](http://img.youtube.com/vi/H9pMUV4leQg/hqdefault.jpg)](https://youtu.be/H9pMUV4leQg)

Los numero complejos son aquellos que tienen una parte real y otra imaginaria (viste el video, no?)

Ok, ya con esas definiciones en la cabeza, sigamos...

Los números se crean a partir de una expresión literal (o sea, que lo escribes directamente en el editor de texto), o como resultado de una combinación de funciones predefinidas y operadores. Expresiones literales de números (incluyendo números expresados en hexadecimal, octal o binario) producen enteros. Si la expresión literal contiene un punto decimal o un signo de exponente, se genera un número en coma flotante. Si se añade como sufijo una 'j' o una 'J' a un literal numérico, se genera un número imaginario puro (Un número complejo con la parte real a cero), que se puede sumar a un número entero o de coma flotante para obtener un número complejo con parte real e imaginaria.

Python 3.6 ha introducido el guion bajo en los literales numéricos, permitiendo colocar un guion bajo entre dígitos y después de especificadores de base para mejorar la legibilidad. Esta característica no está disponible en versiones anteriores de Python.

```
>>> 11_22
1122
>>>
```

¿Cómo se codifican los números negativos en Python? Como normalmente se hace, agregando un signo de menos. Se puede escribir: -11111111, o -11_111_111.

Los números positivos no requieren un signo positivo antepuesto, pero es permitido, si se desea hacer. Las siguientes líneas describen el mismo número: +11111111 y 11111111.


### Enteros: números octales y hexadecimales

Existen dos convenciones adicionales en Python que no son conocidas en el mundo de las matemáticas. El primero nos permite utilizar un número en su representación octal.

Si un número entero esta precedido por un código 0O o 0o (cero-o), el número será tratado como un valor octal. Esto significa que el número debe contener dígitos en el rango del [0..7] únicamente.

0o123 es un número octal con un valor (decimal) igual a 83.

La función print() realiza la conversión automáticamente. Intenta esto en la consola:

```
>>> print(0o123)
83
```

La segunda convención nos permite utilizar números en hexadecimal. Dichos números deben ser precedidos por el prefijo 0x o 0X (cero-x).

0x123 es un número hexadecimal con un valor (decimal) igual a 291. La función print() puede manejar estos valores también. Intenta esto:

```
>>> print(0x123)
291
```

Esta diferenciación también tiene como objetivo el optimizar el uso de la memoria para almacenar datos. Sé que no lo parece, pero es relevante tener estos conceptos en mente. 


### Operaciones

Con los números (excepto con los complejos) puedes realizar las siguientes operaciones matemáticas:

<img src="../img/numeric_operations.png" alt="Python" title="Operaciones con números" />

Notas:

1. También conocida como división entera. El resultado es un número entero en el sentido matemático, pero no necesariamente de tipo entero. El resultado se redondea de forma automática hacia menos infinito: 1//2 es 0, (-1)//2 es -1, 1//(-2) es -1 y (-1)//(-2) es 0.

2. No es apropiada para números complejos. Es preferible convertir a valores en coma flotante usando la función abs() si fuera apropiado.

3. Conversiones desde coma flotante a entero pueden redondearse o truncarse como en C; véanse las funciones math.floor() y math.ceil() para un mayor control.

4. float también acepta las cadenas de caracteres «nan» e «inf», con un prefijo opcional «+» o «-», para los valores Not a Number (NaN) e infinito positivo o negativo.

5. Python define pow(0, 0) y 0 ** 0 para que valgan 1, como es práctica habitual en los lenguajes de programación.

6. Los literales numéricos aceptables incluyen los dígitos desde el 0 hasta el 9, así como cualquier carácter Unicode equivalente (puntos de código con la propiedad Nd).


No olvides, al igual que con los cálculos matemáticos, hay prioridades de operación. Como la clásica regla que las multiplizaciones y divisiones de hacen antes que los las sumas y restas. Te recuedas del colegio? Bueno, en Python también hay prioridades de ejecución. Son hartas y hemos visto solo algunas hasta hora, pero en la [documentación oficial puedes tener más información](https://docs.python.org/es/3/reference/expressions.html#operator-summary).


Algunas consideraciones importantes al realizar operaciones con los números...

Una divisíon (/) siempre dará como resultado un número flotante.

```
>>> 3/5
0.6
```

Como puedes imaginar, el valor de cero punto cuatro puede ser escrito en Python como:

```
>>> 0.4
```

Pero no hay que olvidar esta sencilla regla, se puede omitir el cero cuando es el único dígito antes del punto decimal. En esencia, el valor 0.4 se puede escribir como:

```
>>> .4
```

Veamos algo nuevo, ya lo profundizaremos, pero es una de las grandes cosas de Python (y de otros lenguajes orientados a objetos), es que puedes crear **variables**. Esto es la bomba!!! 😱

Mira el siguiente ejemplo:

<img src="../img/variables.png" alt="Python" title="Asignando variables" />

Acá se crean 2 variables (x, y) y a cada una se le asigna un valor (5 y 4.7 respectivamente). Luesgo realizamos una suma simple. Observa que el intérprete entiende que como se han definido esos valores previamente, los puede usar para el cálculo. Mira lo que pasa cuando no definimos una variable antes de la operación en donde se hace referencia.

<img src="../img/variable2.png" alt="Python" title="Asignando variables" />

Pues arroja un error: name 'y' is not defined.

Bueno, ya sabes porqué pasó eso.


Por ahora lo voy a dejar hasta acá... Pronto actualizaré este documento, ya que nos quedan muchos tipos de datos y apenas llevamos un par.

