# algoritmo_1.py
# Algoritmo 1: Genera cadenas que pertenecen o no al lenguaje de la gramática

def obtener_cadenas_ejemplo():
    # Retorna dos listas:
    # cadenas_validas: Cadenas que cumplen con la gramática definida (S -> aSb | ε).
    # cadenas_invalidas: Cadenas que contienen caracteres del mismo alfabeto pero no cumplen con la gramática.
    
    cadenas_validas = ["", "ab", "aabb", "aaabbb", "aaaabbbb"]  # Cadenas que siguen la estructura de la gramática
    cadenas_invalidas = ["aa", "bb", "aba", "bba", "aab", "abb", "baa", "abab"]  # Cadenas que no cumplen la regla
    return cadenas_validas, cadenas_invalidas

def principal():
    
    # Función principal que obtiene las cadenas de ejemplo y las imprime,
    # separándolas en válidas e inválidas según la gramática.

    cadenas_validas, cadenas_invalidas = obtener_cadenas_ejemplo()  # Se obtienen las cadenas de prueba
    
    # Se imprimen las cadenas que cumplen con la gramática
    print("Cadenas válidas:")
    for cadena in cadenas_validas:
        print(f"  {cadena}")  
    
    # Se imprimen las cadenas que no cumplen con la gramática
    print("\nCadenas inválidas:")
    for cadena in cadenas_invalidas:
        print(f"  {cadena}")

# Se ejecuta la función principal si el archivo es ejecutado directamente
if __name__ == "__main__":
    principal()
