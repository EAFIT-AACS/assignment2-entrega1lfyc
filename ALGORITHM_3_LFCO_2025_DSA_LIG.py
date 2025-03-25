import sys
from ALGORITHM_2_LFCO_2025_DSA_LIG import verificarCad, obtenerCad
from rich.console import Console #Nos ayuda a imprimir en consola con formato
from rich.tree import Tree    # Importa la clase Tree para crear árboles de derivación
from rich.table import Table  # Importa  Table para crear tablas con formato

console = Console()    # Crea una instancia de Console para usarla en el print

#----------------------------------OPERACIONES PARA DERIVACIONES----------------------------------
def leftmost_derivation(cadena):
    """
    Tenemos la Gramática: S -> aSb | ε
    """
    try:   #Previene errores de cadenas que no pertenecen al lenguaje
        if cadena.count('a') != cadena.count('b') or "ba" in cadena:
            raise ValueError("La cadena no pertenece al lenguaje generado por la gramática.")

        pasos = []  # Lista para guardar los pasos de la derivación
        S = "S"
        pasos.append(S)  

        num_a = cadena.count('a') # Cuenta cuantos 'a' tiene la cadena
        forma_actual = "S"

        for _ in range(num_a):   # iniciamos reemplazando "S" por "aSb"
            forma_actual = forma_actual.replace("S", "aSb", 1)
            pasos.append(forma_actual)

        forma_actual = forma_actual.replace("S", "ε", 1)  # Al final, reemplaza "S" por ε  para terminar la derivación
        pasos.append(forma_actual)
        cadena_final = forma_actual.replace("ε", "")
        pasos.append(f"La cadena derivada es: {cadena_final}")

        return pasos
    except ValueError as e:  # Si en algun momneto la cadena no es válida, hace catch al error y lo retorna
        return [str(e)]

def imprimirDerivacion(cadena): #Imprime la derivación por la izquierda de la cadena
    tree = Tree(f"Derivación por la izquierda para la cadena: {cadena}")

    pasos = leftmost_derivation(cadena) #Obtenemos los pasos de la derivación
    nodo_raiz = tree.add("S") #Agregamos el nodo raíz

    nodos = [nodo_raiz]  #tenemos una lista para guardar todos los nodos que usamos 

    for paso in pasos[1:-1]:  #Agregamos los nodos de los pasos
        nuevo_nodo = nodos[-1].add(paso)  #Agrega o apila un nuevo nodo al último nodo
        nodos.append(nuevo_nodo)  #Agrega el nuevo nodo a la lista 

    if "La cadena derivada es:" in pasos[-1]:  #Agregamos el último nodo con color verde si la cadena es aceptada, rojo si es rechazada
        nodos[-1].add(f"[bold green]{pasos[-1]}[/bold green]")
    else:
        nodos[-1].add(f"[bold red]{pasos[-1]}[/bold red]")

    console.print(tree) 

#----------------------------------OPERACIONES PARA CONFIGURACIONES----------------------------------

def verificarCadConConfiguraciones(cadena, transiciones):  #Verifica la cadena con las configuraciones
    estado = 'q0'
    pila = ['Z0']
    configuraciones = [(estado, cadena, ''.join(pila))]

    for i, char in enumerate(cadena):   #Iteramos sobre la cadena
        if (estado, char, pila[-1]) not in transiciones: #
            return configuraciones

        estado, operacionPila = transiciones[(estado, char, pila[-1])]
        
        if callable(operacionPila):
            operacionPila(pila)

        configuraciones.append((estado, cadena[i+1:] if i+1 < len(cadena) else 'ε', ''.join(pila)))
    
    return configuraciones

def imprimirConfiguraciones(configuraciones):
    table = Table(title="Configurations an accepting computation of M on input x")
    table.add_column("state", style="cyan", justify="center")
    table.add_column("Remaining string", style="magenta", justify="center")
    table.add_column("Stack", style="yellow", justify="center")
    
    for estado, restante, pila in configuraciones:
        table.add_row(estado, restante, pila)
    
    console.print(table)

def obtenerCadAceptadas():
    inputCad = sys.stdin.readlines()
    cadenas = []
    for linea in inputCad:
        if "es aceptada" in linea:
            cadena = linea.split("'")[1] if "'" in linea else ""
            if cadena:
                cadenas.append(cadena)
    return cadenas

#----------------------------------MAIN----------------------------------
def main():
    cadenasAceptadas = obtenerCadAceptadas() #Obtenemos las cadenas aceptadas que arroja el algoritmo 2
    
    for cadena in cadenasAceptadas:
        imprimirDerivacion(cadena) #Imprimimos la derivación por la izquierda de la cadena
        configuraciones = verificarCadConConfiguraciones(cadena, transiciones) #Obtenemos las configuraciones y las imprimimos
        imprimirConfiguraciones(configuraciones)

transiciones = {  #como no era funcion en ALGORITHM_2_LFCO_2025_DSA_LIG.py, se puso aquí
    ('q0', 'a', 'Z0'): ('q0', lambda lista: lista.append('P')),
    ('q0', 'a', 'P'): ('q0', lambda lista: lista.append('P')),
    ('q0', 'b', 'P'): ('q1', lambda lista: lista.pop()),
    ('q1', 'b', 'P'): ('q1', lambda lista: lista.pop())
}

if __name__ == "__main__":
    main()