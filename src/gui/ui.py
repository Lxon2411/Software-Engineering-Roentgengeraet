import tkinter as tk
from tkinter import ttk, messagebox

class RadiationUI:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Röntgengerät Simulation")

        self.duration_label = tk.Label(root, text="Strahlungsdauer (Sekunden, max 120):")
        self.duration_label.pack(pady=5)

        self.duration_entry = tk.Entry(root, width=10)
        self.duration_entry.pack(pady=5)

        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)

        self.startButton = tk.Button(root, text="Start", command=self.start_radiation)
        self.startButton.pack(side="right", padx=20, pady=10)

    def start_radiation(self):
        try:
            duration=int(self.duration_entry.get())
            if not 1 <= duration <= 120:
                raise ValueError
            self.controller.start(duration)
            self.startButton.config(state=tk.DISABLED)
        except ValueError:
            messagebox.showerror("Fehler", "Bitte eine Zahl zwischen 1 und 120 eingeben!")


    def update_progress(self, value, max_value):
        self.progress["maximum"] = max_value
        self.progress["value"] = value
        self.root.update_idletasks()


    def reset_UI(self):
        self.startButton.config(state=tk.NORMAL)
        self.progress["value"] = 0

