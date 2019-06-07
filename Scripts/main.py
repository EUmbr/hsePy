import sys
import os

workDir = "D:\\Work\\"
try:
    sys.path.insert(0, workDir+"Library")
    from app import SampleApp
except:
    workDir = "..\\"
    sys.path.insert(0, workDir+"Library")
    from app import SampleApp

os.chdir(workDir)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
