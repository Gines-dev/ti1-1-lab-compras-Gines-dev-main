from compras import *

def test_lectura_fichero(lista):
    print("\n test_lectura_fichero")
    print(lista[:3])
    print(lista[-3:])
    print(len(lista))

def test_hora_menos_afluencia(lista):
    print("\n test hora menos afluencia")
    tupla = hora_menos_afluencia(lista)
    print("La hora con menos afluencia es:", tupla[0],"h. con", tupla[1] ,"llegadas de clientes")

def test_clientes_itinerantes(lista):
    print("\n test clientes")
    lista =clientes_itinerantes(lista, 7)
    print(lista)

def main():
    lista = lectura_fichero("ti1-1-lab-compras-Gines-dev-main/data/compras.csv")
    test_lectura_fichero(lista)
    test_hora_menos_afluencia(lista)
    test_clientes_itinerantes(lista)

if __name__ == "__main__":
    main()
