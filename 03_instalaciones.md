# Instalaciones de programas

Ya que hemos estado hablando de varias cosas sobre programación, ahora es necesario que veamos las cosas que hay que instalar y configurar.

No solo me refiero a instalar Python, que es lo más obvio no?, sino que otras aplicaciones que son de real utilidad para cualquiera que desee empezar en la programación y ser más eficiente.

Acá me voy a referir al uso de Windows como sistema operativo, que es lo que tengo. Las instalaciones en Linux y OSX (Apple) tienen sus particularidades, pero que no conozco en detalle.


## Instalando Python

Para instalar Python, hay que ir a su web oficial https://www.python.org/ 

En la portada de la web, hay que ir a la sección **Downloads**. Se mostrará una serie de links para descargarlo, pero elige la que te pone por defecto (la que aparece en el rectángulo amarillo), que es la última versión disponibe para el sistema operativo desde dond estás ingresando.

<img src="img/download_python.png" alt="Python" title="Descargando Python" />

En el wizard de instalación hay que tener ojo con un par de cosas:

- Marcar la opción de agregar Pyhton al PATH
- Elegir la opción de instalación CUSTOM
- La ruta donde lo instales cámbiala. Es mejor poner una carpeta directamente en la raíz (en mi caso es disco local "C").
Esta es la que me sale por defecto C:\Users\pvill\AppData\Local\Programs\Python\Python310
Es mejor poner esta C:\Python310

<img src="img/install_python1.png" alt="Python" title="Descargando Python" />

- En la pantalla donde pide seleccionar instalar documentation, IDLE, pip y todas esas cosas...

<img src="img/install_python2.png" alt="Python" title="Descargando Python" />

<img src="img/install_python3.png" alt="Python" title="Descargando Python" />

Después las otras cosas que salen dejarlas por defecto, darle a SI a los permisos de administrador y darle a siguiente e instalar.

Luego que se termine todo el proceso, ya deberías tener Python instalado en tu computador.


### ¿Cómo saber si ya tengo Python instalado correctamente?

Para saber eso, necesitamos usar la consola de Windows o PowerShell. También se llama "Símbolo del sistema". Igula luego instalaemos una versión más linda y funcional de esta consola. por ahora usa la que tienen nada más. En Windows 11 ya viene instaado por defecto PowerShell, en las versiones anteriores no viene y está la versión más clásica el terminal. 

Escribe en el buscador de programas cmd o símbolo de sistema o terminal o PowerShell. Igual cualquiera sirve por ahora.

Para saber si ya está funcional Pyhton, hay que escribir en la consola "python" (sin las comillas). Si muestra la versión de Python, está todo bien.

<img src="img/terminal_install.png" alt="Python" title="Instalando Python" />

Felicitaciones!!!! 🥳

Ya tenemos instalado Python.

Además, fíjate que en la consola aparacen >>> al inicio. Esto indica que estamos dentro de Python y que podemos usarlo desde la misma consola.
Podríamos sumar 3 + 3 y obtener el resultado en la misma consola.
```
>>> 3+3
6
>>>
```

Podríamos imprimir en pantalla el clásico Hola Mundo:
```
>>> print("Hola Mundo")
Hola Mundo
>>>
```

Usar Python desde la consola no es muy buena idea, es poco funcional, no es muy estético y cuesta usarla si nos estás acostumbrado/a a ella.
Para eso, es mejor usar un programa especialmente hecho para escribir código, que es un editor de texto o IDE. 

Actualmente uso Visual Studio Code, que es de Microsoft y es uno, sino el más, famoso y usado actualmente para programación. 


## Instalando Visual Studio Code

Para instalarlo, hay que ir a su web oficial https://code.visualstudio.com/

<img src="img/install_vsc.png" alt="Python" title="Instalando Visual Studio Code" />

Por defecto, cuando cargas la página, te muestra la versión más reciente de VSC y la que corresponde a tu sistema operativo.
Puedes elegir otras versiones, pero no es recomendable. Es mejor dejar la que sale nada más.

Instalarlo es como cualquier programa, solo darle a siguiente muchas veces y esperar un poco.

Una vez ya instalado nuestro IDE (Visual Studio Code), hay que hacer algunas configuraciones pequeñas. Bueno, VSC es muy configurable, tiene cientos de opciones la verdad, pero veremos las más básicas para empezar a programar en Pyhton.


### Configurando VSC

Una de las cosas más interesantes de Visual Studio Code es el uso de las extensiones. Las extensiones son como pequeñas aplicaciones que agregan funcionalidades a VSC. 

Para buscar las extensiones, hay 2 formas:
- Desde la web del marketplace
- Desde la misma aplicación de VSC

Por ahora vamos a usar la versión web. 
Ir a https://marketplace.visualstudio.com/VSCode 

Buscar la extensión de pyhton:

<img src="img/extension_python1.png" alt="Python" title="Instalando extension Python VSC" />

Van a salir muchas extensiones, pero la extensión que recomiendo es la de Microsoft, que es la que sale primero habitualmente.

<img src="img/extension_python2.png" alt="Python" title="Instalando extension Python VSC" />

Darle clic a esa extensión e instalarla. 
Te va a pedir algunos permisos para abrir el VSC. Dale permitir.

<img src="img/extension_python3.png" alt="Python" title="Instalando extension Python VSC" />

Luego de unos segundos, ya debería estar instalado.
Te debería salir una pantalla similar a esta en el Visual Studio Code:

<img src="img/extension_python4.png" alt="Python" title="Instalando extension Python VSC" />

Con eso, ya debería estar todo ok!!