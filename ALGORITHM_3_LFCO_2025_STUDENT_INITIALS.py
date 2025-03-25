# algoritmo_3.py
# Algoritmo 3: Construye el árbol de derivación (o la configuración de aceptación) a partir de las cadenas válidas

import os
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout
from ALGORITHM_1_LFCO_2025_STUDENT_INITIALS import obtener_cadenas_ejemplo

# Ajusta la ruta de Graphviz según tu instalación (este ejemplo es para Windows)
os.environ["PATH"] += os.pathsep + "C://Program Files//Graphviz//bin"

def generar_arbol_derivacion(cadena):

# Genera el árbol de derivación para una cadena dada.
    
    contador_nodos = 0
    pila = [(0, "S")]  # Se inicia la pila con el símbolo de inicio "S"
    aristas = []  # Lista para almacenar las conexiones entre nodos
    
    # Se procesa la cadena de entrada para construir el árbol de derivación
    while pila:
        id_padre, simbolo = pila.pop()
        if simbolo == "S":
            if cadena:
                caracter = cadena[0]  # Se extrae el primer carácter de la cadena
                cadena = cadena[1:]  # Se elimina el primer carácter de la cadena
                if caracter == "a":
                    id_izquierda = contador_nodos + 1
                    id_medio = contador_nodos + 2
                    id_derecha = contador_nodos + 3
                    contador_nodos += 3
                    aristas.append((id_padre, id_izquierda, "a"))
                    aristas.append((id_padre, id_medio, "S"))
                    aristas.append((id_padre, id_derecha, "b"))
                    pila.append((id_derecha, "b"))
                    pila.append((id_medio, "S"))
                    pila.append((id_izquierda, "a"))
            else:
                contador_nodos += 1
                aristas.append((id_padre, contador_nodos, "eps"))  # Se representa la derivación vacía
    return aristas

def dibujar_arbol_derivacion(cadena):
    
# Dibuja el árbol de derivación para una cadena válida.

    grafo = nx.DiGraph()
    aristas = generar_arbol_derivacion(cadena)
    for origen, destino, etiqueta in aristas:
        grafo.add_edge(origen, destino, label=str(etiqueta))
    posicion = graphviz_layout(grafo, prog="dot")
    plt.figure(figsize=(8, 6))
    nx.draw(grafo, posicion, with_labels=True, node_color='lightblue', edge_color='gray', 
            node_size=2000, font_size=10)
    etiquetas_aristas = {(origen, destino): str(etiqueta) for origen, destino, etiqueta in aristas}
    nx.draw_networkx_edge_labels(grafo, posicion, edge_labels=etiquetas_aristas, font_family="Arial", font_size=12)
    plt.title(f"Árbol de derivación para '{cadena}'", fontname="Arial", fontsize=14)
    plt.show()

def principal():
    
# Función principal que obtiene cadenas válidas y genera sus árboles de derivación.
    
    cadenas_validas, _ = obtener_cadenas_ejemplo()  # Se obtienen solo las cadenas válidas
    print("Visualizando árboles de derivación para las cadenas válidas:")
    for cadena in cadenas_validas:
        print(f"Mostrando árbol para '{cadena}'...")
        dibujar_arbol_derivacion(cadena)

if __name__ == "__main__":
    principal()
