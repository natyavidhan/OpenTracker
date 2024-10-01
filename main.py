import tkinter as tk
import json
from tkinter.constants import *

from consts import Fonts
from consts import Colors


class App:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.geometry("500x800")
        self.root.title("OpenTracker")
        self.root.resizable(False, False)
        self.root.configure(background=Colors.primary)

        self.settings = json.load(open("settings.json"))

        self.time = tk.StringVar(self.root, "00-00-0000 00:00 PM")
        self.timer_var = tk.StringVar(self.root, "00:00:00")

        self.clock = tk.Label(self.root, textvariable=self.time, font=Fonts._20, bg=Colors.primary, fg=Colors.text)
        self.clock.place(x=0, y=20, width=500, height=25)

        tk.Label(self.root, text="Total", font=Fonts._16, bg=Colors.primary, fg=Colors.text).place(x=232, y=65)

        self.grand_timer = tk.Label(self.root, textvariable=self.timer_var, font=Fonts._48, bg=Colors.primary, fg=Colors.text)
        self.grand_timer.place(x=0, y=100, width=500, height=55)

        self.tabs_frame = tk.Frame(self.root, width=450, height=500)
        self.tabs_frame.place(x=25, y=165)
        
            
        self.timer_canvas = tk.Canvas(self.tabs_frame)
        vbar=tk.Scrollbar(self.timer_canvas, orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=self.timer_canvas.yview)
        self.timer_canvas.config(yscrollcommand=vbar.set)
        self.timer_canvas.place(x=0, y=0, width=450, height=500)

        self.subs_frames = []

        for idx, subs in enumerate(self.settings['subjects']):
            self.timer_canvas.create_rectangle(25, 20+(120*idx), 425, 120+(120*idx))
            self.timer_canvas.config(scrollregion=(0, 0, 450, 140+(120*idx)))


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()