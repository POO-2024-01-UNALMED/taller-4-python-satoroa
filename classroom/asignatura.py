class Asignatura:
    def __init__(self, nombre, salon=None):
        self._nombre = nombre
        self._salon = salon

    def __eq__(self, other):
        if not isinstance(other, Asignatura):
            return False
        return self._nombre == other._nombre and self._salon == other._salon