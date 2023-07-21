"""
1. Mostrar mensaje
2. Leer por consola
3. Variables
4. Estructuras
5. Listas, dicciones, conjuntos
6. Objetos
"""
print("Hola mundo :')")
#Leer datos de entrada
#desde la terminal (consola) y guardarlos en una variable:
"""nombre = input('Ingrese su nombre:') #guardamos el valor ingresado
edad=int(input('Ingrese su edad'))
print(f'mi nombre es {nombre} tengo {edad}')
print(type(edad))
if edad>=18 and nombre!='perrone':
   print("Donde las petristas")
else:
   print(f'Prohibido la entrada señorit@ {nombre}')
suma=0
for i in range(1,21):
   suma+=i
print(f'la suma de los 20 primeros números es {suma}')

datos=0
numero=int(input("Ingrese dato"))
while numero!=25:
   numero=int(input("Ingrese dato"))
   datos+=numero
print(datos)
"""
#listas
lista=[3,4,"Cualquier datos",["Lista dentro de lista",43,32],25]
print(lista)
lista.append(7)
print(lista)
lista.pop()
print(lista)
#Conjuntos
lista=[3,4,2,3,4,5,6,7,1,3]
conjunto=set(lista)
print(conjunto)
#Union Intersección
A={1,2,3}
B={2,3,4}
#Intersección
C=A&B
print(f'La intersección es {C} ')
#Unión
D=A|B
print(f'La Unión es {D} ')
D.add(748)

#<>
#Tupla
tupla=(4,4,3,2,1,4)
print(tupla)
diccionario={"nombre":"Santiago","apellido":"Sierra","Edad":19}
print(diccionario["nombre"])
