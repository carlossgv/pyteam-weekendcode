# pyteam-weekendcode
Proyecto de Pyteam para WeekendCode de Recorders - Categoría Mr. Robot.

Quien no se ha topado con estas preguntas relacionadas al covid ¿En qué fase estoy?, ¿Puedo salir?, si voy a esta comuna, ¿necesito algún papel? ¿Cuáles son las farmacias más cercanas abiertas?
Bueno nosotros responderemos a esa interrogante, y es que todo proyecto o solución se basa en un problema y nosotros también lo tuvimos, y decidimos solucionarlo en una sola plataforma que contenga toda la información respecto al covid, y que permita al usuario obtenerla lo más simple posible.
Somos Py Team!

## Funcionamiento 👇

El proyecto tiene solo 1 página principal, la cual te entregará información de las farmacias de turno cercanas, el clima y la fase según tu ubicación, para ello debes o permitir la geolocalización o ingresar la dirección de tu interés.

![Pagina Help-Covid](/Readme_images/Help-Covid_1.png)

Luego de que se ha ingresado la dirección el resultado que deberías obtener sería algo como la siguiente imagen

![Pagina Help-Covid](/Readme_images/Help-Covid_2.png)


### Requisitos 📋

Para este proyecto se uso principalmente **Django 3.1.3**, **geopy 2.1.0**, **Bootstrap v5.0.0-beta1** y **Python 3.8.5**.
Los requisitos para este proyecto los puedes encontrar en el archivo:

- requirements.txt

Adicionalmente también necesitaras credenciales para consumir las APIs del clima y de google maps:

* [API Clima](https://www.weatherbit.io/) - API Clima
* [API Google Maps](https://developers.google.com/maps/documentation/javascript/overview) - API Google Maps

Puedes configurar un entorno virtual usando **Conda**. A continuación se muestra un ejemplo de cómo puedes configurar uno de nombre **covid** para **Python 3.8**

```
conda create --name covid python=3.8
```

Una vez ya creado el entorno debes ingresar en él, lo cual se haría de la siguiente manera 

```
conda activate covid
```

Entonces ya dentro del entorno virtual instalas los requerimientos

```
pip install -r requirements.txt
```

Con esto deberías tener lista la configuración inicial

### Instalación 🔧

Una vez ya tienes todos los requisitos ya deberías poder probar el proyecto haciendo un

```
python manage.py runserver
```

## Construido con 🛠️

* [Django](https://www.djangoproject.com) - Framework web
* [Bootstrap](https://getbootstrap.com) -  Framework Front-end

## Autores✒️

* **Carlos Gonzales** - *Colaborador* - [carlossgv](https://github.com/carlossgv)
* **Eduardo A. Barrios** - *Colaborador* - [GTXs4](https://github.com/gtxs4)
* **Erick Henriquez R.** - *Colaborador* - [ErickHenriquez](https://github.com/ErickHenriquez)
