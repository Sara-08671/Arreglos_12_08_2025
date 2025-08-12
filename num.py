import numpy as np
vector = np.array([1, 2, 3, 4, 5])
print(vector)
# quiero imprimir el tercer elemento del vector (indice 2)
"""
Los vectores no son como las listas, no tienen un método append()
para agregar elementos y no tienen un método pop() para eliminar
elemntos, pero si tienen método reshape() para cambiar su forma, 
adicionalmente despues de creado no se puede cambiar el tamaño del vector
"""
vector1 =np.zeros(5)# Creamos un vector de 5 ceros
print(vector1)
vector2 =np.ones(5)
print(vector2)
vector3 = np.random(1, 5, 100)
print(vector3)#Imprimimos el vector de numeros aleatorios
vector4 = np.linspace(1, 10, 5)
print("linspace", vector4)
vector5 = np.random.rand(10)
print(vector5)
vector6 = np.random.randint(1, 10, 10)
print(vector6)
