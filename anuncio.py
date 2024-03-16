from abc import ABC
from error import SubTipoInvalidoException

class Anuncio(ABC):
    tipo_anuncio = ['Video', 'Display', 'Social']
    def __init__(self, alto:int, ancho:int, campana:dict, anuncio:str) -> None:
        self.__alto = alto
        self.__ancho = ancho
        self.__anuncio = anuncio
        self.__campana = {}

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto)->None:
        if alto >  0:
            self.__alto = alto
        else:
             self.__alto = 1

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho)->None:
        if ancho >  0:
            self.__ancho = ancho
        else:
             self.__ancho = 1

    @property
    def campana(self) -> dict:
        return self.__campana
    
    @campana.setter
    def campana(self, campana)->None:
        self.__campana = campana

    @property
    def anuncio(self) -> str:
        return self.__anuncio

    @anuncio.setter
    def anuncio(self, anuncio)->None:
            self.__anuncio = anuncio

    def validar_tipo(tipo):
        if tipo == 'Social':
            print("Es Social. Formato de red disponible\n")
        elif tipo == 'Display':
            print("Es Display. Formato de pantalla disponible\n")
        elif tipo == 'Video':
            print("Es Video. Formato de pantalla disponible\n")
        else:
            raise SubTipoInvalidoException("El parámetro no corresponde a un SUB_TIPOS", tipo)

    @staticmethod
    def mostrar_formatos(tipo):
        Anuncio.tipo_anuncio.remove(tipo)
        print(f'''                      FORMATO 1: {tipo}
                    =====================
                    - Subtipo 1: {Anuncio.tipo_anuncio[0]}
                    - Subtipo 2: {Anuncio.tipo_anuncio[1]}\n         ''')
    


class Video(Anuncio):
    def __init__(self, ancho:int, alto:int, duración:int, sub_tipo:str) -> None:
        self.__ancho =  ancho
        self.__alto = alto
        self.__duración = duración
        self.sub_tipo = 'Video'

    @property
    def alto(self) -> int:
        return self.alto

    @property
    def sub_tipo(self) -> int:
        return self.sub_tipo

    @alto.setter
    def alto(self, alto)->None:
        if alto >  0:
            self.__alto = alto
        else:
             self.__alto = 1

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho)->None:
        if ancho >  0:
            self.__ancho = ancho
        else:
             self.__ancho = 1

    @property
    def duración(self) -> int:
        return self.__duración

    @duración.setter
    def duración(self, duración)->None:
        if duración >  0:
            self.__duración = duración
        else:
             self.__duración = 5

    def comprimir_anuncio():
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio():
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")


class Display(Anuncio):
    def __init__(self,sub_tipo:str):
        self.sub_tipo = 'Display'
        super().__init__()

    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio():
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")



class Social(Anuncio):
    def __init__(self,sub_tipo:str):
        self.sub_tipo = 'Social'
        super().__init__()

    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")
    def redimensionar_anuncio():
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
