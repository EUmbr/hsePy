"""
Главная программа для запуска приложения
Автор: Умбрас Е.Д. БИВ182
"""
import sys
import os

WORK_DIR = "D:\\Work\\"
try:
    sys.path.insert(0, WORK_DIR+"Library")
    from app import SampleApp
except:
    WORK_DIR = "..\\"
    sys.path.insert(0, WORK_DIR+"Library")
    from app import SampleApp

os.chdir(WORK_DIR)

if __name__ == "__main__":
    APP = SampleApp()
    APP.mainloop()
