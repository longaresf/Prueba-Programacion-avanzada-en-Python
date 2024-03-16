from error import LargoExcedidoException,SubTipoInvalidoException
from anuncio import Anuncio
class Campana():
    MAX = 2

    def __init__(self, nombre:str, fecha_inicio:str, fecha_termino:str, anuncio:str):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncio = anuncio
        self.lista_anuncios = []

    @property
    def fecha_termino(self) -> int:
        return self.__fecha_termino

    @property
    def fecha_inicio(self) -> int:
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio)->None:
        self.__fecha_inicio = fecha_inicio

    @fecha_termino.setter
    def fecha_termino(self, fecha_termino)->None:
        self.__fecha_termino = fecha_termino

    @property
    def anuncio(self) -> int:
        return self.__anuncio
    
    @property
    def nombre(self) -> int:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre)->None:
        self.__nombre = nombre

    @property
    def anuncio(self) -> int:
        return self.__anuncio

    @anuncio.setter
    def anuncio(self, anuncio)->None:
        self.__anuncio = self.anuncio

    def validar_nombre(nombre):
        if len(nombre) > Campana.MAX:
            raise LargoExcedidoException("El nombre de la campaña debe tener menos de 250 caracteres", len(nombre), Campana.MAX)
        else:
            Campana.nombre = nombre

    def __str__(self):
        if self.nombre is None:
            return super().__str__()
        else:
            mensaje_rec = f'Nombre Campaña: {self.nombre}\nAnuncios: {self.anuncio}'
            return mensaje_rec

