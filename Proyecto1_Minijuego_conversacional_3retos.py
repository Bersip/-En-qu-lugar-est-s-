"""
Proyecto N°1. Hacer un minijuego de una aventura conversacional:
    
    Son 3 retos o habitaciones (libres, el usuario debe resolverlo).
    Preferiblemente resolución con palabras.
    Debe tener la opción de salir que ninguna de las entradas
    del usuario de algún error.
    
"""
    
import modulos.modulo_intro as intro
import modulos.modulo_reto1 as reto1
import modulos.modulo_reto2 as reto2
import modulos.modulo_reto3 as reto3
import modulos.modulo_conclu as conclu

def ciclo_principal():
    pasalir=False
    pasalir = intro.introduccion()
    if pasalir:
        return 0
    pasalir = reto1.puerta1()
    if pasalir:
        return 0
    pasalir = reto2.puerta2()
    if pasalir:
        return 0
    pasalir = reto3.puerta3()
    if pasalir:
         return 0
    pasalir = conclu.final()
    if pasalir:
         return 0
print("---------------------------")
print("     En donde estoy?      ")
print("---------------------------")
   
ciclo_principal()
