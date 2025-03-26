import pywhatkit
import pyautogui
import time

# Variable para almacenar el tiempo del último mensaje enviado
last_sent_time = 0  
cooldown = 30  # Tiempo de espera en segundos

def send_smg(msg="🚭 Alerta: Se detectó a alguien fumando!", cel="70812048", mode="contacto"):
    global last_sent_time

    current_time = time.time()  
    if current_time - last_sent_time < cooldown:
        print(f"Espera {int(cooldown - (current_time - last_sent_time))} segundos antes de enviar otro mensaje.")
        return

    tel = f'+503{cel}'
    grupo = ''
    mensaje = msg

    if mode == 'contacto':
        pywhatkit.sendwhatmsg_instantly(tel, mensaje)  # Usa la sesión abierta
    elif mode == 'grupo':
        pywhatkit.sendwhatmsg_to_group_instantly(grupo, mensaje)

    time.sleep(3)  # Esperar a que el mensaje se escriba
    pyautogui.press("enter")  # Simular "Enter" para enviarlo
    print("Mensaje enviado con éxito")

    time.sleep(2)  # Esperar a que se cierre la ventana de WhatsApp
    pyautogui.hotkey('ctrl', 'w')  # Cerrar la ventana de WhatsApp

    last_sent_time = time.time()  # Actualizar el tiempo del último mensaje enviado
