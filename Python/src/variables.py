'''
Created on 3 ene. 2021

@author: aleja
'''

# Ejemplos de variables
numero = 1
flotante = 1.55
string = 'Hola soy un string'
booleano = True
otroBoolPeroFalso = False
otroBoolPeroResultado = (1 == 34)
otroBool = ("soy" in string)
boolNotIn = ("un" not in string)
print(numero,flotante,string,booleano,otroBoolPeroFalso,otroBoolPeroResultado,otroBool);

# Ejemplos de variables numericas
suma = 44 + 25
resta = 79 - 10
div = 84 / 2
mult = 23 * 3
resto = 50 % 5
# print('Resultado de la suma',suma, 'de la resta',resta,'de la div',div
#       , 'de la mult', mult, 'del resto', resto)
# print('Ahora al cuadrado',2**2)
# print('Operacion completita',(5+33)/(8**2 - 66))

# Ejemplos de variables string
#sin_escapado = 'hey hey how are you my friend are you going to MOE's''
escapado = "hey hey how are you my friend are you going to MOE's"
print(escapado);
nombre = 'Charles'
apellido= 'Bukowski'
print(nombre + " " +  apellido);
print(nombre * 3 + " " + apellido * 4)

luchador = 'Daniel Bryan'
print(luchador[3])
letrita = luchador[9]
print(letrita)
print(luchador[3:7])
print(luchador[2:])
print(luchador[:5])
print(luchador[0:9:4])
print(luchador[-4:-1])

# La linea de aqui abajo devuelve error
# luchador[0] = 'd'
minusculas = 'd' + luchador[1:]
sinespcaio = luchador[0:6] + '' + luchador[7:]
print(minusculas, " y sin espacio:",sinespcaio)

# Ejercicios con listas
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)
listaloca = ["stringazo",69,88.87,False]
print(listaloca)
print(listaloca[0] * 2 + " aqui estamos")
print(listaloca[1] / lista[4])


listaloca[0] = "otro string"
lista.append(20)
print(lista)
print(listaloca)

# Cuando se quiere modificar una lista entero se utiliza [:] que sirve para hacer una copia
lista[:] = []
print(lista)
print(len(lista))

# Ejemplo de una lista bidimensional
matriz = [[2,3,4,5],[1,5,8,7]]

for fila in matriz:
    for columna in fila:
        print(columna,end=' ')
    print()
