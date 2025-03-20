# PDA y Árboles de Derivación

## 1. Información de los Estudiantes del equipo
- **Nombre del estudiante:** Camilo Alvarez Villegas, Sara Echeverri
- **Número de clase:** Camilo Alvarez Villegas (Lunes de 6pm-9pm 7308), Sara Echeverri (Miércoles de 6pm-9pm 7309)

## 2. Versiones del Sistema Operativo, Lenguaje de Programación y Herramientas
- **Sistema Operativo:** Windows 10 (64-bit)
- **Lenguaje de Programación:** Python 3.9.7
- **Herramientas y Librerías Utilizadas:**
  - [NetworkX](https://networkx.org)
  - [Matplotlib](https://matplotlib.org)
  - [Graphviz](https://graphviz.org)

## 3. Instrucciones para Ejecutar la Implementación

1. **Descargar o clonar** el repositorio.

2. Asegurarse de tener **Python 3** instalado.

3. **Instalar las librerías necesarias:**

   - Abrir una terminal o símbolo del sistema y ejecutar los siguientes comandos:
   
     ```bash
     pip install networkx matplotlib
     ```

4. **Instalación de Graphviz (Paso a Paso):**

   - **Paso 1:** Visitar la página oficial de Graphviz en: [https://graphviz.org/download/](https://graphviz.org/download/)
   - **Paso 2:** En la sección de descargas, buscar la versión para Windows (por ejemplo, "Graphviz Download for Windows 64-bit") y hacer clic en el enlace para descargar el instalador.
   - **Paso 3:** Una vez descargado el archivo (por ejemplo, `graphviz-2.49.3.msi` o una versión similar), ejecutarlo para iniciar el proceso de instalación.
   - **Paso 4:** Seguir las instrucciones del instalador:
     - Aceptar los términos de la licencia.
     - Seleccionar el directorio de instalación (por defecto suele ser `C:\Program Files\Graphviz`).
     - Completar la instalación haciendo clic en "Instalar" y luego "Finalizar".
   - **Paso 5:** Verificar que el directorio que contiene el ejecutable de Graphviz (normalmente `C:\Program Files\Graphviz\bin`) esté agregado a la variable de entorno **PATH**:
     - Para verificarlo, abre una terminal y escribe:
       ```bash
       where dot
       ```
       Si se muestra la ruta `C:\Program Files\Graphviz\bin\dot.exe`, Graphviz está correctamente instalado.
     - **Nota:** Si la ruta no está en el PATH, se puede agregar temporalmente con el siguiente comando en el símbolo del sistema:
       ```bash
       set PATH=%PATH%;C:\Program Files\Graphviz\bin
       ```
       O, para una configuración permanente, agregar manualmente la ruta en las Variables de Entorno de Windows (Panel de Control > Sistema > Configuración avanzada del sistema > Variables de Entorno).

5. **Ejecutar cada uno de los siguientes archivos por separado:**

   - Para generar y visualizar las cadenas (Algorithm 1):
     ```bash
     python ALGORITHM_1_LFCO_2025_STUDENT_INITIALS.py
     ```
   - Para evaluar las cadenas con el PDA (Algorithm 2):
     ```bash
     python ALGORITHM_2_LFCO_2025_STUDENT_INITIALS.py
     ```
   - Para visualizar los árboles de derivación (Algorithm 3):
     ```bash
     python ALGORITHM_3_LFCO_2025_STUDENT_INITIALS.py
     ```

6. Cada script mostrará los resultados en la consola o en ventanas gráficas (en el caso de los árboles de derivación).

## 4. Explicación del Algoritmo

Esta solución para la asignación de Lenguajes Formales se compone de tres algoritmos:

1. **Algorithm 1 (Generación de Cadenas):**
   - Se implementa una función que retorna ejemplos de cadenas válidas (que cumplen con la gramática `S -> aSb | ε`) y cadenas inválidas (que utilizan el mismo alfabeto pero no cumplen la gramática).

2. **Algorithm 2 (PDA):**
   - Se implementa un Autómata de Pila (PDA) que reconoce las cadenas generadas en el Algorithm 1.
   - El PDA inicializa una pila, define las transiciones y procesa la cadena símbolo a símbolo, aceptándola si la pila queda vacía al finalizar.

3. **Algorithm 3 (Árbol de Derivación):**
   - A partir de las cadenas válidas, se construye y visualiza el árbol de derivación (o la configuración de aceptación) correspondiente.
   - Se utilizan las librerías NetworkX, Matplotlib y Graphviz para representar gráficamente el árbol.
