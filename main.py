# Code by bevatsal1122 (GitHub)
# Trust God, Your Code will Work

# Alarm Clock & Stopwatch

import tkinter as tk


class Clock:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Alarm Clock")
        self.window.geometry("1100x650")
        self.window.resizable(False, False)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    play = Clock()
    play.run()
