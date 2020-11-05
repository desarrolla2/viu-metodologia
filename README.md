# Introducción

Este es un ejercicio realizado para la asignatura de **metodología de la programación** de la **Universidad Internacional de Valencia**.

Los requisitos del ejercício pueden encontrarse en la carpeta doc. Cada unidad competencial tiene sus propios requisitos y su rubrica.

Para esta versión del programa he decidido utilizar el framework de desarrollo web [django](https://www.djangoproject.com/)

# Instalación y ejecución del programa

Para ejecutar este programa es necesario seguir las siguientes instrucciones. Estas instrucciones están pensadas para ser
ejecutadas en un sistema Linux, concretamente en un ubuntu 18.04.

El sistema debe tener instalado python3 para la ejecución del entorno y pip3 para la instalación de dependencias. 
También será necesario disponer de una base de datos mysql.

Lo primero es entrar en el virtual env donde tenemos disponible algunas librerías necesarias, para ello desde la raiz del
proyecto ejecutamos:

```bash 
source env/bin/activate
```

Luego debemos configurar la base de datos, para ello editaremos el fichero `project/settings.py`' en la sección de databases

```bash 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'orchids',
        'USER': 'orchids',
        'PASSWORD': 'HFatmTWMvc6D0xUV;&',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Debes indicar los datos de conexión a tu base de datos.

**Nota**: *Normalmente es una mala practica publicar passwords o incluirlas en el repositorio tal y como yo he hecho aquí, pero al ser
simplemente una practica he decidido hacerlos así por comodidad*

El siguiente paso es generar la base de datos, para ello debemos ejecutar

```bash
python3 manage.py migrate
```

Ya tenemos todo listo, ahora sólo necesitamos levantar el servidor de pruebas, con el siguiente comando

```bash
python3 manage.py runserver
```

Abre un navegador y entra a [orchid manager](http://localhost:8000/)

# Explicación funcional

He realizado una explicación funcional en estos videos.

- [Explicación funcional 1](https://www.youtube.com/watch?v=SSYgWzbgX-s&feature=youtu.be)
- [Explicación funcional 2](https://www.youtube.com/watch?v=mFdcs0_jQCY&feature=youtu.be)

# Explicación técnica

He realizado una breve explicación técnica en este video.

- [Explicación técnica](https://www.youtube.com/watch?v=6cqpwb8Vh0I&feature=youtu.be)



