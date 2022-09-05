# Podemos crear o definir nuestras propias funciones
# Lo hacemos con la palabra especial "def" y el cuerpo
# La función debe ir correctamente indentado

def chuchuwa(inst) :
    print("chuchuwa chuchuwa chuchuwa wa wa!")
    print("chuchuwa chuchuwa chuchuwa wa wa!")
    print("Atención!, Compañía:")
    print(inst)

print(chuchuwa)
print(type(chuchuwa))

# El llamado de la función 
chuchuwa("Mano hacia el frente")
chuchuwa("Hombros hacia atrás")

# Las funciones deben llamarse o ejecutarse con los mismos parámetros que se definió
chuchuwa(42) # no cumple el parametro
result = chuchuwa("lengua afuera")

# Si la función no tiene un valor de retorno,nos entregará "None",que es para representar:"Nada"
print(result)

