import ctypes

ctypes.windll.kernel32.SetConsoleTitleW('XRdows')

import webbrowser
import shutil
from XRdows_text import command_table
# from setup import Deve_mode
from S_D import (
    P_T,
    E_P,
    P_W,
    E_L,
    C_T,
    C_Z,
    hex_to_str,
    M_P,
    R_py_F,
    R_exe_F,
    play_music
)
from consts import (
    folder,
    _1_E,
    _2_E,
    _3_E,
    _5_E,
    _6_E,
    _7_E,
    _8_E,
    _9_E,
    _10_E,
    _11_E,
    _12_E,
    _13_E
)
import time
import os

pycache = os.path.join(folder, './__pycache__')

if os.path.exists(pycache):
    shutil.rmtree(pycache)

class __XRdows_total__():
    def __init__(self):

        P_T()

    def XRdows_N_D(self):

        running = True

        # webbrowser.open(os.path.join(folder, './py_C_F/introduce/introduce.html'))

        while running:
            time.sleep(0.5)
            command = input(f'{_1_E}')
            if command == 'C_T':
                C_T()
            elif command == 'P_W':
                print(f'{_2_E}')
                P_W()
                print(f'{_3_E}')
                time.sleep(0.5)
            elif command == '_EXIT':
                E_P()
                time.sleep(1)
                running = False
            elif command == ':wq':
                E_P()
                time.sleep(1)
                running = False
                '''
            elif command == '_C_L':
                C_L()
    '''
            elif command == '_E_L':
                E_L()
            elif command == '_I_H_':
                webbrowser.open(os.path.join(folder, './py_C_F/html/introduce.html'))
                time.sleep(1)
            elif command == 'Deve_mode_True':
                time.sleep(1)
                Deve_pw = input(f'{_8_E}')
                D_P_W = hex_to_str(hex_to_str('353835323331333233333334333537373661373337383738'))
                if Deve_pw == D_P_W:
                    print(f'{_9_E}')
                    running = False
                    XRdows_T.XRdows_D()
                else:
                    time.sleep(1)
                    print(f'{_10_E}')
            elif command == '__mode__':
                time.sleep(1)
                print(F' > Deve_mode is False')
            elif command == 'print()':
                content = input(f'{_13_E}')
                print(f' > {content}')
            elif command == 'M_P':
                M_P()
            elif command == 'R_py_F':
                R_py_F()
            elif command == 'R_exe_F':
                R_exe_F()
            elif command == 'M_P_D':
                folder_path = os.path.join(folder, './music_file')
                print(' > The file name format is \'music{name}\'')
                for filename in os.listdir(folder_path):
                    if 'music' in filename:
                        temp = ''.join(filename)
                        list_temp_ = temp.split('music')
                        if list_temp_[0] == '':
                            if os.path.isfile(os.path.join(folder_path, filename)):
                                with open(os.path.join(folder_path, filename), 'r', encoding='UTF-8') as file:
                                    file_name = ''.join(file.name)
                                    list_ = file_name.split('.')
                                    list_len_ = len(list_) - 1
                                    if list_[list_len_] == 'mp3' or list_[list_len_] == 'flac':
                                        play_music(file.name)
                                    else:
                                        print(f' > This file ({filename}) is not playable (mp3 or flac file suffix required)')
                        else:
                            print(' > The file name is formatted incorrectly')
            else:
                time.sleep(0.5)
                print(f' > No "{command}"')

    def XRdows_D(self):

        running = True

        while running:
            time.sleep(0.5)
            command = input(f'{_1_E}')
            if command == 'C_T':
                C_T()
            elif command == 'P_W':
                print(f'{_2_E}')
                P_W()
                print(f'{_3_E}')
                time.sleep(0.5)
            elif command == '_EXIT':
                E_P()
                time.sleep(1)
                running = False
            elif command == ':wq':
                E_P()
                time.sleep(1)
                running = False
                '''
            elif command == '_C_L':
                C_L()
    '''
            elif command == '_E_L':
                E_L()
            elif command == '_I_H_':
                webbrowser.open(os.path.join(folder, './py_C_F/html/introduce.html'))
                time.sleep(1)
            elif command == 'Deve_mode_False':
                running = False
                XRdows_T.XRdows_N_D()
            elif command == 'C_F':
                try:
                    time.sleep(0.5)
                    C_F_P = input(f'{_5_E}')
                    path = os.path.join(C_F_P)
                    with open(path, 'w') as file:
                        time.sleep(0.5)
                        D_C = input(f'{_6_E}')
                        file.write(D_C)
                except:
                    time.sleep(1)
                    print(f'{_7_E}')
            elif command == '__code__':
                try:
                    path = os.path.join(folder, input(f'{_11_E}'))
                    C_Z(os.path.join(folder), path + '\\code.CODE')
                except:
                    time.sleep(1)
                    print(f'{_7_E}')
            elif command == '__mode__':
                time.sleep(1)
                print(f' > Deve_mode is True')
            elif command == '__Self_destruction__':
                time.sleep(1)
                print(f'{_12_E}')
                try:
                    time.sleep(1)
                    path = os.path.join(folder, input(f'{_11_E}'))
                    C_Z(os.path.join(folder), path + '\\code.CODE')
                except:
                    time.sleep(1)
                    print(f'{_7_E}')
                time.sleep(1)
                # shutil.rmtree(os.path.join(folder, './__pycache__'))
                # shutil.rmtree(os.path.join(folder, './py_C_F'))
                # os.remove(os.path.join(folder, './consts.py')) 
                # os.remove(os.path.join(folder, './Login_Data.py'))
                os.remove(os.path.join(folder, './S_D.py'))
                # os.remove(os.path.join(folder, './setup.py'))
                os.remove(os.path.join(folder, './XRdows_text.py'))
            elif command == 'print()':
                content = input(f'{_13_E}')
                print(f' > {content}')
            elif command == 'M_P':
                M_P()
            elif command == 'R_py_F':
                R_py_F()
            elif command == 'R_exe_F':
                R_exe_F()
            elif command == 'M_P_D':
                folder_path = os.path.join(folder, './music_file')
                print(' > The file name format is \'music{name}\'')
                for filename in os.listdir(folder_path):
                    if 'music' in filename:
                        temp = ''.join(filename)
                        list_temp_ = temp.split('music')
                        if list_temp_[0] == '':
                            if os.path.isfile(os.path.join(folder_path, filename)):
                                with open(os.path.join(folder_path, filename), 'r', encoding='UTF-8') as file:
                                    file_name = ''.join(file.name)
                                    list_ = file_name.split('.')
                                    list_len_ = len(list_) - 1
                                    if list_[list_len_] == 'mp3' or list_[list_len_] == 'flac':
                                        play_music(file.name)
                                    else:
                                        print(f' > This file ({filename}) is not playable (mp3 or flac file suffix required)')
                        else:
                            print(' > The file name is formatted incorrectly')
            else:
                time.sleep(0.5)
                print(f' > No "{command}"')

XRdows_T = __XRdows_total__()

if __name__ == '__main__':
    XRdows_T.XRdows_N_D()
