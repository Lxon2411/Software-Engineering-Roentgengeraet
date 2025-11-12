import tkinter as tk
from tkinter import PhotoImage

from src.gui.ui import RadiationUI
from src.controller.radiation_controller import RadiationController


def main():
    root = tk.Tk()
    controller = RadiationController(None)
    ui = RadiationUI(root, controller)
    controller.ui = ui
    root.title("Röntengerät Simulation")
    root.geometry("900x600")

    root.resizable(False, False)

    icon = PhotoImage(file="icon.png")
    root.iconphoto(False, icon)

    root.mainloop()


if __name__ == "__main__":
    main()
