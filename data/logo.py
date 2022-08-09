import sys, os, random

#---- MODULE RICH IN PYTHON -------
from rich import print as prints
from rich.panel import Panel
biru_m = '[bold cyan]'
hapus  = '[/]'


class Logo:

    def __init__(self):
        if "linux" in sys.platform.lower():
            try:os.system("clear")
            except:pass
        elif "win" in sys.platform.lower():
            try:os.system("cls")
            except:pass
        else:
            try:os.system("clear")
            except:pass

    def log(self):
        WAR = random.choice(["[deep_pink3]","[green]","[cyan]","[blue]"])
        prints(Panel(f"""{WAR}             
██    ██ ███    ██ ██  ██████  ██    ██ ███████     
██    ██ ████   ██ ██ ██    ██ ██    ██ ██          
██    ██ ██ ██  ██ ██ ██    ██ ██    ██ █████       
██    ██ ██  ██ ██ ██ ██ ▄▄ ██ ██    ██ ██          
 ██████  ██   ████ ██  ██████   ██████  ███████ {WAR}version: 0.5[/]     
                          ▀▀                                                                                                                                                                thanks to yayan-xd"""))
