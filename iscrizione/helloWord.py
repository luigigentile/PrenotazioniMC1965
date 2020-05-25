import os
from pathlib import Path
import subprocess

class Prova():



    def __init__(self, name):
        self.name = name

    def stampaName(self):
        current_dir = str(Path(__file__).resolve().parent.parent.parent)
        current_file = current_dir +"/power.py"
#        print(current_file)
        print(f"il  mio nome e {self.name}")
        return self.name

##    print(f"sto eseguendo il modulo prova argomento passato {name}")
