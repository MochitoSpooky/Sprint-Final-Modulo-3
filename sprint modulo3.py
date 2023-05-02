import random

usuarios = ['usuario1', 'usuario2', 'usuario3', 'usuario4', 'usuario5', 'usuario6', 'usuario7', 'usuario8', 'usuario9', 'usuario10']

cuentas = {}

def crear_cuenta(usuario):
    #crear contraseña con requerimientos solicitados, mayusculas, minusculas y numeros
    password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=8))
    print(f"La contraseña de {usuario} es: {password}")
    #solicitar numero telefonico con al menos 8 digitos
    while True:
        numero = input(f"Ingrese el numero telefonico de {usuario}: ")
        if numero.isdigit() and len(numero) == 8:
            break