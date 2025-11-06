import tkinter as tk
from src.gui.ui import RadiationUI


def main():
    root = tk.Tk()
    app = RadiationUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
