class Asignatura:

    def __init__(self, nombre=None, salon="remoto"):
        self._nombre = nombre
        self._salon = salon

    def __str__(self):
        if self._nombre is not None:
            return f"{self._nombre} {self._salon}"

    # def __str__(self):
    #     pass
