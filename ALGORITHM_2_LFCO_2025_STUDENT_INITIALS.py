# algoritmo_2.py
# Algoritmo 2: Implementa un Autómata con Pila (PDA) que reconoce las cadenas generadas por la gramática

from ALGORITHM_1_LFCO_2025_STUDENT_INITIALS import obtener_cadenas_ejemplo

def automata_pila_acepta(cadena):
    pila = []
    
    for caracter in cadena:
        if caracter == 'a':
            pila.append('A')  # Se agrega un elemento a la pila cuando se encuentra 'a'
        elif caracter == 'b':
            if pila:
                pila.pop()  # Se elimina un elemento de la pila cuando se encuentra 'b'
            else:
                return False  # Si no hay elementos en la pila y se encuentra 'b', la cadena no es válida
    
    return len(pila) == 0  # La pila debe estar vacía para que la cadena sea aceptada

def principal():
    
    # Función principal que obtiene cadenas de prueba y evalúa si son aceptadas por el autómata con pila.
    
    cadenas_validas, cadenas_invalidas = obtener_cadenas_ejemplo()
    cadenas_prueba = cadenas_validas + cadenas_invalidas
    
    print("Resultados del Autómata con Pila:")
    for cadena in cadenas_prueba:
        resultado = "Aceptada" if automata_pila_acepta(cadena) else "Rechazada"
        print(f"Cadena '{cadena}' -> {resultado}")

if __name__ == "__main__":
    principal()
