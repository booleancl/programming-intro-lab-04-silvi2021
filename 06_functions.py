# Una función es un grupo de sentencias con un nombre que realizan una computación.
# Primero uno define una función y luego de "llama" o "ejecuta" esa función.

# Python vienen con muchas funciones listas para usar.
# Solo hay que llamarla o ejecutarlas
print("Hola Silvia")

# La mayoria de las funciones entregan un valor,es decir,nos devuelven el resultado. Ejemplo:

str_num = '32'
real_num = int(str_num) # Esta función  transforma a entero
print(type(real_num))

float_num = 3.999
int_num = int(float_num) # No aplica,corta la parte decimal
print(int_num)

# La función linea es un error
# int("Hola Inmundo")

print(float('32')) # Esta función entrega un float
print(str(3.1415)) # Esta función entrega un str

# Composición de funciones : Anidar funciones

print(str(3.1415))