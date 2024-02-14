import os
from consts import (
    folder,
    configs
)

def XRthon():
    if 'XRthon' in configs:
        if configs['XRthon'] == True:
            XRthon_F_isexists = os.path.exists(os.path.join(folder, './mods_file/XRthon_mods_file/_XRthon_/main.py'))
            if XRthon_F_isexists == True:
                from mods_file.XRthon_mods_file._XRthon_.main import mains
                mains()
            elif XRthon_F_isexists == False:
                print(' > The mods file (XRthon) file does not exist')
        elif configs['XRthon'] == False:
            print(' > You don\'t have XRthon enabled')
        else:
            print(' > The XRthon value must be True or False')
    else:
        print(' > The XRthon key does not exist')