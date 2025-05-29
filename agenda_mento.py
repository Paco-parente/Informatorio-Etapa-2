#Nivel 3 | Agenda de contactos {
#Dado un diccionario llamado agenda que almacena contactos, donde cada clave es el nombre de una persona y su valor otro diccionario con su teléfono y correo electrónico, escribí un programa qué:
#A- Le pida al usuario que ingrese un nombre para buscar
#B- Verifique si ese nombre está en la agenda
#C- Si está, muestre el número de teléfono y el email correspondiente
#D- Si no está, no muestre nada

agenda = {
    "Ana": {"tel": "12345", "email": "ana@mail.com"},
    "Juan": {"tel": "67890", "email": "juan@mail.com"}
}

nombre = input("buscar contacto")

if nombre in agenda:
    print("Telefono:", agenda[nombre]["tel"])
    print("Email:", agenda[nombre]["email"])

else:
    print("El contacto no esta en la agenda")