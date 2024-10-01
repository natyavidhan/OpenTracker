import tkinter as tk
from consts import Fonts
from consts import Colors

class App:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.geometry("500x800")
        self.root.resizable(False, False)
        self.root.configure(background=Colors.primary)

        self.time = tk.StringVar(self.root, "00-00-0000 00:00 PM")
        self.timer_var = tk.StringVar(self.root, "00:00:00")

        self.clock = tk.Label(self.root, textvariable=self.time, font=Fonts._20, bg=Colors.primary, fg=Colors.text)
        self.clock.place(x=0, y=20, width=500, height=25)

        tk.Label(self.root, text="Total", font=Fonts._16, bg=Colors.primary, fg=Colors.text).place(x=232, y=65)

        self.grandtimer = tk.Label(self.root, textvariable=self.timer_var, font=Fonts._48, bg=Colors.primary, fg=Colors.text)
        self.grandtimer.place(x=0, y=100, width=500, height=55)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()