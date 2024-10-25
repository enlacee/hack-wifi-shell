import time
import pywifi
from pywifi import const

def connect_to_wifi(ssid, password):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Selecciona la primera interfaz de red inalámbrica disponible

    # Desconectar de cualquier red actual
    iface.disconnect()
    time.sleep(1)  # Espera a que se complete la desconexión

    # Crear perfil de conexión WiFi
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.key = password
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP


    # Agregar y conectar usando el perfil
    iface.remove_all_network_profiles()  # Limpia perfiles previos para evitar conflictos
    temp_profile = iface.add_network_profile(profile)

    # Intentar conectar
    iface.connect(temp_profile)
    connected = False
    for _ in range(10):  # Aumenta a 15 segundos el tiempo de espera
        print("status: ", iface.status())
        if iface.status() == const.IFACE_CONNECTED:
            connected = True
            break
        time.sleep(1)

    # Comprobar estado final de la conexión
    if not connected:
        print("No se pudo conectar a la red.")
        iface.disconnect()
    else:
        print("Conectado exitosamente a la red.")

    return connected

def main():
    words_array= ["123456", "123456789"]
    selected_ssid="MOVISTAR_A141_INVITADO"
    indicator= False
    try:
        for password in words_array:
            print("====")
            print("Acces to WIFI: ", selected_ssid, "  === password: ", password)
            if connect_to_wifi(selected_ssid , password):
                indicator = True
                break
        if (indicator == True):
            print("WiFi Status", "Connected to WiFi successfully!")
        else:
            print("WiFi Status", "Failed to connect to WiFi.")
    except NameError:
        print("WiFi Status", "No file selected.")


# Scan all networks
# usefulll simple view for see all near networks
def scan():
    print("print scan init")
    # Inicializar la interfaz de red
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Seleccionar la primera interfaz Wi-Fi

    # Iniciar el escaneo
    iface.scan()
    results = iface.scan_results()

    # Mostrar las redes encontradas
    for network in results:
        print(f"SSID: {network.ssid}, Signal: {network.signal}")


if __name__ == "__main__":
    scan()
    main()
