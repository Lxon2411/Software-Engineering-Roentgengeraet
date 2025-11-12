import threading
import time

from src.config import MAX_DURATION

class RadiationController:
    def __init__(self, ui):
        self.ui = ui
        self.running = False
        self.thread = None

    def start(self, duration):
        if self.running:
            return
        self.running = True
        self.thread = threading.Thread(target=self._run_radiation, args=(duration,), daemon=True)
        self.thread.start()

    def _run_radiation(self, duration):
        for i in range(duration +1):
            if not self.running:
                break
            self.ui.update_progress(i, duration)
            time.sleep(1)
        self.running = False
        self.ui.reset_ui()

    def stop(self):
        self.running = False