import sys

def verificarCad(cadena, transiciones):
    """Establecemos los valores iniciales"""
    estado = 'q0'
    pila = ['Z0']
    
    for i, char in enumerate(cadena):
        """Si la produccion que obtenemos no está definida, rechazamos la cadena"""
        if (estado, char, pila[-1]) not in transiciones:
            return False  
        """Si llega acá, es porque la produccion existe (la llave existe, por lo que 
        obtenemos el valor de esta, y lo desempaquetamos en dos variables, estado y operacionPila
        ,donde estado guardará el valor actualizado del estado, y operacionPila guardará una lambda"""
        estado, operacionPila = transiciones[(estado, char, pila[-1])]
        
        if callable(operacionPila):
            """Si operacionPila es una función (callable), le aplicamos esa operación a la pila,
            la cual representamos por medio de una lista, que es mutable en Python, por lo que no 
            tenemos que reasignar la variable pila, sino que la modificamos (el objeto original)"""
        
            operacionPila(pila)  

    return pila == ['Z0'] 
#no se puso que retorne true/false, porque la comparación ya retorna un bool(necesario para Configuración de algorimo 3) 

"""Nuestro PDA aceptará por pila vacia, entonces si nuestra pila, despues de procesar
la cadena, queda solo con el símbolo inicial, la aceptamos, de otro modo, la rechazamos."""

def imprimirResultado(cadena, boolResultado):
    """Si verificarCad nos retorna true, es porque la pila quedó vacia (solo con el símbolo
    inicial de la pila), entonces la aceptamos,si retorna false, es porque no paso, y rechazamos
    la cadena."""
    if boolResultado:
        print(f"La cadena '{cadena}' es aceptada por el DFA")
    else:
        print(f"La cadena '{cadena}' es rechazada por el DFA")

def obtenerCad():
    """Obtenemos las cadenas generadas en el archivo algoritmo1, esto usando sys, y readlines() pues son varias, si fuera una sería readline(), y las guarda
    en una lista"""
    inputCad = sys.stdin.readlines()
    """Con readlines obtenemos las cadenas junto con el salto de linea, así que se lo quitamos con strip(), y como readlines() obtiene las cadenas
    tal cual se imprimen, le quitamos las comillas simples que agregamos para que el output fuera más legible,con replace(), pues no hay ninguna produccion que
    maneje el char ', por lo que si no lo hacemos, el DFA rechazaría todas las que le pasemos, y las cadenas que queden las guardamos en una lista"""
    inputCad = [linea.strip().replace("'", "") for linea in inputCad]  # Limpiar formato
    return inputCad

def main():
    """Definimos las transiciones en un diccionario, donde key serán los valores "actuales"
    y el value serán los nuevos valores después de leer el char, donde la pila resultante
    está dada por una función lambda, las cuales son para hacer push() o pop() sobre la pila."""
    
    transiciones = {
        ('q0', 'a', 'Z0'): ('q0', lambda lista: lista.append('P')),
        ('q0', 'a', 'P'): ('q0', lambda lista: lista.append('P')),
        ('q0', 'b', 'P'): ('q1', lambda lista: lista.pop()),
        ('q1', 'b', 'P'): ('q1', lambda lista: lista.pop())
    }

    """Las líneas serán las que retorne la función."""
    lineas = obtenerCad()
    for linea in lineas:
        resultado = verificarCad(linea, transiciones)  
        """Imprimir resultado toma la cadena y un valor booleano, el último es retornado por verificarCad, el cual, dependiendo si la cadena se puede
        producir con la gramática, genera un bool."""# Solo retorna True o False
        imprimirResultado(linea, resultado)  # Muestra si es aceptada o rechazada

if __name__ == "__main__":
    main()
