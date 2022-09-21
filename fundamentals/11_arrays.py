# Los arreglos (listas) son una ESTRUCTURA DE DATOS FUNDAMENTAL
# que permite agrupar valores de cualquier tipo,separados por coma

first_array = ['Sacar la basura','peinarse','dormir','secar la ropa']

# En python el primer elemento de un arreglo tiene posición(indice) 0
print(first_array[0]) 

print(first_array[1])
print(first_array[2])
print(first_array[3])

# no existe el elemento con indice 4  python da un error
# print(first_array[4])

# Podemos saber el largo de un arreglo o lista con la funcion pre definida len()

print(len(first_array))

# Ademas podemos agregar elementos al final del arreglo con el metodo append
first_array.append('comer')
first_array.append('dormir')

# Podemos indicar la posición del nuevo elemento a agregar con insert
first_array.insert(0,'levantarse')

# Podemos imprimir la lista completa
print(first_array)



