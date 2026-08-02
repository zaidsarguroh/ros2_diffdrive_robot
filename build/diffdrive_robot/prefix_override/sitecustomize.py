import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/zaid/diffdrive_ws/src/diffdrive_robot/install/diffdrive_robot'
