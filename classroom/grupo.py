from classroom.asignatura import Asignatura

class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, alumnos=None):
        self._grupo = grupo
        self._asignaturas = asignaturas if asignaturas is not None else []
        self.listadoAlumnos = alumnos if alumnos is not None else []
        self.__class__.grado = "Grado 12"

    def agregarAlumno(self, *alumnos):
        for alumno in alumnos:
            if isinstance(alumno, list):
                self.listadoAlumnos = alumno + self.listadoAlumnos
            else:
                self.listadoAlumnos.append(alumno)

    def listadoAsignaturas(self, **asignaturas):
        self._asignaturas.extend(Asignatura(nombre) for nombre in asignaturas.values())

    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}"

    @property
    def grado(self):
        return self.__class__.grado

