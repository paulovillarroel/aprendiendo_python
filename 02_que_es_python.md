# ¿Qué es Python?

Python es un lenguaje de programación de propósito general, de alto nivel, orientado a objetos e interpretado. 

Epa!!!
Vamos por parte...


## Lenguaje de programación

Un lenguaje es un medio (y una herramienta) para expresar y registrar pensamientos. Hay muchos lenguajes a nuestro alrededor. Algunos de ellos no requieren hablar ni escribir, como el lenguaje corporal. Es posible expresar tus sentimientos más profundos de manera muy precisa sin decir una sola palabra.

Otro lenguaje que se emplea cada día es la lengua materna, que utilizas para manifestar tu voluntad y para pensar en la realidad. Las computadoras también tienen su propio lenguaje, llamado lenguaje máquina, el cual es muy rudimentario.
Los comandos que reconoce son muy simples. Podemos imaginar que la computadora responde a órdenes como "Toma este número, divídelo entre otro y guarda el resultado".

Un conjunto completo de comandos conocidos se llama **lista de instrucciones**, a veces abreviada IL (por sus siglas en inglés). Los diferentes tipos de computadoras pueden variar según el tamaño de sus IL y las instrucciones pueden ser completamente diferentes en diferentes modelos.


Podemos decir que cada lenguaje (máquina o natural, no importa) consta de los siguientes elementos:

