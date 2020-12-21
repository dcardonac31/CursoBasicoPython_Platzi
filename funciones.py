# def imprimir_mensaje():
#     print('mensaje especial: ')
#     print('Estoy aprendiendo a usar funciones')


# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()


def conversacion(opcion):
    print('Hola')
    print('Cómo estás')
    print('Elegiste la opción '+ opcion)
    print('Adios')

opcion = input('Elige una opción (1, 2, 3): ')
if opcion == '1':
    conversacion(opcion)
elif opcion == '2':
    conversacion(opcion)
elif opcion == '3':
    conversacion(opcion)
else:
    print('Escribe la opción correcta')
