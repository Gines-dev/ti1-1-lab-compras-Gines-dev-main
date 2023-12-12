from collections import *
from datetime import *
import csv

Compra = namedtuple('Compra','dni,supermercado,provincia,fecha_llegada,fecha_salida,total_compra')

def lectura_fichero(ruta_fichero):
    with open(ruta_fichero, encoding="utf-8") as f:
        res = []
        lector = csv.reader(f, delimiter=",")
        next(lector)
        for dni,supermercado,provincia,fecha_llegada,fecha_salida,total_compra in lector:
            dni = dni
            supermercado = supermercado
            provincia = provincia
            fecha_llegada = lectura_fecha(fecha_llegada)
            fecha_salida = lectura_fecha(fecha_salida)
            total_compra = float(total_compra)
            res.append(Compra(dni,supermercado,provincia,fecha_llegada,fecha_salida,total_compra))
        return res


def lectura_fecha(texto):
    return datetime.strptime(texto, "%d/%m/%Y %H:%M")

def hora_menos_afluencia(lista_tup):
    dicci = defaultdict(int)
    for i in lista_tup:
        clave = i.fecha_llegada.hour
        dicci[clave] += 1
    return min(dicci.items(), key=lambda x:x[1])
    
Posición_ranking = namedtuple('posición_ranking','supermercado, facturación')

def supermercados_mas_facturacion(lista_tup):
    #lista = list()
    #for i in lista_tup:
    #sorted(dicc.items(), reverse=True, key=lambda t:t[1])[n]
    #pass
    pass

def clientes_itinerantes(compras: list[Compra],n: int) -> list[tuple[str, list[str]]]:
    lista_res=list()
    dicci = defaultdict(set)
    for i in compras:
        clave = i.dni
        dicci[clave].add(i.provincia)
    for dni, conj_pro in dicci.items():
        if len(conj_pro)>n:
            lista_pro = sorted(conj_pro)
            lista_res.append((dni,lista_pro))
    return lista_res

