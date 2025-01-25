# Impresora 2D en Python

[![PyPI](https://img.shields.io/pypi/v/markitdown.svg)](https://pypi.org/project/markitdown/)
![PyPI - Downloads](https://img.shields.io/pypi/dd/markitdown)
[![Built by AutoGen Team](https://img.shields.io/badge/Built%20by-AutoGen%20Team-blue)](https://github.com/microsoft/autogen)


Este proyecto es una impresora 2D escrita en Python que permite crear patrones y dibujos básicos en una cuadrícula utilizando coordenadas cartesianas.

## Características

Dibujo de figuras geométricas simples (líneas, cuadrados, círculos).

Guardado e impresión de patrones en formato de texto o imagen.

Interfaz de línea de comandos para dibujar figuras mediante comandos sencillos.

Fácil de extender para agregar nuevas figuras o funciones de impresión.

## Instalación

Para instalar las dependencias del proyecto, puedes ejecutar:

pip install -r requirements.txt

Si deseas instalarlo desde el código fuente:

git clone https://github.com/tu-usuario/impresora-2d-python.git
cd impresora-2d-python
pip install -e .

Uso

Desde la línea de comandos

Ejemplo de uso para dibujar una línea:

python impresora2d.py --figura linea --x1 0 --y1 0 --x2 10 --y2 10

Para generar un archivo de salida con el dibujo:

python impresora2d.py --figura cuadrado --x 5 --y 5 --lado 10 -o dibujo.txt

Desde Python

Puedes utilizar la impresora 2D dentro de tus proyectos de Python de la siguiente manera:

from impresora2d import Impresora2D

impresora = Impresora2D()
impresora.dibujar_linea(0, 0, 10, 10)
impresora.guardar('dibujo.txt')

Docker

Si prefieres usar Docker, puedes ejecutar el proyecto de la siguiente manera:

docker build -t impresora2d:latest .
docker run --rm impresora2d:latest --figura circulo --x 5 --y 5 --radio 3

Contribuir

Este proyecto es de código abierto y se aceptan contribuciones. Puedes ayudar de las siguientes maneras:

Reportando errores o sugiriendo mejoras en la sección de Issues.

Enviando pull requests con nuevas funciones o correcciones.

Pasos para contribuir

Haz un fork del repositorio.

Crea una rama con la funcionalidad que deseas agregar.

Envía tu pull request para revisión.

Pruebas

Para ejecutar las pruebas del proyecto:

pytest tests/

Licencia

Este proyecto está bajo la licencia MIT. Puedes ver más detalles en el archivo LICENSE.

¡Esperamos que disfrutes usando la impresora 2D en Python y contribuyas con mejoras!