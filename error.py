class LargoExcedidoException(Exception):
    def __init__(self, mensaje:str, largo:int, maximo:int) -> None:
        self.mensaje = mensaje
        self.largo = largo
        self.maximo = maximo

    def __str__(self) -> str:
        if self.largo is None and self.maximo is not None:
            return super().__str__()
        else:
            mensaje_rec = f'Mensaje: {self.mensaje}, Largo: {self.largo}, Máximo: {self.maximo}'
            return mensaje_rec

class SubTipoInvalidoException(Exception):
    def __init__(self, mensaje:str, tipo:str) -> None:
        self.mensaje = mensaje
        self.tipo = tipo
    
    def __str__(self) -> str:
        if self.tipo is None:
            return super().__str__()
        else:
            mensaje_rec = f'Mensaje: {self.mensaje}, Tipo: {self.tipo}'
            return mensaje_rec

