import random

def generarCadAceptadas():
    """Obtenemos la cantidad de veces que a, y por tanto b, se mostrarán de forma aleatoria (randint toma los valores inclusive, ambos)"""
    n=random.randint(0,10)
    """En python podemos multiplicar strings, haciendo que este se repita n número de veces, y concatenar cadenas con el +, así generamos la cadena aceptada por el lenguaje, 
    con ayuda de f"", convertimos lo que está dentro de {} a string, y le agregamos las comillas simples """
    return f"'{'a'*n + 'b'*n}'"

def generarCadRechazadas():
    n=random.randint(1,10)
    """Quisimos tener dos "versiones" de las cadenas rechazadas, las cuales se ejecutarán
    de forma "aleatoria" al obtener un 0 o 1 con randint, y convirtiendolo a bool"""
    k=bool(random.randint(0,1))
    if(k):
        return f"'{'ab'*n + 'b'*n}'"
    return f"'{'a'*n + 'b'*(n+1)}'"

def main():
    """Usamos un ciclo para generar n cadenas"""
    for i in range(5):
        print(generarCadAceptadas())
    for i in range(5):
        print(generarCadRechazadas())



if __name__=="__main__":
    main()
