usuarios = [
    {"nombre": "Juan", "apellido": "Pérez", "documento": "123456789", "direccion": "Calle 1", "telefono": "3001234567", "entidad": "Independiente", "usuario": "juan123", "contraseña": "1234", "saldo": 500000},
    {"nombre": "Ana", "apellido": "Gómez", "documento": "987654321", "direccion": "Calle 2", "telefono": "3007654321", "entidad": "Banco X", "usuario": "ana456", "contraseña": "5678", "saldo": 300000},
    {"nombre": "Carlos", "apellido": "López", "documento": "111223344", "direccion": "Calle 3", "telefono": "3012345678", "entidad": "Banco Y", "usuario": "carlos789", "contraseña": "0001", "saldo": 1000000},
    {"nombre": "Laura", "apellido": "Martínez", "documento": "555443322", "direccion": "Calle 4", "telefono": "3018765432", "entidad": "Independiente", "usuario": "laura999", "contraseña": "4321", "saldo": 250000},
    {"nombre": "Miguel", "apellido": "Sánchez", "documento": "223344556", "direccion": "Calle 5", "telefono": "3009876543", "entidad": "Banco X", "usuario": "miguel100", "contraseña": "5670", "saldo": 150000},
    {"nombre": "María", "apellido": "Rodríguez", "documento": "776655443", "direccion": "Calle 6", "telefono": "3006543210", "entidad": "Banco Y", "usuario": "maria111", "contraseña": "9876", "saldo": 200000},
    {"nombre": "José", "apellido": "García", "documento": "333444555", "direccion": "Calle 7", "telefono": "3012347654", "entidad": "Independiente", "usuario": "jose333", "contraseña": "1357", "saldo": 800000},
    {"nombre": "Elena", "apellido": "Vega", "documento": "888999000", "direccion": "Calle 8", "telefono": "3018765432", "entidad": "Banco X", "usuario": "elena222", "contraseña": "2468", "saldo": 450000},
    {"nombre": "Luis", "apellido": "Torres", "documento": "444555666", "direccion": "Calle 9", "telefono": "3005678901", "entidad": "Banco Y", "usuario": "luis444", "contraseña": "1112", "saldo": 350000},
    {"nombre": "Pedro", "apellido": "Álvarez", "documento": "999000111", "direccion": "Calle 10", "telefono": "3011234567", "entidad": "Independiente", "usuario": "pedro555", "contraseña": "2222", "saldo": 600000},
]

def autenticar_usuario():
    intentos = 0
    while intentos < 3:
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        for user in usuarios:
            if user["usuario"] == usuario and user["contraseña"] == contraseña:
                return user  
        intentos += 1
        print(f"Error en las credenciales. Intentos restantes: {3 - intentos}")
    
    print("Demasiados intentos fallidos. Se cobrará un rubro a su cuenta.")
    for user in usuarios:
        if user["usuario"] == usuario:
            user["saldo"] -= 5000
            print(f"Se han descontado 5000 de su cuenta. Saldo actual: {user['saldo']}")
    return None

def realizar_retiro(usuario):
    print("Opciones de retiro: 10,000; 20,000; 50,000; Otro")
    retiro = input("¿Cuánto desea retirar?: ")

    if retiro == "Otro":
        monto = int(input("Ingrese el monto a retirar (mínimo 10,000 y múltiplo de 10): "))
        if monto < 10000 or monto % 10 != 0:
            print("Monto no válido. El retiro debe ser mayor a 10,000 y múltiplo de 10.")
            return
    else:
        monto = int(retiro)

    if usuario["saldo"] >= monto:
        billetes = {50000: 0, 20000: 0, 10000: 0}
        for billete in billetes.keys():
            if monto >= billete:
                billetes[billete] = monto // billete
                monto = monto % billete
        if monto == 0:
            confirmacion = input(f"Usted va a retirar {usuario['saldo'] - monto}. ¿Desea continuar? (SI/NO): ")
            if confirmacion.lower() == "si":
                usuario["saldo"] -= monto
                print(f"Retiro exitoso. Su saldo actual es: {usuario['saldo']}")
        else:
            print("Monto inválido.")
    else:
        print("Saldo insuficiente.")
    

def realizar_transferencia(usuario):
    cantidad = float(input("¿Cuánto desea transferir?: "))
    if cantidad <= usuario["saldo"]:
        destinatario = input("Ingrese el nombre del destinatario: ")
        usuario["saldo"] -= cantidad
        print(f"Transferencia realizada a {destinatario}. Su saldo es ahora: {usuario['saldo']}")
    else:
        print("Saldo insuficiente para la transferencia.")

def banco():
    print("Bienvenido al Banco. Ingrese sus credenciales:")
    usuario = autenticar_usuario()

    if usuario is None:
        return

    while True:
        print("\nOperaciones disponibles:")
        print("1. Retiro")
        print("2. Transferencia")
        print("3. Pago de servicios públicos")
        print("4. Pago de impuestos")
        print("5. Adelanto de saldo")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            realizar_retiro(usuario)
        elif opcion == "2":
            realizar_transferencia(usuario)
        elif opcion == "3":
            print("Pago de servicios públicos no implementado aún.")
        elif opcion == "4":
            print("Pago de impuestos no implementado aún.")
        elif opcion == "5":
            print("Adelanto de saldo no implementado aún.")
        elif opcion == "6":
            print(f"Gracias por utilizar nuestros servicios. Su saldo final es: {usuario['saldo']}")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

banco()
