import random
import string

# define las letras a usar para la contraseña
letters = string.ascii_letters
digits = string.digits

alfabeto = letters + digits

usuarios = ['usuario1', 'usuario2', 'usuario3', 'usuario4', 'usuario5', 'usuario6', 'usuario7', 'usuario8', 'usuario9', 'usuario10']

cuentas = {}

def crear_cuenta(usuario):
    #crear contraseña con requerimientos solicitados, mayusculas, minusculas y numeros
    password = ''.join(random.choices(alfabeto, k=8))
    print(f"La contraseña de {usuario} es: {password}")
    #solicitar numero telefonico con al menos 8 digitos
    while True:
        numero = input(f"Ingrese el numero telefonico de {usuario}: ")
        if numero.isdigit() and len(numero) == 8:
            break
        else:
            print("El número telefónico debe tener 8 dígitos numéricos.")
        # Guardar cuenta y contraseña
    cuentas[usuario] = {'contraseña': password, 'telefono': numero}
    print(f"Cuenta creada para {usuario}.")
    
# Crear cuenta para cada usuario
for usuario in usuarios:
    crear_cuenta(usuario)
    
# Mostrar cuentas y contraseñas
print("Cuentas creadas:")
for usuario, datos in cuentas.items():
    print(f"Usuario: {usuario}, Contraseña: {datos['contraseña']}, Teléfono: {datos['telefono']}")