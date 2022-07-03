# Code by bevatsal1122
# Trust God, Your Code will Work!!

# Alarm Clock & Stopwatch
# PP Semester_2 Project

import tkinter as gui
import datetime
import time
import winsound

class Clock:
    def __init__(self):
        self.window = gui.Tk()
        self.window.title("Alarm Clock")
        self.window.geometry("1100x650")
        self.window.resizable(False, False)

        self.hours = [
            00, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
            13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24
        ]
        self.minutes = [
            00, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
            13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
            25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
            49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60
        ]

        self.alarm_frame = self.create_alarm_frame()
        self.stopwatch_frame = self.create_stopwatch_frame()
        self.alarm_label = self.create_alarm_label()
        self.create_dropdowns()
        self.set_button = self.create_set_button()


    def create_alarm_frame(self):
        frame = gui.Frame(self.window, width=550)
        frame.pack(fill="both", side="left")
        frame.configure(bg="black")
        return frame

    def create_stopwatch_frame(self):
        frame =gui.Frame(self.window, width=550)
        frame.pack(fill="both", side="right")
        frame.configure(bg="darkgrey")
        return frame

    def create_alarm_label(self):
        label = gui.Label(self.alarm_frame, bg="black", fg="white",
                        font=("Arial", 20))
        label.pack(fill="both", side="top", pady=70)
        return label

    def create_dropdowns(self):
        self.hour_options = gui.StringVar()
        self.hour_options.set("Hours")
        dropdown0 = gui.OptionMenu(self.alarm_label, self.hour_options, *self.hours)
        dropdown0.pack(padx=45, side="left")
        dropdown0.configure(height=2, width=8, font=("Arial", 24, "bold"))
        
        self.minutes_options = gui.StringVar()
        self.minutes_options.set("Minutes")
        dropdown1 = gui.OptionMenu(self.alarm_label, self.minutes_options, *self.minutes)
        dropdown1.pack(padx=45, side="right")
        dropdown1.configure(height=2, width=8, font=("Arial", 24, "bold"))

    def create_set_button(self):
        button = gui.Button(self.alarm_frame, text="Set Alarm", bg="white", fg="black",
                        font=("Arial", 26, "bold"), command=self.alarm)
        button.pack(pady=10, side="top")
        button.config(width=22, height=1)
        return button

    def alarm(self):
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        while True:
            x = str(self.hour_options.get())
            y = str(self.minutes_options.get())
            if int(x) / 10 < 1:
                x = "0" + x
            if int(y) / 10 < 1:
                y = "0" + y
            set_alarm = f"{x}:{y}"
            time.sleep(1)
            current_time = datetime.datetime.now().strftime("%H:%M")
            print(current_time)
            print(set_alarm, "\n\n")
    
            if current_time == set_alarm:
                k = 0
                while k < 30:
                    k = k + 1
                    time.sleep(1.1)
                    winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
                break

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    play = Clock()
    play.run()
