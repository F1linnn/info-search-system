import tkinter as tk
from Controller.Controller import Controller


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x600")
    app = Controller(root)
    root.mainloop()


