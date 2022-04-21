from difflib import SequenceMatcher
from tkinter import *
from tkinter.font import BOLD
import random
import time

class SpeedTest:
    def __init__(self, master):
        self.master = master #root
        self.time=0 ## self.end_time = self.start_time
        self.accurary = 0.0
        self.wpm = 0
        self.start_time = 0
        self.end_time = 0
        self.lbl_accuracy = None
        self.lbl_wpm = None
        self.lbl_tiem = None

        lbl_title = Label(self.master, text="Test Your Typing Speed", \
            font=("Arial", 25, BOLD), pady=20).grid(row=0, column=0, columnspan=2)
        self.lbl_text = Label(self.master, text = "this will be replaced.", \
            font=("Arial", 15), pady=10)
        self.lbl_text.grid(row=1, column=0, columnspan=2)

        self.txtbox = Text(self.master, height = 5, width = 80)
        self.txtbox.grid(row=2, column=0, columnspan=2, padx=20)

        with open("sentences.txt", "r") as f:
            self.text_list = f.readlines()
        
    def draw_text(self):
        self.lbl_text.config(text="")
        text = random.choice(self.text_list)
        self.lbl_text=Label(self.master, text = text, wraplength=500, \
            font=("Arial", 15), pady=10)
        self.lbl_text.grid(row=1, column=0, columnspan=2)

    def display_result(self, *arg):
        self.lbl_time = Label(self.master, text=f"Time: {self.time} sec",font=("Arial", 15))
        self.lbl_time.grid(row=4, column=0, columnspan=2)
        self.lbl_accuracy = Label(self.master, text=f"Accuraccy: {self.accurary} %",font=("Arial", 15))
        self.lbl_accuracy.grid(row=5, column=0, columnspan=2)
        self.lbl_wpm = Label(self.master, text=f"WPM: {self.wpm}",font=("Arial", 15))
        self.lbl_wpm.grid(row=6, column=0, columnspan=2)

    def start_timer(self, args):
        self.start_time = round(time.perf_counter(), 2)

    def check_accuracy(self, *args):
        self.end_time = round(time.perf_counter(), 2)
        self.time = round(self.end_time - self.start_time, 2) 
        entered_text = self.txtbox.get("1.0", END)
        ratio = SequenceMatcher(None, self.lbl_text.cget("text"), entered_text).ratio()
        self.accurary = round(ratio*100, 2) # SequenceMatcher(None, self.lbl_text.cget("text"), entered_text).ratio()
        self.wpm = round(len(entered_text.split())*60/self.time,2)
        self.display_result()        

    def clear_text(self, *args):
            self.txtbox.delete('1.0', END)
            self.lbl_time.config(text= "")
            self.lbl_accuracy.config(text= "")
            self.lbl_wpm.config(text= "")
            self.draw_text()            

    def start_game(self):
        self.txtbox.bind('<Button>', self.start_timer)
        self.txtbox.bind("<Return>", self.check_accuracy)
        btn_check = Button(root, text = "Check", command=self.check_accuracy, font = ('arial', 15))
        btn_check.grid(row = 3, column=0, pady=15)

        btn_clear = Button(root, text = "Clear", command=self.clear_text, font = ('arial', 15))
        btn_clear.grid(row = 3, column=1, pady=15)


if __name__ == "__main__":
    root = Tk()
    root.title("Typing Speed Test")
    root.iconbitmap("favicon.ico")
    root.geometry("700x520")
    
    game = SpeedTest(root)
    
    game.draw_text()
    game.start_game()
    root.mainloop()