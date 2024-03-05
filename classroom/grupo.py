class Grupo:
    def __init__(self, nombre, asignaturas, alumnos):
        self._nombre = nombre
        self._asignaturas = asignaturas
        self._alumnos = alumnos

    def agregarAlumno(self, nombre, asignaturas):
        self._alumnos.append(Alumno(nombre, asignaturas))

    def listadoAlumnos(self):
        return [alumno.nombre for alumno in self._alumnos]

    def __eq__(self, other):
        if not isinstance(other, Grupo):
            return False
        return self._nombre == other._nombre and self._alumnos == other._alumnos
