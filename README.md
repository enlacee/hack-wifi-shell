# test/hack WIFI

Tool: discover WIFI with easy password

## Bash script `test_wifi.sh`

set the right permission in this case execution:

    chmod +x test_wifi.sh
    ./test_wifi

## Python script (`index.py`)

is not working, but it's useful to understand the use and
communication of WIFI inside

### create project

    python -m venv venv
    source ./venv/bin/active
    pip install -r requirements.txt

### Execute the command start app
Execute the next command 
You need to execute usend venviroment python with `sudo` because
We need to access to networksFiles just have access by root it's for security

    Permission denied: '/var/run/wpa_supplicant'

You have to execute this script for not change the permission of the files `we need to run with sudo`

    sudo ./venv/bin/python index.py 



### Error: bug:

A some wifi module not retun the true connection and for them
i cant know when the password is correct! in this script
the code that not working like i want it it: `index.py`

    if iface.status() == const.IFACE_CONNECTED:


