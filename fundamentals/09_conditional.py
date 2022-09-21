# Tenemos expresiones que se pueden evaluar en términos booleanos 
# ó dicótomicos
# Ejemplo:

print(10 > 9)

# Esto nos permite hacer ejecuciones condicionales,por ejemplo

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False 

gaby_age = 4
Silvia_age = 44

# Estas siguientes instrucciones las podríamos leer como:
# "Si resultado de is_adult ejecutada con la variable gaby_age
# es verdadero,entonces el programa imprime '¿Quieres una Cerveza'
# de otro modo (else),imprime ' Cantemos Chuchuwa?'"

if is_adult(gaby_age):
 print("¿Quieres una cerveza?")
else:
 print("Cantemos chuchuwa") 



if is_adult(Silvia_age):
    print("¿quieres una cerveza?")
else :
    print("Cantemos chuchuwa?")

# elif es una abreviación de " else is",nos permite seguir evaluando expresiones.Podemos tener tantos elif 
# como necesitemos
if Silvia_age > gaby_age:
    print("Silvia es mayor que gaby")
elif silvia_age < gaby_age:
    print("silvia es menor que gaby")
else:
    print("Tienen la misma edad gaby y silvia")
  
