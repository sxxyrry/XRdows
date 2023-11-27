import ctypes

# 设定控制台标题为“XRdows”
ctypes.windll.kernel32.SetConsoleTitleW('XRdows')

# 导入
from XRdows_text import command_table
from setup import Deve_mode
from S_D import (
    P_T,
    E_P,
    C_L,
    P_W,
    E_L,
    C_T,
    C_Z,
    hex_to_str
)
from consts import (
    folder,
    _1_E,
    _2_E,
    _3_E,
    _4_E,
    _5_E,
    _6_E,
    _7_E,
    _8_E,
    _9_E,
    _10_E
)
import time
import os

# 主函数
def XRdows():

    running = True

    P_T()

    # 循环
    while running:
        time.sleep(0.5)
        command = input(f'{_1_E}')
        if Deve_mode == True:
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
            elif command == '_C_L':
                C_L()
            elif command == '_E_L':
                E_L()
            elif command == 'Deve_mode_False':
                with open(os.path.join(folder, './py_C_F/setup/deve_mode.py'), 'w') as file:
                    file.write('''Deve_mode = False''')
                time.sleep(1)
                print(f'{_4_E}')
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
                    path = os.path.join(folder, input(' > Please enter the path where the code is stored >>>'))
                    C_Z(os.path.join(folder), path + '\\code.CODE')
                except:
                    time.sleep(1)
                    print(f'{_7_E}')
            elif command == '__mode__':
                time.sleep(1)
                print(F' > Deve_mode is {Deve_mode}')
            else:
                time.sleep(0.5)
                print(f' > No "{command}"')
        else:
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
            elif command == '_C_L':
                C_L()
            elif command == '_E_L':
                E_L()
            elif command == 'Deve_mode_True':
                time.sleep(1)
                Deve_pw = input(f'{_8_E}')
                D_P_W = hex_to_str('58523132333435776a737878')
                if Deve_pw == D_P_W:
                    print(f'{_9_E}')
                    with open(os.path.join(folder, './py_C_F/setup/deve_mode.py'), 'w') as file:
                        file.write('''Deve_mode = True''')
                else:
                    time.sleep(1)
                    print(f'{_10_E}')
            elif command == '__mode__':
                time.sleep(1)
                print(F' > Deve_mode is {Deve_mode}')
            else:
                time.sleep(0.5)
                print(f' > No "{command}"')

if __name__ == '__main__':
    # 主函数调用
    XRdows()
