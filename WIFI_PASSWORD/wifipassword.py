import subprocess

WIFI_NAMES = subprocess.check_output('netsh wlan show profiles').decode('utf-8')
WIFI_NAMES_OUTPUT = WIFI_NAMES.splitlines()
for line in WIFI_NAMES_OUTPUT:
    if("All User Profile" in line):
        WIFI_NAME=line.split(":")[1][1:]
        output= subprocess.check_output('netsh wlan show profile name="'+WIFI_NAME+'" key=clear').decode('utf-8')
        WIFI_PASSWORDS_OUPUT=output.splitlines()
        for wifi_password in WIFI_PASSWORDS_OUPUT:
            if("Key Content" in wifi_password):
                print(WIFI_NAME+" : "+wifi_password.split(":")[1][1:])