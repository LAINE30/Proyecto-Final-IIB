# Impresora 2D en Python


[![PyPI](https://img.shields.io/pypi/v/markitdown.svg)](https://laine30.github.io/)
![PyPI - Downloads](https://img.shields.io/pypi/dd/markitdown)
[![Built by AutoGen Team](https://img.shields.io/badge/Built%20by-AutoGen%20Team-blue)](https://github.com/LAINE30/Proyecto-Final-IIB.git)

> [!IMPORTANT]
> Impresora 2D en Python 1.0.0 alpha 1. Este proyecto es una impresora 2D escrita en Python que permite crear patrones y dibujos básicos en una cuadrícula utilizando coordenadas cartesianas.


## Características

- Dibujo de figuras geométricas simples (líneas, cuadrados, círculos).

- Guardado e impresión de patrones en formato de texto o imagen.

- Interfaz gráfica fácil e intuitiva de manejar

- Fácil de extender para agregar nuevas figuras o funciones de impresión.

## Instalación

Para instalar Impresora2D, usa pip: `pip install Impresora2D`. Por otra parte, tu puedes instalarlo de otra forma:

```bash
git clone github.com/LAINE30/Proyecto-Final-IIB.git
cd Impresora2D
pip install -e .
```
## Uso

### Desde la línea de comandos de shell

```bash
python Impresora2D.py
```
En la ventana principal tu puedes modificar aspectos tales como:
- Seleccionar archivo SVG
- Distancia entre puntos (0.1-0.5mm)
- Velocidad de animación
- Cambiar el color de impresión

### Plugins

Por ahora esta versión no soporta plugins, pero en actualizaciones futuras tendrá grandes novedades...

Para encontrar plugins válidos,uscar en GitHub con en hashtag #Impresora2D-plugins

## Archivos necesarios

Para instalar las dependencias del proyecto, puedes ejecutar:

```bash
pip install -r requirements.txt
```

## Desde Python

Puedes utilizar la impresora 2D dentro de tus proyectos de Python de la siguiente manera:

from impresora2d import Impresora2D

```python
impresora = Impresora2D()
impresora.dibujar_linea(0, 0, 10, 10)
impresora.guardar('dibujo.txt')
```

## Contribuir

Este proyecto es de código abierto y se aceptan contribuciones. Puedes ayudar de las siguientes maneras:

Reportando errores o sugiriendo mejoras en la sección de Issues.

Enviando pull requests con nuevas funciones o correcciones.

## Pasos para contribuir

Haz un fork del repositorio.

Crea una rama con la funcionalidad que deseas agregar.

Envía tu pull request para revisión.

Pruebas

Para ejecutar las pruebas del proyecto:

pytest tests/

Licencia

Este proyecto está bajo la licencia MIT. Puedes ver más detalles en el archivo LICENSE.

¡Esperamos que disfrutes usando la impresora 2D en Python y contribuyas con mejoras!
