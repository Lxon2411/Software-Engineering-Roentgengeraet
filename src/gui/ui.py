import tkinter as tk
from tkinter import ttk, messagebox
import winsound

from src.config import MAX_DURATION


class RadiationUI:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root

        self.duration_label = tk.Label(root, text="Strahlungsdauer (Sekunden, max 120):")
        self.duration_label.pack(pady=5)

        self.duration_entry = tk.Entry(root, width=10)
        self.duration_entry.pack(pady=5)

        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)

        self.progress_label = tk.Label(root, text="Fortschritt: 0 %")
        self.progress_label.pack(pady=5)

        self.startButton = tk.Button(root, text="Start", command=self.start_radiation)
        self.startButton.pack(padx=20, pady=10)

    def start_radiation(self):
        try:
            duration = int(self.duration_entry.get())
            if not 1 <= duration <= MAX_DURATION:
                raise ValueError
            self.controller.start(duration)
            self.startButton.config(state=tk.DISABLED)
            self.root.focus_set()
        except ValueError:
            messagebox.showerror("Fehler", f"Bitte eine Zahl zwischen 1 und {MAX_DURATION} eingeben!")

    def update_progress(self, value, max_value):
        self.progress["maximum"] = max_value
        self.progress["value"] = value

        percent = (value/max_value) * 100 if max_value > 0 else 0
        self.progress_label.config(text=f"Fortschritt: {percent:.0f} %")

        self.root.update_idletasks()

    def reset_ui(self):
        self.startButton.config(state=tk.NORMAL)
        self.progress["value"] = 0
        self.duration_entry.delete(0, tk.END)
        self.progress_label.config(text=f"Fortschritt: 0 %")

    def show_finished_message(self, duration):
        winsound.Beep(400, 600)
        messagebox.showinfo("Fertig", f"Die Strahlung wurde erfolgreich nach {duration} Sekunden beendet.")


