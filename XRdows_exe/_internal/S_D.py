import time
import os
import sys
import subprocess
import shutil
import zipfile
import pygame
from XRdows_text import(
    XRdows,
    Edition_logs,
    command_table
)
# from Login_Data import L_D
from consts import (
    folder,
    _14_E,
    _15_E,
    _16_E,
    _17_E
)

def XRDOWS():
    time.sleep(0.5)
    print(f'{XRdows}')
    time.sleep(0.5)

def prompt():
    print(' > Processor/running interpreter : python')
    time.sleep(0.5)
    print(f' > python_version : {sys.version}')
    time.sleep(0.5)
    print(' > Program name : XRdows')
    time.sleep(0.5)
    print(' > by : \'是星星与然然呀\'')

'''
def G_O_S():
    subprocess.run(os.path.join(folder, './py_C_F/G_O_S/G_O_S.exe'))
'''

def E_L():
    time.sleep(0.5)
    print(f'{Edition_logs}')
    time.sleep(0.5)

def P_T():
    XRDOWS()
    prompt()
    # L_D()

def C_T():
    time.sleep(0.5)
    print(f'{command_table}')
    time.sleep(0.5)

def E_P():
    time.sleep(0.5)
    print(' > Is exiting')

def P_W():
    subprocess.run(os.path.join(folder, './py_C_F/P_W/plane_war_normal_edition.exe'))

def C_Z(source_folder, output_filename):
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), source_folder))

def hex_to_str(h):
    return ''.join([chr(int(h[i:i+2], 16)) for i in range(0, len(h), 2)])

def play_music(file_path):
    pygame.init()
    pygame.mixer.init()
    music_file = pygame.mixer.Sound(os.path.join(file_path))
    music_file.play()
    time.sleep(music_file.get_length())

def M_P():
    try:
        file_path = input(f'{_14_E}')
        play_music(file_path)
    except:
        print(f'{_15_E}')
        M_P()

def R_py_F():
    try:
        file_path = os.path.join(input(f'{_16_E}'))
        with open(file_path, 'r', encoding='UTF-8') as file:
            try:
                while 1:
                    exec(file.read())
                    break
            except Exception as error:
                print(f' > Error is {error}')
                R_py_F()
    except:
        print(f'{_15_E}')
        R_py_F()

def R_exe_F():
    try:
        file_path = input(f'{_17_E}')
        subprocess.run(file_path)
    except:
        print(f'{_15_E}')
        R_exe_F()

if __name__ == '__main__':
    P_T()
    E_L()
