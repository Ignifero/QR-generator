#!usr/bin/env python
"""
Script para generar códigos qr con el módulo qrcode.

Es necesario instalar los módulos qrcode y pillow para poder ejecutar este script.

pip install qrcode
pip install pillow

"""

# Importación de los módulos que se usarán.
import qrcode
import os
import sys

def limpiar_consola():
  """
  Esta función sirve solo para limpiar la consola al momento de
  interactuar. Dependiendo del sistema operativo, limpiará la 
  pantalla con un comando usando os.
  """

  sistema_operativo = sys.platform.lower

  if sistema_operativo == 'linux':
    return os.system('clear')
  elif sistema_operativo == 'windows':
    return os.system('cls')

def pausa():
  """
  Esta función simula una pausa en la ejecución del script para mejorar
  la interacción.
  """

  sistema_operativo = sys.platform.lower

  if sistema_operativo == 'windows':
    return os.system('pause')
  else:
    input('\nPulsa "Enter" para continuar... ')

limpiar_consola()

print('=================================================================')
print('=================================================================')
print('   ______       ________')
print(' /        \    |    _   \'')
print('|    / \   |   |   |_|   |')
print('|   |   |  |   |       \_|')
print('|    \_/\ \|   |   |\   \'')
print(' \ ______\  \  |___| \___\ Generator')
print('          \__\'')
print('=================================================================')
print('=================================================================')
print()
print()
link = input('Ingresa el texto o link o teléfono que quieres en QR >>: ')

# Se crea el QR con este método
qr = qrcode.make(link)

nombre = input('\nIndica el nombre del archivo >>: ')

# Se salva
qr.save(f'{nombre}.png')

print('\n' + 'QR generado. Hasta pronto!')

pausa()
