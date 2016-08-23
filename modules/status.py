# Import modules
import subprocess
import ipaddress
from colorama import init, Fore

init()

all_hosts = {
    'DAETSAM-04': '138.100.43.91',
    'DAETSAM-05': '138.100.43.95',
    'DAETSAM-06': '138.100.43.96',
    'MOSTRADOR-01': '138.100.43.92',
    'MOSTRADOR-02': '138.100.43.93',
    'AD-SERVER': '138.100.43.246',
    'BACKUP-SERVER': '138.100.43.158',
    'DEV-SERVER': '138.100.43.240',
    'WEB': 'daetsam.aq.upm.es',
    'WIFI': '138.100.43.159'
}

info = subprocess.STARTUPINFO()
info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = subprocess.SW_HIDE

def status_colored(access_type):
    if access_type in 'Online.':
        access_accepted = Fore.GREEN + access_type + Fore.RESET
        return access_accepted

    elif access_type in 'Offline.':
        access_denied = Fore.RED + access_type + Fore.RESET
        return access_denied
    else:
        return access_type


for key, value in all_hosts.items():
    output = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(all_hosts[key])], stdout=subprocess.PIPE,
                              startupinfo=info).communicate()[0]

    if "La solicitud de ping no pudo encontrar" in str(output):
        print(key, value, status_colored('Offline'))

    elif "Tiempo de espera agotado para esta solicitud." in str(output):
        print(key, value, status_colored('Offline'))

    else:
        print(key, value, status_colored('Online'))

