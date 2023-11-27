import time
import os
import sys
import subprocess
import shutil
from XRdows_text import XRdows, Edition_logs, command_table
from Login_Data import L_D
import zipfile
from consts import folder

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
    print(' > Version : 0.9 beta')
    time.sleep(0.5)
    print(' > by : ' + "'" + '是星星与然然呀' + "'")

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
    L_D()

def C_L():
    os.remove(os.path.join(folder, './py_C_F/Login_Data/Login_Data.py'))
    shutil.rmtree(os.path.join(folder, './py_C_F/Login_Data/__pycache__'))
    time.sleep(0.5)
    print(' > Login canceled')

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

if __name__ == '__main__':
    P_T()
    E_L()
