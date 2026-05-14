
# frase = input("Ingrese una frase: ").lower()
# vocales = consonantes = espacios = 0

# frase_convertida = frase.split()
# frase_convertida = "".join(frase_convertida)

# if frase_convertida.isalpha():
#     for caracter in frase:
#         if caracter in "aeiou":
#             vocales += 1
#         elif caracter == " ":
#             espacios += 1
#         else:
#             consonantes += 1
#     print("Vocales:", vocales)
#     print("Consonantes:", consonantes)
#     print("Espacios:", espacios)

# else:
#     print("La frase que ingresaste no puede ser analizada pues incluye números o caracteres especiales")

#====================================================================================

# inf = int(input("Ingrese el límite inferior (el límite inferior no puede ser menor a 2): "))

# if inf < 2:
#     inf = 2

# if inf > 49:
#     inf = 49

# sup = int(input("Ingrese el límite superior (el límite superior no puede ser menor al inferior ni mayor a 50) :"))

# if sup < inf:
#     sup = inf +1

# if sup > 50:
#     sup = 50

# for numero in range(inf, sup+1):
#     es_primo = True
#     for divisor in range(2, numero):
#         if numero % divisor == 0:
#             es_primo = False
#             break
#     if es_primo:
#         print(numero, "es primo")
#     else:
#         print(numero, "no es primo")

#=======================================================================================================

# intentos = 3
# respuesta = 4
# belphegor = 5

# while intentos > 0 and belphegor != respuesta:
#     if intentos == 3:
#         print("h")
#     elif intentos == 2:
#         print()
#     else:
#         print()

#Nah, no vale la pena seguir pensando en eso
