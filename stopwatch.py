import tkinter as tk
from tkinter import ttk
import time

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("300x200")

        self.running = False
        self.time_elapsed = 0

        # Display label for the stopwatch time
        self.label = ttk.Label(self.root, text="00:00:00", font=("Arial", 40), background="lightgrey", anchor="center")
        self.label.pack(expand=True, fill='both')

        # Start, Pause, Reset buttons
        self.start_button = ttk.Button(self.root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.pause_button = ttk.Button(self.root, text="Pause", command=self.pause)
        self.pause_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.reset_button = ttk.Button(self.root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # Keep track of the start time
        self.start_time = 0

    def update_timer(self):
        if self.running:
            # Calculate time difference
            current_time = time.time()
            elapsed = current_time - self.start_time
            self.time_elapsed += elapsed
            self.start_time = current_time

            # Format time into minutes, seconds, and milliseconds
            minutes = int(self.time_elapsed // 60)
            seconds = int(self.time_elapsed % 60)
            milliseconds = int((self.time_elapsed * 100) % 100)

            # Update label to show the time
            self.label.config(text=f"{minutes:02}:{seconds:02}:{milliseconds:02}")

            # Keep updating every 50ms
            self.root.after(50, self.update_timer)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time()
            self.update_timer()

    def pause(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.time_elapsed = 0
        self.label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
