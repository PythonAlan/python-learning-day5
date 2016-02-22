#!/usr/bin/env python3
#antuor:Alan
import sys
import os
pre_path = os.path.abspath('/Users/Alan/desktop/Alanproject/day5/my_pj')
#设置环境变量，把该主目录添加到sys.path里.文件退出则无效，所以写死在这个主文件
sys.path.append(pre_path)
from backend.logic import view,handle

view.home()
view.movie()
handle.cal()

"""总逻辑：
1.frontend里的user_main调用logic中的view
2.logic里的view调用db中的sql_api(去数据库查数据）
3.sql_api再调用config里settings的DATABASE（依赖验证）
"""