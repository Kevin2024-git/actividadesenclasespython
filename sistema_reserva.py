# sistema_reservas.py

# Lista global para almacenar los usuarios registrados
usuarios = []

# Lista global para almacenar las reservas
reservas = []

# Función para registrar un nuevo usuario
def registrar_usuario():
    nombre_usuario = input("Ingresa tu nombre de usuario: ").strip()
    
    # Verificar si el nombre de usuario ya existe
    if nombre_usuario in usuarios:
        print("El nombre de usuario ya está registrado. Intenta con otro.")
    else:
        usuarios.append(nombre_usuario)
        print(f"Usuario '{nombre_usuario}' registrado exitosamente.")

# Función para reservar un viaje
def reservar_viaje():
    nombre_usuario = input("Ingresa tu nombre de usuario: ").strip()
    
    # Verificar si el usuario está registrado
    if nombre_usuario not in usuarios:
        print("Usuario no registrado. Por favor, regístrate primero.")
        registrar_usuario()
    
    destino = input("Ingresa el destino del viaje: ").strip()
    fecha = input("Ingresa la fecha del viaje (DD/MM/AAAA): ").strip()
    
    reserva = {
        'usuario': nombre_usuario,
        'destino': destino,
        'fecha': fecha
    }
    
    reservas.append(reserva)
    print("Reserva realizada exitosamente.")

# Función para ver las reservas de un usuario
def ver_reservas():
    nombre_usuario = input("Ingresa tu nombre de usuario: ").strip()
    
    # Filtrar las reservas del usuario
    reservas_usuario = [reserva for reserva in reservas if reserva['usuario'] == nombre_usuario]
    
    if reservas_usuario:
        print(f"Reservas de {nombre_usuario}:")
        for i, reserva in enumerate(reservas_usuario, start=1):
            print(f"{i}. Destino: {reserva['destino']}, Fecha: {reserva['fecha']}")
    else:
        print("No tienes reservas.")

# Función para cancelar una reserva
def cancelar_reserva():
    nombre_usuario = input("Ingresa tu nombre de usuario: ").strip()
    
    # Filtrar las reservas del usuario
    reservas_usuario = [reserva for reserva in reservas if reserva['usuario'] == nombre_usuario]
    
    if reservas_usuario:
        print(f"Reservas de {nombre_usuario}:")
        for i, reserva in enumerate(reservas_usuario, start=1):
            print(f"{i}. Destino: {reserva['destino']}, Fecha: {reserva['fecha']}")
        
        # Seleccionar la reserva a cancelar
        try:
            seleccion = int(input("Selecciona el número de la reserva que deseas cancelar: ")) - 1
            reserva_a_cancelar = reservas_usuario[seleccion]
            reservas.remove(reserva_a_cancelar)
            print("Reserva cancelada exitosamente.")
        except (IndexError, ValueError):
            print("Selección inválida.")
    else:
        print("No tienes reservas para cancelar.")

# Función principal que maneja el menú del sistema
def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar un usuario")
        print("2. Reservar un viaje")
        print("3. Ver reservas")
        print("4. Cancelar una reserva")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            reservar_viaje()
        elif opcion == '3':
            ver_reservas()
        elif opcion == '4':
            cancelar_reserva()
        elif opcion == '5':
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

# Ejecutar el menú principal al iniciar el programa
if __name__ == "__main__":
    menu_principal()
