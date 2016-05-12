from Tkinter import *
from PIL import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()
        self.input = Image.open("happy_baton.png")
        self.image = ImageTk.PhotoImage(self.input)

        self.button = Button(
            frame, image=self.image, fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "hi there, everyone!"

root = Tk()

app = App(root)

root.mainloop()
