"""This is a module that creates a simple Tkinter launcher for testing menu --> level / level --> level loading. Using Tkinter here saves time for implementing separate control schemes etc. The final version might be just using the pygame library though."""

from config import *

if True:
    launcher = config.classes.Launcher()
    launcher.frame.pack()
    launcher.button_1.pack()
    launcher.button_2.pack()
    # launcher.root.mainloop()
