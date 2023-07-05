# DÍA 2

# ! FUNCIONES BÁSICAS Y SINTAXIS

# Sintaxis normal de una función sin parámetros. 
def decir_hola():
    print("Hola");

decir_hola();


# Función para saber si hay un número par en una lista:

num_list = [1,2,3,4,5,6,7,8,9,10];

def check_num_par(num_list):
    for num in num_list:
        if num % 2 == 0:
            print(f"El número {num} es par");

check_num_par(num_list); # Esto recorrerá la lista y retornará: El número 2 es par
                                                               #El número 4 es par
                                                               #El número 6 es par
                                                               #El número 8 es par
                                                               #El número 10 es par


# ! *ARGS Y **KWARGS (Los KWARGS trabajan en forma de diccionario mientras que los ARGS trabajan en forma de tuplas)

# def funcion(a,b): # <-- a esto se le llaman argumentos posicionales, porque se encuentran en la posicion en el 0 y 1 en este caso.
    # Retornar el 5% de la suma de a y b
    # print (sum((a,b) * 0.05));

# funcion(40,50)


# Caso con *ARGS 
def funcion_args(*args): # <-- va a recibir los argumentos que le pasé en la invocación
    return print(sum(args) * 0.05) # <-- usará los argumentos recibidos en "args".

funcion_args(100, 100, 200, 100, 100); # <-- Acá le puedo ir pasando todos los argunmentos que yo quiera. Importante: retorna una #!TUPLA

#Caso con **KWARGS
def funcion_kwargs(**kwargs):
    if "fruit" in kwargs:
        print("Mi fruta escogida es la {}".format(kwargs["fruit"]))
    else:
        print("No hay fruta")

funcion_kwargs(fruit="manzana", veggie="lechuga")

#Caso con *ARGS y KWARGS
def funcion_combinada(*args, **kwargs):
    print(args)
    print(kwargs)
    print("me gustaría {} {}".format(args[0], kwargs['comida']))

funcion_combinada(10, 30, 50, fruta="naranja", comida='leche', animal='perro');


# ! FUNCIONES LAMBDA (las expresiones lambda también se conocen como funciones anónimas)

# Ejemplo básico:
numeros = [1,2,3,4,5];

square = lambda num: num ** 2

print(square(5));

# ----- otro ejemplo ----- #

numeros = [1,2,3,4,5];

square = lambda num: num ** 2

print(list(map(lambda num: num ** 2, numeros))); # Devuelve una lista

# ----- otro ejemplo -----

lambda_func = lambda x: True if x**2 >= 10 else False # 'x' es el argumento de entrada de la función lambda.
lambda_func(3) # Retorna False
lambda_func(4) # Retorna True

# True if x**2 >= 10 else False; es una expresión condicional que devuelve True si la condición x**2 >= 10 es verdadera, y False en caso contrario.

mi_dicc = {"A": 1, "B": 2, "C": 3}
sorted(mi_dicc, key=lambda x: mi_dicc[x]%3) # Retorna ['C', 'A', 'B']