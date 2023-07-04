                            # APUNTES DE COSAS QUE ME PARECEN IMPORTANTES

miCadena = "Hola Mundo";

# ! Sistema del slicing -> start:stop:step

print(miCadena[0:3])

# El método .split() que es muy útil:

x = "hola mundo"
x = x.split() # Esto separaría por espacios

# Normalmente cuando tenemos un set de datos los tenemos separados así= "Hola|Mundo|Todo|Bien?"
# Y si nosotros hacemos un x = x.split("|") devolvería todo así= "Hola","Mundo","Todo","Bien?"


# ! FORMATO DE IMPRESIÓN DE CADENAS DE TEXTO

#.format() y F-strings.
print('Esta es una cadena de {}'.format('TEXTO'))
# imprime: Esta es una cadena de TEXTO

print('Esta {} {} {}'.format('es', 'una', 'cadena'))
# imprime: Esta es una cadena

print('Esta {0} {0} {0}'.format('es', 'una', 'cadena'))
# imprime: Esta es es es
# Porque está agarrando el 'es' del .format

print('Esta {0} {1} {2}'.format('es', 'una', 'cadena'))
# Así sería la manera correcta de hacerlo.

print('Esta {e} {u} {c}'.format(e = 'es', u = 'una', c = 'cadena'))
# Esta es otra manera de hacerlo aplicando variables en el .format


resultado = 100/888 # Esto es igual a: 0.11261261261261261
# Formateo de float "{valor:width.precision.f}"
print("Los resultados son {r:1.5f}".format(r=resultado))
# Normalmente voy a querer trabajar con precisión.

# Otra manera de aplicar interpolación de cadena de texto ->
nombre = "Rodrigo"
apellido = "Palomo"
edad = 22

print(f"Mi nombre es {nombre}, mi apellido es {apellido} y tengo la edad de {edad}")


# ! LISTAS (diccionarios(clave valor)).

mi_diccionario = {
    'manzana': '2.90',
    'panqueques':['manzana','banana'],
    'leche': '5.90'
}
# Si quiero agregar un objeto nuevo con su respectivo valor:
mi_diccionario['coca'] = 10

# Si quiero ver cuántas "keys" hay, ejecuto el comando .keys()
print(mi_diccionario.keys())
# Si quiero ver los valores le atribuyo el método .values()
print(mi_diccionario.values())
# Si quiero ver los pares separados por paréntesis ejecuto el método .items()
print(mi_diccionario.items())


# ! TUPLAS (son como las listas, pero con la diferencia de que las tuplas son inmutables, es decir, que no puede ser reasignado.)

t = (1, 2 ,3);
lista = [1, 2, 3];
print(lista)

# No permite reasignación
# t[0] = "Cosa";

# Permite reasignación.
lista[0] = "Cosa";


# ! SETS: Los sets son una representación única y desordenada de elementos.

miset = set()

miset.add(1) # Esto va a retornar un {1}, es decir, cuando la computadora lea 
             # el print(miset) va a retorar ese valor.

milista = [1,1,1,2,2,2,3,3,3];
print(set(milista)) # Esto va a retornar los elementos que no están repetidos, es decir {1, 2, 3}.
                    # Aunque parezca que los "set" tienen orden porque están en {1, 2, 3}, no, no lo tienen.


# ! OPERADORES LÓGICOS
# && = and
# || = or
#- ! = not

# ! DECLARACIONES

# Sin mucho más que agregar a los que ya sé. Sólo cambia la sintaxis en el "else if(){}"

hambre = True;
sed = False;

if hambre and not sed:
    print("¡Tenemos hambre!")
elif hambre == True and sed == True:
    print("¡Tenemos hambre y sed!")
else:
    print("¡No queremos nada!")

# Nótese que la sintaxis es distinta. No hay paréntis y tampoco hay llaves. Los paréntesis se obvian y las llaves se reemplazan con un ":", podríamos traducirlo como un "entonces".
# También recalcar que los operadores lógicos son utilizados con palabras literales.


# ! CICLOS FOR

lista_iterable = [1,2,3,4,5,6,7,8,9,10];

for num in lista_iterable:
    print(num)
# Ciclo For común de toda la vida

# ahora vamos a checkear a ver cual es par y cual es inpar
suma_lista = 0;

for num in lista_iterable:
    suma_lista = suma_lista + num;

    if(num % 2 == 0):
        print(f"el número {num} es par")
        # print(suma_lista);

# <---- Tupla unpacking ---->

tupla_for = [(1,2),(3,4),(5,6),(7,8)]

for item in tupla_for:
    print(item)
    # Esto imprimirá (1, 2)
                    #(3, 4)
                    #(5, 6)
                    #(7, 8)

for (a,b) in tupla_for:
    print(a)
    print(b)
    # Esto imprimirá : 1
                      #2
                      #3
                      #4
                      #5
                      #6
                      #7
                      #8

d = {'y1': 3, 'y2': 1, 'y3': 2}

for value in d.values():
    print(value)


# ! CICLOS WHILE

# PALABRAS CLAVE ÚTILES
# break
# continue
# pass

x = 0;

while x <= 5:
    print(f"El valor actual de x es {x}")
    x += 1;
else:
    print("X no es mayor que 5")

otra_x = [1,2,3];

for item in otra_x:
    # comment
    pass;
print("Fin del libreto")


# ! OPERADORES ÚTILES 

contador_indice = 0;
palabra = "hola";

for letter in palabra:
    print(palabra[contador_indice])
    contador_indice += 1; #esto imprime
                          #h
                          #o
                          #l
                          #a

# Para no tener que estar haciendo el contador a cada rato hacemos:

for item in enumerate(palabra):
    print(item); #esto imprime:
                 #(0, 'h')
                 #(1, 'o')
                 #(2, 'l')
                 #(3, 'a')

for index,letter in enumerate(palabra):
    print(index)
    print(letter)#esto imprime:
                 #0
                 #h
                 #1
                 #o
                 #2
                 #l
                 #3
                 #a

milista1 = [1,2,3,4,5,6]
milista2 = ['a', 'b', 'c']
d = {'k1': 1}
milista3 = [100, 200, 300]

for item in zip(milista1, milista2): # El .zip() va a unir las listas
    print(item) # esto imprime: #(1, 'a') <- índice 0 de milista1 + índice 0 de milista2 y así sucesivamente
                                #(2, 'b')
                                #(3, 'c')

print(min(milista1)) # el .min() devuelve el número mínimo de esa lista.
print(min(milista1)) # el .max() devuelve el número máximo de esa lista.

resultado = input('Escribe un número aquí: ')

print(resultado)


# Conversor de celcius a fahrenheit
celcius = [0, 10, 20, 34.5]
fahrenheit = [((9 / 5) * temp + 32) for temp in celcius]
print(fahrenheit)


# ! INTRODUCCIÓN A FUNCIONES