- Un alfabeto: un conjunto de símbolos utilizados para formar palabras de un determinado lenguaje (por ejemplo, el alfabeto latino para el inglés, el alfabeto cirílico para el ruso, el kanji para el japonés, y así sucesivamente).
- Un léxico: (también conocido como diccionario) un conjunto de palabras que el lenguaje ofrece a sus usuarios (por ejemplo, la palabra "computadora" proviene del diccionario en inglés, mientras que "cmoptrue" no; la palabra "chat" está presente en los diccionarios de inglés y francés, pero sus significados son diferentes.
- Una sintaxis: un conjunto de reglas (formales o informales, escritas o interpretadas intuitivamente) utilizadas para precisar si una determinada cadena de palabras forma una oración válida (por ejemplo, "Soy una serpiente" es una frase sintácticamente correcta, mientras que "Yo serpiente soy una" no lo es).
- Una semántica: un conjunto de reglas que determinan si una frase tiene sentido (por ejemplo, "Me comí una dona" tiene sentido, pero "Una dona me comió" no lo tiene).

La IL es, de hecho, el alfabeto de un lenguaje máquina. Este es el conjunto de símbolos más simple y principal que podemos usar para dar comandos a una computadora. Es la lengua materna de la computadora.


## Interpretado

La programación de computadora es el acto de establecer una secuencia de instrucciones con la cual se causará el efecto deseado. El efecto podría ser diferente en cada caso específico: depende de la imaginación, el conocimiento y la experiencia del programador.

Por supuesto, tal composición tiene que ser correcta en muchos sentidos, tales como vimos más arriba.
Desafortunadamente, un programador también puede cometer errores en cada uno de los cuatro sentidos anteriores. Cada uno de ellos puede hacer que el programa se vuelva completamente inútil.

Supongamos que has escrito correctamente un programa. ¿Cómo persuadimos a la computadora para que lo ejecute? Tienes que convertir tu programa en lenguaje máquina. Afortunadamente, la traducción puede ser realizada por la computadora, haciendo que todo el proceso sea rápido y eficiente.

Existen dos formas diferentes de transformar un programa de un lenguaje de programación de alto nivel a un lenguaje de máquina:

- COMPILACIÓN: el programa fuente se traduce una vez (sin embargo, esta ley debe repetirse cada vez que se modifique el código fuente) obteniendo un archivo (por ejemplo, un archivo .exe si el código está diseñado para ejecutarse en MS Windows) que contiene el código máquina; ahora puedes distribuir el archivo en todo el mundo; el programa que realiza esta traducción se llama compilador o traductor.

- INTERPRETACIÓN: Tú (o cualquier usuario del código) puedes traducir el programa fuente cada vez que se ejecute; el programa que realiza este tipo de transformación se denomina intérprete, ya que interpreta el código cada vez que está destinado a ejecutarse; también significa que no puede distribuir el código fuente tal como está, porque el usuario final también necesita que el intérprete lo ejecute.

Debido a algunas razones muy fundamentales, un lenguaje de programación de alto nivel en particular está diseñado para caer en una de estas dos categorías. Existen muy pocos idiomas que se pueden ser tanto compilados como interpretados. Por lo general, un lenguaje de programación se proyecta con este factor en la mente de sus constructores: ¿Se compilará o interpretará?

El intérprete lee el código fuente de una manera que es común en la cultura occidental: de arriba hacía abajo y de izquierda a derecha. Hay algunas excepciones, que se verán más adelante.
En primer lugar, el intérprete verifica si todas las líneas subsiguientes son correctas (utilizando los cuatro aspectos tratados anteriormente).
Si el intérprete encuentra un error, termina su trabajo inmediatamente. El único resultado en este caso es un mensaje de error.
No siempre es fácil resolver qué está causando un error. Se necesita práctica para ir resolviédolos y una capacidad muy importante, para cualquier programador, que es la de saber buscar en internet el error (posiblemente te suene Stack Overflow).


En resumen, podemos decir que sea interpretado tiene como ventajas y desventajas:

**Ventajas:**
- Se puedes ejecutar el código en cuanto se completa; no hay fases adicionales de traducción.
- El código se almacena utilizando el lenguaje de programación, no el de la máquina; esto significa que puede ejecutarse en computadoras que utilizan diferentes lenguajes máquina; no se compila el código por separado para cada arquitectura diferente.

**Desventajas**
- La interpretación incremente es más lento (frente al compilado): el código compartirá la potencia de la computadora con el intérprete, por lo que no puede ser realmente rápido.
- Tanto tú como el usuario final deben tener el intérprete para ejecutar el código.


## Alto nivel

Según Wikipedia, un lenguaje de programación de alto nivel se caracteriza por expresar los algoritmos de una manera adecuada a la capacidad cognitiva humana, en lugar de la capacidad con que los ejecutan las máquinas. Estos lenguajes permiten una máxima flexibilidad al programador a la hora de abstraerse o de ser literal. Permiten un camino bidireccional entre el lenguaje máquina y una expresión casi oral entre la escritura del programa y su posterior compilación. 

Es decir, está pensado para ser entendido por las personas.


## Propósito general

Esto  es básicamente que se puede usar para varios propósitos.

Algunos ejemplos en donde se ha usado Python (en mayor o menor medida) son:

- Dropbox, UBER, Spotify o Pintrest.
- Aplicaciones de Internet (BitTorrent, Jogger Publishing Assistant, TheCircle, TwistedMatrix)
- 3D CAD/CAM (FreeCAD, Fandango, Blender, Vintech RCAM)
- Aplicaciones Empresariales (Odoo, Tryton, Picalo, LinOTP 2, RESTx)
- Aplicaciones de Imagen (Gnofract 4D, Gogh, imgSeek, MayaVi, VPython)
- Aplicaciones Móviles (Aarlogic C05/3, AppBackup, Pyroute)
- Aplicaciones de Oficina (calibre, faces, Notalon, pyspread)
- Administradores de Información Personal (BitPim, Narval, Prioritise, Task Coach, WikidPad)

(Fuente: https://wiki.python.org/moin/PythonProjects)

Pyhton puede ser utilizado en:

- Desarrollo Web (como los frameworks Django y Pyramid, micro-frameworks Flask y Bottle)
- Computación científica y numérica (por ejemplo, SciPy, una colección de paquetes con fines matemáticos, científicos y de ingeniería; Ipython, un shell interactivo que permite la edición y grabación de sesiones de trabajo)
- Educación 
- GUIs de Escritorio (por ejemplo, wxWidgets, Kivy, Qt)
- Desarrollo de software (control de compilación, gestión y pruebas: Scons, Buildbot, Apache Gump, Roundup, Trac)
- Aplicaciones empresariales (ERP y sistemas de comercio electrónico: Odoo, Tryton)

(Fuente: https://www.python.org/about/apps)


A pesar de que se puede usar un muchas áreas, para aplicaciones móviles Python esta lejos de ser una buena idea. A día de hoy, nadie pensaría en crear una app con Pyhton. Hay alternativas mucho mejores.


## Orientado a objetos

Este es un tema relevante y muy importante, pero no es muy fácil de asimilar en primera instancia. Y tampoco de explicar en pocas palabras.
Para mejor entendimiento, es mejor ver estos 2 breves videos. De seguro, más adelante en el estudio se haga más fácil entender estos conceptos.

[![POO BettaTech](http://img.youtube.com/vi/tTPeP5dVuA4/hqdefault.jpg)](https://youtu.be/tTPeP5dVuA4)

[![POO Platzi](http://img.youtube.com/vi/Mi_sRAfs7TE/hqdefault.jpg)](https://youtu.be/Mi_sRAfs7TE)


## Volvamos a Python

El nombre del lenguaje de programación Python proviene de una antigua serie de comedia de la BBC llamada Monty Python's Flying Circus.

Una de las características sorprendentes de Python es el hecho de que en realidad es el trabajo de una persona. Fue creado por Guido van Rossum, nacido en 1956 en Haarlem, Países Bajos.

En 1999, Guido van Rossum definió sus objetivos para Python:

- Un lenguaje fácil e intuitivo tan poderoso como los de los principales competidores.
- De código abierto, para que cualquiera pueda contribuir a su desarrollo.
- El código que es tan comprensible como el inglés simple.
- Adecuado para tareas cotidianas, permitiendo tiempos de desarrollo cortos.


Python es muy popular y, actualmente (al momento de crear este documento al menos), es el lenguaje de programación más usado en el mundo. Puedes ver el top ten de [PYPL PopularitY of Programming Language](https://pypl.github.io/PYPL.html) y el [TIOBE Programming Community Index](https://www.tiobe.com/tiobe-index/).


Aunque suene extraño, existen dos tipos principales de Python, llamados Python 2 y Python 3.

El desarrollo de Python 2 se ha estancado intencionalmente, aunque eso no significa que no haya actualizaciones. Por el contrario, las actualizaciones se emiten de forma regular, pero no pretenden modificar el idioma de manera significativa. Prefieren arreglar cualquier error recién descubierto y agujeros de seguridad. La ruta de desarrollo de Python 2 ya ha llegado a un callejón sin salida, pero Python 2 en sí todavía está muy vivo.

Python 3 es la versión más nueva y actual del lenguaje.

Estas dos versiones de Python no son compatibles entre sí. Las secuencias de comandos de Python 2 no se ejecutarán en un entorno de Python 3 y viceversa, por lo que si deseas que un intérprete de Python 3 ejecute el código Python 2 anterior, la única solución posible es volver a escribirlo o revisarlo qué partes se pueder reutilizar. Pero el migrar del 2 al 3 es demasiado difícil, consume mucho tiempo, es demasiado caro y es demasiado arriesgado migrar una aplicación Python 2 antigua a una nueva plataforma.


En defiinitiva, si estamos partiendo a estudiar y aprender Python, la mejor opción es hacerlo con la versión 3. Y es la que usaré.
