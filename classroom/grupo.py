from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, alumnos=None):
        self._grupo = grupo
        self._asignaturas = asignaturas if asignaturas is not None else []
        self.listadoAlumnos = alumnos if alumnos is not None else []

    def agregarAlumno(self, *alumnos):
        for alumno in alumnos:
            if isinstance(alumno, list):
                self.listadoAlumnos.extend(alumno)
            else:
                self.listadoAlumnos.append(alumno)

    def listadoAsignaturas(self, **asignaturas):
        for nombre, salon in asignaturas.items():
            asignatura = Asignatura(nombre, salon)
            self._asignaturas.append(asignatura)

    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}"

    @property
    def grado(self):
        return self.__class__.grado
