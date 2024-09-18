from Funciones import nuevo_tema, nuevo_subtema


print('hola mundo mi nombre es "juuzou"')
print('saludos')

def error():
    yufdkhbdhbabbauwbjbjbbdbska.hjhjgg
 
def factorial(n): 
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)
numero = 500
print ("factorial de", numero, " es ", factorial(numero))


nuevo_tema("variebles")
edad = 20
print('edad:', edad)

altura = 1.65
print("altura:", altura)

nombre = "Eduardo"
print("nombre:", nombre)

es_trabajador = True
print(es_trabajador)




nuevo_tema("listas")

frutas = ['manzanas', 'peras', 'piñas', 'naranjas', 'guayabas', 'papayas'] 
print('frutas: ',frutas)

varias_cosas = ['Escuela', 23, True, frutas]
print('varias_cosas', varias_cosas)

"""
    seleccionando un elemento
    comentario de multiples lineas
"""
print('frutas[2]: ', frutas[2])

print('frutas[-1]: ', frutas[-1])
print('frutas[-2]: ', frutas[-2])

print('frutas[1:5]: ', frutas[1:5])
print('frutas[1:5:2]: ', frutas[1:5:2])

# agregando un elemento al final
frutas.append('fresas')
print("frutas: ", frutas)

frutas.remove('naranjas')
print("frutas: ", frutas)

frutas.insert(4, 'kiwi')
print("frutas: ", frutas)

#creando una lista vacia
calificaciones = []
libros=list () #genera otra lista
print('calificaciones', calificaciones)
print('libros', libros)

frutas.reverse()
print("frutas: ", frutas)
frutas.sort()
print("frutas: ", frutas)

nuevo_tema("diccionarios")

persona ={"nombre " :"pedro", 
         "apellido": "perez", 
         "edad": 48, 
         "estatura": 1.70, 
         "hijos": ["casimira", "bryan", "eliud"] }

print ("persona : ", persona)


print("persona.keys(): ",persona.keys())
print("persona.values(): ", persona.values())

print('persona_get("nombre ") :', persona.get("nombre "))
print('persona_get("estatura") :', persona.get("estatura"))
#items significa dame todos los elementos
print("persona.items(): ", persona.items())

nuevo_tema("ciclos")
nuevo_subtema("for")
for i in range(10):
    print(i)

print("############")
for i in range(3,10,):
    print(i)

print("############")
for i in range(3,10, 2):
    print(i)

print ("len(frutas):", len(frutas))

for fruta in frutas:
    print(fruta) 
print("########## con led")
for indice in range(len(frutas)):
    print("indice", indice , frutas[indice])

print("########### con enumerate")
for indice , fruta in enumerate (frutas):
    print(indice,fruta)

print("############ for en un diccionario")
for key, value in persona.items():
    print(key, value)