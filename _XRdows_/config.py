import yaml
import os
from consts import (
    folder
)

class config_t():
    def __init__(self):
        with open(os.path.join(folder, './config/config.yaml'), 'r') as f:
            self.configs = yaml.safe_load(f)
        # self.XRthon()
    
    def XRthon(self):
        if 'XRthon' in self.configs:
            if self.configs['XRthon'] == True:
                XRthon_F_isexists = os.path.exists(os.path.join(folder, './front_file/XRthon_front_file/_XRthon_/main.py'))
                if XRthon_F_isexists == True:
                    from front_file.XRthon_front_file._XRthon_.main import mains
                    mains()
                elif XRthon_F_isexists == False:
                    print(' > The prefix file (XRthon) file does not exist')
            elif self.configs['XRthon'] == False:
                print(' > You don\'t have XRthon enabled')
            else:
                print(' > The XRthon value must be True or False')
        else:
            print(' > The XRthon key does not exist')
    
    def get_configs(self):
        return self.configs

config = config_t()
