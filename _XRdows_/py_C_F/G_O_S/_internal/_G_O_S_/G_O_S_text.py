import os
import pathlib
# from unicode import unicode

folder = pathlib.Path(__file__).parent.resolve()

with open(os.path.join(folder, './py_C_F/all_text/caption.txt'), 'r', encoding='UTF-8') as file:
    caption = f'{file.read()}'

with open(os.path.join(folder, './py_C_F/all_text/concerning.txt'), 'r', encoding='UTF-8') as file:
    concerning = f'{file.read()}'

with open(os.path.join(folder, './py_C_F/all_text/concerning_content_1.txt'), 'r', encoding='UTF-8') as file:
    concerning_content_1 = f'{file.read()}'

with open(os.path.join(folder, './py_C_F/all_text/concerning_content_2.txt'), 'r', encoding='UTF-8') as file:
    concerning_content_2 = f'{file.read()}'

if __name__ == '__main__':
    print(f'{caption}\n{concerning}\n{concerning_content_1}\n{concerning_content_2}')
