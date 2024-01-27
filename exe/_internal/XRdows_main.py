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
    pygame
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
        self.music = 0

        P_T()
    
    def sleep(self, music_file):
        self.music_file = music_file
        self.music_file_len_ = int(music_file.get_length()) + 1
        self.start = time.time()
        while 1:
            self.now = time.time()
            if int(self.now - self.start) <= self.music_file_len_:
                # print(int(now - start), music_file_len_)
                if self.mode == 'F_D':
                    self.XRdows_F_D()
                elif self.mode == 'T_D':
                    self.XRdows_T_D()
            else:
                raise RuntimeWarning()
    def play_music(self, file_path = '', file_list = [], mode = 'F_D'):
        self.mode = mode
        self.file_path = file_path
        self.file_list = file_list
        if self.music >= 1:
            self.music = 0
            self.music_file.stop()
        try:
            pygame.init()
            pygame.mixer.init()
            if self.file_list != []:
                try:
                    self.music += 1
                    self.next_music = ''.join(file_list.pop(0))
                    # print(next_music)
                    
                    #pygame.mixer.Sound.load(next_music)
                    self.music_file = pygame.mixer.Sound(self.next_music)
                    self.music_file.play()
                    self.sleep(self.music_file)
                except IndexError:
                    return
            elif self.file_path != '':
                self.music += 1
                self.music_file = pygame.mixer.Sound(os.path.join(file_path))
                self.music_file.play()
                self.sleep(self.music_file)
                return
        except:
            return

    def XRdows_F_D(self):

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
                    self.XRdows_T_D()
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
                M_P(self, 'F_D')
            elif command == 'R_py_F':
                R_py_F()
            elif command == 'R_exe_F':
                R_exe_F()
            elif command == 'M_P_D':
                folder_path = os.path.join(folder, './music_file')
                print(' > The file name format is \'music_{i(1 start)}_{name}\'')
                file_list_ = []
                i = 0
                for filename in os.listdir(folder_path):
                    i += 1
                    if f'music_{i}_' in filename:
                        temp = ''.join(filename)
                        list_temp_ = temp.split('music')
                        if list_temp_[0] == '':
                            if os.path.isfile(os.path.join(folder_path, filename)):
                                file_list_.append([os.path.join(folder_path+'/'+filename)])
                                with open(os.path.join(folder_path, filename), 'r', encoding='UTF-8') as file:
                                    file_name = ''.join(file.name)
                                    list_ = file_name.split('.')
                                    list_len_ = len(list_) - 1
                                    if list_[list_len_] == 'mp3' or list_[list_len_] == 'flac':
                                        self.play_music(file_list=file_list_, mode='F_D')
                                    else:
                                        print(f' > This file ({filename}) is not playable (mp3 or flac file suffix required)')
                        else:
                            print(' > The file name is formatted incorrectly')
            else:
                time.sleep(0.5)
                print(f' > No "{command}"')

    def XRdows_T_D(self):

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
                self.XRdows_F_D()
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
                M_P(self, 'T_D')
            elif command == 'R_py_F':
                R_py_F()
            elif command == 'R_exe_F':
                R_exe_F()
            elif command == 'M_P_D':
                folder_path = os.path.join(folder, './music_file')
                print(' > The file name format is \'music{name}\'')
                file_list_ = []
                for filename in os.listdir(folder_path):
                    if 'music' in filename:
                        temp = ''.join(filename)
                        list_temp_ = temp.split('music')
                        if list_temp_[0] == '':
                            if os.path.isfile(os.path.join(folder_path, filename)):
                                file_list_.append([filename])
                                with open(os.path.join(folder_path, filename), 'r', encoding='UTF-8') as file:
                                    file_name = ''.join(file.name)
                                    list_ = file_name.split('.')
                                    list_len_ = len(list_) - 1
                                    if list_[list_len_] == 'mp3' or list_[list_len_] == 'flac':
                                        self.play_music(file_list=file_list_, mode='T_D')
                                    else:
                                        print(f' > This file ({filename}) is not playable (mp3 or flac file suffix required)')
                        else:
                            print(' > The file name is formatted incorrectly')
            else:
                time.sleep(0.5)
                print(f' > No "{command}"')

XRdows_T = __XRdows_total__()

if __name__ == '__main__':
    XRdows_T.XRdows_F_D()
