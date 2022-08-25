# Comentarios

Este tema de los comentarios en el código (o comentar el código) pareciera ser algo poco relevante, pero no lo es. Decidí dedicar un capítulo específico a este tema, pues es algo se usa mucho, pero no siempre de buena forma y puede generar varios problemas si no se realiza de forma ordenada. 

Quizá en algún momento será necesario poner algunas palabras en el código dirigidas no a Python, sino a las personas quienes estén leyendo el código con el fin de explicarles como es que funciona, también para documentar quien es el autor del programa y en que fecha fue escrito o entregar alguna información relevante. 

También, los comentarios puedes ser útiles para ti mismo, pero más adelante en el tiempo. Es frecuente que uno tenga que retomar un código después de un tiempo y no recuerde bien qué ni cómo lo hizo. Para eso casos, los comentarios son útiles. Pero debes tener em nete los mismos criterios que vamos a ver en este capítulo.



Un texto insertado en el programa el cual es, **omitido en la ejecución**, es denominado un comentario.

Pero ojo, y en especial si estás aprendiendo a programar, es código que escibas debe hablar por sí mismo. Eso significa que debe ser los más autoexplicativo posible. Ya vimos en unos capítulos anteriores la importancia del nombre de las variables y de que éstos sean significativos. 

Los comentarios no deberían explicar lo que hace el código (el qué), sino más bien el porqué se hace algo. Eso, solo si es necesario, pues como ya vimos, el uso de comentarios debe ser juicioso y acotado.

Además, aunque suene extraño, le debes dar mantención a tus comentarios, además de a tu código. Con mantención me refiero a solucionar errores (bugs), ajustar variables o nuevas lógicas, agregar o sacar funcionalidades, etc. Todo eso puede llegar a ser costoso, lento y aburrido, en especial en soluciones grandes o con muchos participantes. Si además de eso hay que estar ajustando todos los comentarios que hay repartidos en el código, se hace una tarea más compleja y factible de error o de generar confusión a la hora de interpretarlo.

Entonces, lo más simple es tratar de no usar comentarios, excepto que sean muy necesario y entregue información relevante del código, no explicar explícitamente lo que hace, sino para dar contexto.


## ¿Cómo se colocan los comentarios?

Tiene que ser hecho de cierta manera para que Python no intente interpretarlo como parte del código.

Cuando Python se encuentra con un comentario en el programa, el comentario es completamente transparente, desde el punto de vista de Python, el comentario es solo un espacio vacío, sin importar que tan largo sea.

En Python, un comentario es un texto que comienza con el símbolo # y se extiende hasta el final de la línea. Si se desea colocar un comentario que abarca varias líneas, se debe colocar este símbolo en cada línea.

```
# Esta programa calcula la hipotenusa (c)
# a y b son las longitudes de los catetos
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5 
print("c =", c)
```

Otra instancia de usar un comentario es para separar parte del código para que sea más legible. Como si fuesen capítulos de un libro. Esto puede ser útil en muchos casos, pero tener códigos de muchas líneas (> 200 ó 300) tiende a no ser una buena idea. Dificulta la legibilidad y es más complejo de mantener. Ademas, es muy posible que el código contenga muchas funciones y realice muchas cosas a la vez, y quizás sea necesario separarlo en trozos más pequeños independientes o de repensar las funciones. Pero es un tema más avanzado que veremos más adelante. Por ahora, no importa mucho, pero tenlo en mente.

Una situación que veo con frecuencia y que yo uso también, es la de comentar una línea para evitar un output en especial y dejar que otros sí se ejecuten. Esto se puede ver mucho cuando se están probando cosas en el código y aún se están agregando y sacando cosas para evaluar sus resultados. Es común en esos casos. Pero esta práctica podría generar que se nos pase una línea comentada (que no debería estar comentada) y que se ejecute el programa y no arroje el resultado esperado. Esto provocará tiempo de búsqueda de la falla y solución, además, que pudiera ser que no haya ningún error el código como tal, sino que no resulta como uno quiere. Por lo que la práctica de comentar y descomentar outputs solo son para pruebas en ambientes controlados y en espacios pequeños del código para evitar que pasen a producción (esto es que el programa sea usado por el usuario final) sin darse cuenta.

En este ejemplo, si se descomenta la línea *# y = y + x*, el resultado del print es totalmente distinto. Prúebalo en tu consola.

```
# Este es un programa de prueba.
x = 1
y = 2
# y = y + x
print(x + y)
```

[**<< CAPITULO ANTERIOR**](https://github.com/paulovillarroel/aprendiendo_python/blob/main/07_operadores/07_operadores.md) | [**SIGUIENTE CAPITULO >>**](https://github.com/paulovillarroel/aprendiendo_python/blob/main/09_strings/09_strings.md)