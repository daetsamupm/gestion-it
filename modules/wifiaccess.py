import re
from PyQt5.QtWidgets import QTableWidgetItem
import os
from settings import PATH_MODULES
path = os.path.dirname(os.path.realpath('wifi.py'))
LOGS = os.path.join(PATH_MODULES, "wifidaetsam.log")

p = re.compile(u'.*(AUTH: RADIUS).*')

with open(LOGS, 'r') as f:
    logs = f.read()

logs = logs.splitlines()


def vaciar_tabla(tabla):
    for fila in range(tabla.rowCount()):
        tabla.removeRow(fila)

# TODO: Mejorar la logica de negocios de la parte de comprobaciones y de generar tabla
def get_logs(tabla):
    for log in logs:
        if re.search(p, log):
            string = log.split()
            fecha = ' '.join(string[0:3])

            analisis_acceso = string[12]

            if analisis_acceso in 'Access':
                tipo_acceso = string[13]
                if tipo_acceso in 'accepted.':
                    tipo_acceso = 'VALIDO'
                    informacion_usuario = ' '.join(string[14:15]).replace('(', "").replace(',', "")
                else:
                    tipo_acceso = 'DENEGADO'
                    informacion_usuario = ' '.join(string[19:20]).replace('(', "").replace(',', "")
            elif analisis_acceso in 'No':
                informacion_usuario = ''.join(string[16]).replace("(", '')
                tipo_acceso = 'INVALIDO'

            rowPosition = tabla.rowCount()
            tabla.insertRow(rowPosition)
            tabla.setItem(rowPosition, 0, QTableWidgetItem(fecha))
            tabla.setItem(rowPosition, 1, QTableWidgetItem(tipo_acceso))
            tabla.setItem(rowPosition, 2, QTableWidgetItem(informacion_usuario))
