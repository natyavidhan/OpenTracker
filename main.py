import tkinter as tk
import tkinter.font as font

class App:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.geometry("500x800")
        self.root.resizable(False, False)
        self.root.configure(background="#262626")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()