import tkinter as tk
import json
from tkinter.constants import *
from datetime import datetime
import pytz

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
        self.start_img = tk.PhotoImage(file="assets/start.png")
        self.root.image = self.start_img
        self.pause_img = tk.PhotoImage(file="assets/pause.png")
        self.root.image = self.pause_img

        self.time = tk.StringVar(self.root, "00-00-0000 00:00 PM")
        self.timer_var = tk.StringVar(self.root, "00:00:00")

        self.clock = tk.Label(self.root, textvariable=self.time, font=Fonts._20, bg=Colors.primary, fg=Colors.text)
        self.clock.place(x=0, y=20, width=500, height=25)

        tk.Label(self.root, text="Total", font=Fonts._16, bg=Colors.primary, fg=Colors.text).place(x=232, y=65)

        self.grand_timer = tk.Label(self.root, textvariable=self.timer_var, font=Fonts._48, bg=Colors.primary, fg=Colors.text)
        self.grand_timer.place(x=0, y=100, width=500, height=55)

        self.tabs_frame = tk.Frame(self.root, width=450, height=500, borderwidth=0, highlightthickness=0)
        self.tabs_frame.place(x=25, y=165)
            
        self.timer_canvas = tk.Canvas(self.tabs_frame, bg=Colors.secondary, borderwidth=0, highlightthickness=0)

        vbar=tk.Scrollbar(self.timer_canvas, orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=self.timer_canvas.yview)

        self.timer_canvas.config(yscrollcommand=vbar.set)
        self.timer_canvas.place(x=0, y=0, width=450, height=500)

        self.subs_frames = []

        for idx, subs in enumerate(self.settings['subjects']):
            self.timer_canvas.create_rectangle(25, 20+(120*idx), 425, 120+(120*idx), fill=Colors.primary, width=0)
            self.timer_canvas.config(scrollregion=(0, 0, 450, 140+(120*idx)))

            self.timer_canvas.create_image((40, 35+(120*idx)), anchor="nw", image=self.start_img if subs['paused'] else self.pause_img)
            self.timer_canvas.create_text((110, 35+(120*idx)), anchor="nw", font=Fonts._16, text=subs['name'], fill=Colors.text)
            print(subs['time'])
            time = f"{str(subs['time']//3600).zfill(2)}:{str((subs['time']//60)%60).zfill(2)}:{str(subs['time']%60).zfill(2)}"
            self.timer_canvas.create_text((110, 55+(120*idx)), anchor="nw", font=Fonts._30, text=time, fill=Colors.text)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()