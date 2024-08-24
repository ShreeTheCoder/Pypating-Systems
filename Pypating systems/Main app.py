import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import subprocess

def cli_os_func():
    subprocess.run(["python", "CLI OS\\boot.py"])


window = ttk.Window()

cli_os = ttk.Button(window,
                    text="CLI OS",
                    bootstyle=DANGER,
                    command=cli_os_func)

cli_os.place(x=0, y=0)

window.mainloop()
