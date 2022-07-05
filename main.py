# Alarm Clock & Stopwatch
# PP Semester_2 Project

import tkinter as gui
import datetime
import time
import pygame
from threading import *

class Clock:
    def __init__(self):
     
        self.window = gui.Tk()
        self.window.title("Alarm Clock & Stopwatch")
        self.window.geometry("1100x650")
        # self.window.resizable(False, False)

        self.hours = [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
            13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23
        ]
        self.minutes = [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
            13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
            25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
            49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59
        ]
        self.alarm_number = 0
        self.alarm_list = {}
        self.counter = 66600
        self.running = False


        self.alarm_frame = self.create_alarm_frame()
        self.stopwatch_frame = self.create_stopwatch_frame()
        self.show_clock_stopwatch_label = self.create_show_clock_stopwatch_label()
        self.show_stopwatch, self.start_stopwatch, self.stop_stopwatch, self.reset_stopwatch = self.create_clock_stopwatch_label()
        self.alarm_label = self.create_alarm_label()
        self.show_alarm_label = self.create_show_alarm_label()
        self.delete_alarm_label = self.create_delete_alarm_label()
        self.create_delete_material()
        self.create_dropdowns()
        self.set_button = self.create_set_button()
        pygame.mixer.init()
        
    def create_alarm_frame(self):
        frame = gui.Frame(self.window, width=550)
        frame.pack(fill="both", side="left")
        frame.configure(bg="black")
        return frame

    def create_stopwatch_frame(self):
        frame = gui.Frame(self.window, width=550)
        frame.pack(expand=True, fill="both", side="right")
        frame.configure(bg="darkgrey")
        return frame

    def create_show_clock_stopwatch_label(self):
        label = gui.Label(self.stopwatch_frame, bg="darkgrey", fg="black",
                        font=("Arial", 20))
        label.pack(fill="both", side="top", pady=50)
        return label

    def create_clock_stopwatch_label(self):
        label = gui.Label(self.show_clock_stopwatch_label, text="00:00:00", width=100, font=("Arial", 28))
        start = gui.Button(self.show_clock_stopwatch_label, text='Start', width=21, height=5,
                        font=("Arial", 10), command=self.start)
        stop = gui.Button(self.show_clock_stopwatch_label, text='Stop', width=21, height=5,
                        state='disabled',font=("Arial", 10), command=self.stop)
        reset = gui.Button(self.show_clock_stopwatch_label, text='Reset', width=21, height=5,
                        state='disabled', font=("Arial", 10), command=self.reset)
        label.pack()
        start.pack(side="left", pady=20, padx=2)
        stop.pack(side ="left")
        reset.pack(side="left", padx=2)
        return label, start, stop, reset

    def count(self):
        if self.running:
            if self.counter == 66600:			
                display = "Starting..."
            else:
                display = datetime.datetime.fromtimestamp(self.counter).strftime("%H:%M:%S")

            self.show_stopwatch.config(text=display)
            self.show_stopwatch.after(1000, self.count)
            self.counter += 1	
    
    def start(self):
        self.running = True
        self.count()
        self.start_stopwatch['state'] = 'disabled'
        self.stop_stopwatch['state'] = 'normal'
        self.reset_stopwatch['state'] = 'normal'

    def stop(self):
        self.start_stopwatch['state'] = 'normal'
        self.stop_stopwatch['state'] = 'disabled'
        self.reset_stopwatch['state'] = 'normal'
        self.running = False

    def reset(self):
        self.counter=66600
        if self.running==False:      
            self.reset_stopwatch['state'] = 'disabled'
            self.show_stopwatch.config(text = "00:00:00")
        else:               
            self.show_stopwatch.config(text = "Starting...")

    def create_alarm_label(self):
        label = gui.Label(self.alarm_frame, bg="black", fg="white",
                        font=("Arial", 20))
        label.pack(fill="both", side="top", pady=70)
        return label

    def create_show_alarm_label(self):
        label = gui.Label(self.alarm_frame, bg="black", fg="white",
                        font=("Arial", 20), text="Nothing to display")
        label.pack(fill="both", side="top")
        return label

    def create_delete_alarm_label(self):
        label = gui.Label(self.alarm_frame, bg="black", fg="white",
                        font=("Arial", 20), text="Delete Alarm")
        label.pack(fill="both", side="bottom", pady=10, padx=100)
        return label
    
    def delete_alarm(self):
        todelete = 'Alarm ' + self.iptext.get("1.0", "end-1c")
        if todelete in self.alarm_list:
            self.alarm_list.pop(todelete)
            self.update_show_alarm_label()

    def create_delete_material(self):
        self.iptext = gui.Text(self.delete_alarm_label, height = 1, width = 10)
        self.iptext.pack(side="left")
        deletebox = gui.Button(self.delete_alarm_label, height = 2,
                 width = 10,
                 text ="Delete",
                 command = self.delete_alarm)
        deletebox.pack(side="right")

    def update_show_alarm_label(self):
        texttoadd = ""
        for i in self.alarm_list:
            texttoadd += str(i) + "   " + self.alarm_list[i] + "\n"
        self.show_alarm_label.config(text=texttoadd)

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

    def threading(self):
        t1=Thread(target=self.alarm)
        t1.start()

    def create_set_button(self):
        button = gui.Button(self.alarm_frame, text="Set Alarm", bg="white", fg="black",
                        font=("Arial", 26, "bold"), command=self.threading)
        button.pack(pady=10, side="top")
        button.config(width=22, height=1)
        return button

    def alarm_executed(self, x):
        self.alarm_list.pop(x)
        self.update_show_alarm_label()
        time.sleep(9)
        self.alarm_number -= 1

    def alarm(self):
        if len(self.alarm_list) > 6:
            texttoadd = ""
            for i in self.alarm_list:
                texttoadd += str(i) + "   " + self.alarm_list[i] + "\n"
            texttoadd += "Maximum Limit Reached!!"
            self.show_alarm_label.config(text=texttoadd)
        else:
            x = str(self.hour_options.get())
            y = str(self.minutes_options.get())
            if int(x) / 10 < 1:
                x = "0" + x
            if int(y) / 10 < 1:
                y = "0" + y
            set_alarm = f"{x}:{y}"
            self.alarm_number += 1
            self.alarm_list["Alarm " + str(self.alarm_number)] = set_alarm
            self.update_show_alarm_label()
            while len(self.alarm_list)>=1:
                time.sleep(1)
                tod = False
                dele = ""
                current_time = datetime.datetime.now().strftime("%H:%M")
                for x, y in self.alarm_list.items():
                    if current_time == y:
                        pygame.mixer.music.load("alarm_tune.mp3")
                        pygame.mixer.music.play(loops=0)
                        time.sleep(30)
                        tod = True
                        dele = x
                        break
                if tod == True:
                    self.alarm_executed(dele)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    play = Clock()
    play.run()
