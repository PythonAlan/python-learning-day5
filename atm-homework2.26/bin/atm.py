#!/usr/bin/env python3
#antuor:Alan

import os,sys
base_dir = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))
print(base_dir)
sys.path.append(base_dir)
print(sys.path)
from core import main
if __name__=="__main__":
    main.run()