import re
import os
from colorama import init, Fore

init()
init(autoreset=True)

# LOGS = '/var/log/wifidaetsam.log'
LOGS = 'wifidaetsam.log'
LOGS_1 = 'logs.txt'
p = re.compile(u'.*(AUTH: RADIUS).*')
with open(LOGS, 'r') as f:
    logs = f.read()

logs = logs.splitlines()


def access_colored(access_type):
    if access_type in 'accepted.':
        access_accepted = Fore.GREEN + access_type + Fore.RESET
        return access_accepted

    elif access_type in 'denied.':
        access_denied = Fore.RED + access_type + Fore.RESET
        return access_denied
    else:
        return access_type


for log in logs:

    if re.search(p, log):
        string = log.split()
        type_access = log.split()[13]

        first = ' '.join(string[0:13]) + ' '
        kind_access = access_colored(type_access)
        user_id = ' '.join(string[14:])
        print(first + str(kind_access) + user_id)