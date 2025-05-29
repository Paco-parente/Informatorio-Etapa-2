#contador = 0
#while True:
#   contador += 1
#    print(f"hola hace frio {contador} veces")

# flag = True
# while flag:
#     print ("hola infor tengo frio")

#     respuesta = input("desea continuar? s/n")

#     if respuesta == "n":
#         flag = False  

# while True :
#     print ("hola infor tengo frio")

#     respuesta = input("desea continuar? s/n")

#     if respuesta == "n":
#         break 

while True:
    print ("hola infor tengo frio")

    respuesta = input("desea continuar? s/n")

    if not respuesta == "s" or not respuesta == "n":
        print("introduce una respuesta valida")

    if respuesta == "n":
       
        break  

    print("luego del break")