from campana import Campana 
from anuncio import Anuncio, Video, Display, Social 
from error import SubTipoInvalidoException, LargoExcedidoException
from datetime import datetime
import os

tipo_anuncio = None

try:
    fecha_actual = datetime.now()
    c = Campana('Ventas_csc', str(fecha_actual).split("  ")[0], '11-05-2024', 'Video')
    nom_c = input(f'Nombre de campaña actual: {c.nombre}. Favor indique nuevo nombre para la campaña\n')
    opcion = int(input(f'Favor indique nuevo tipo de anuncio para la campaña. Tipo de campaña actual: {c.anuncio}.\n1. Video\n2. Display.\n3. Social\n'))
    if opcion == 1:
        if Campana.anuncio.__class__ != Video:
            tipo = 'Video'
        else:
            print(f'favor seleccione una opción distinta a: {Campana.anuncio}')

    if opcion == 2:
        if Campana.anuncio.__class__ != Display:
            tipo = 'Display'
        else:
            print(f'favor seleccione una opción distinta a: {Campana.anuncio}')
            
    if opcion == 3:
        if Campana.anuncio.__class__ != Social:
            tipo = 'Social'
        else:
            print(f'favor seleccione una opción distinta a: {Campana.anuncio}')

    Campana.validar_nombre(nom_c)
    Anuncio.validar_tipo(tipo)
    Campana.validar(tipo)
    c = Campana(nom_c, str(fecha_actual).split("  ")[0], '11-05-2024', tipo)

    Anuncio.mostrar_formatos(tipo)
 

except LargoExcedidoException as e:
    print("Error LargoExcedidoException.", e)

    fecha_actual = datetime.now()
    with open(f"error.log", "a") as log:
            log.write(f"{fecha_actual} - [ERROR]: {e}\n")

except SubTipoInvalidoException as e:
    print("Se produjo error SubTipoInvalidoException.", e)

    fecha_actual = datetime.now()
    with open(f"error.log", "a") as log:
            log.write(f"{fecha_actual} - [ERROR]: {e}\n")
