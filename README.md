# Información

Este es un ejercicio realizado para la asignatura de **metodología de la programación** de la **Universidad Internacional de Valencia**.

Los requisitos del ejercício pueden encontrarse en la carpeta doc. Cada unidad competencial tiene sus propios requisitos y su rubrica.

## Módulo Logging

Me hubiera gustado tener mejor control de la salida del programa.

- Permitir la configuración del nivel de verbosidad.
- Enviar la salida a un fichero de log.

Para ello estube echando un vistazo a la librería [login](https://docs.python.org/3/library/logging.html)

Ante la falta de tiempo disponible, tube que utilizar la la función `print`, pero incrementé el nivel de verbosidad,
tal y cómo me indicó el profesor.

## Módulo de lectura y escritura

Los datos se leeran y escribirán en el directorio `src/data`. Los requisitos indicaban que deberían guardarse en la 
misma carpeta que el fichero, pero se ha optado por utilizar un directorio por ser más ordenado.

Los datos se guadarán en formato json. Los requisitos indicaban que debería utilizarse el formato csv, pero json es un 
formato más sencillo de leer y de escribir, por lo que se ha optado por el para la realización del ejercicio.

Algunos datos no son guardados como es la lista de orquideas vendidas y destruidas, ya que queda fuera del alcance del
ejercício.