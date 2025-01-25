import os
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def cargar_svg(ruta_archivo):
    # Verificar si el archivo existe
    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo '{ruta_archivo}' no existe.")
        return None

    try:
        tree = ET.parse(ruta_archivo)
        root = tree.getroot()
        return root
    except Exception as e:
        print(f"Error al cargar el archivo SVG: {e}")
        return None

def dibujar_svg(svg_root):
    fig, ax = plt.subplots()

    # Ajuste de límites y proporciones
    ax.set_aspect('equal')
    ax.set_xlim(0, 500)
    ax.set_ylim(0, 500)
    
    for elem in svg_root.iter():
        tag = elem.tag.split('}')[-1]  # Quitar el namespace si existe

        if tag == 'rect':
            x = float(elem.get('x', 0))
            y = float(elem.get('y', 0))
            width = float(elem.get('width', 0))
            height = float(elem.get('height', 0))
            ax.add_patch(patches.Rectangle((x, y), width, height, fill=False, edgecolor='blue'))

        elif tag == 'circle':
            cx = float(elem.get('cx', 0))
            cy = float(elem.get('cy', 0))
            r = float(elem.get('r', 0))
            ax.add_patch(patches.Circle((cx, cy), r, fill=False, edgecolor='red'))

        elif tag == 'line':
            x1 = float(elem.get('x1', 0))
            y1 = float(elem.get('y1', 0))
            x2 = float(elem.get('x2', 0))
            y2 = float(elem.get('y2', 0))
            ax.plot([x1, x2], [y1, y2], color='green')

    plt.gca().invert_yaxis()  # Invertir para coincidir con coordenadas SVG
    plt.title("Representación 2D del archivo SVG")
    plt.show()

# Construcción segura de la ruta del archivo SVG
ruta_svg = os.path.join(os.getcwd(), 'impresora3D', 'models', 'casa.svg')

# Procesar e imprimir SVG
svg = cargar_svg(ruta_svg)
if svg:
    dibujar_svg(svg)
