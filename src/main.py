import tkinter as tk
from gui.ui import RadiationUI

from controller.controller import RadiationController
from tkinter import PhotoImage

def main():
    root = tk.Tk()
    root.title("Röntgengerät Simulation")
    root.geometry("500x550")
    root.resizable(False, False)

    icon = PhotoImage(file="icon.png")
    root.iconphoto(False, icon)

    ui = RadiationUI(root, None)
    controller = RadiationController(ui)
    ui.controller = controller
    root.mainloop()


if __name__ == "__main__":
    main()

