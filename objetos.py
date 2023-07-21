class Estudiante:
    def __init__(self, nombre,apellido,edad):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__edad=edad
    def __str__(self):
        return f'el estudiante de nombre {self.__nombre} {self.__apellido} tiene {self.__edad} años'
    def agregarEdad(self):
        self.__edad+=1

estu = Estudiante('Juan', 'Perez', 20)
estu2=Estudiante('Santiago','Sierra',19)
estu3=Estudiante('Sebastian','Perrone',20)
estu4=Estudiante('Mateo','Avalos',21)
estudiantes=[estu,estu2,estu3,estu4]
for i in estudiantes:
    print(i)
class EstudiantePosgrado(Estudiante):
    def __init__(self, nombre, apellido, edad,programa):
        super().__init__(nombre, apellido, edad)
        self.__programa=programa