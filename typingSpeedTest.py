from difflib import SequenceMatcher, Differ
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

        self.master.title("Typing Speed Test")
        self.master.iconbitmap("favicon.ico")
        self.master.geometry("700x520")

        lbl_title = Label(self.master, text="Test Your Typing Speed", \
            font=("Arial", 25, BOLD), pady=20).grid(row=0, column=0, columnspan=2)
        self.lbl_text = Label(self.master, text = "this will be replaced.", \
            font=("Arial", 15), pady=10)
        self.lbl_text.grid(row=1, column=0, columnspan=2)

        self.txtbox = Text(self.master, height = 5, width = 80)
        # self.txtbox = Text(self.master, height = 5, width = 80, command=self.check_letter)
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

        # self.diff = Label(self.master, font=('Arial', 11), text= self.diff, wraplength=550)
        # self.diff.grid(row=8, column=0, columnspan=2)

    def start_timer(self, args):
        self.start_time = round(time.perf_counter(), 2)

    def check_accuracy(self, *args):
        print(f"START TIME in check_accuracy 111111: {self.start_time}") 

        self.end_time = round(time.perf_counter(), 2)
        self.time = round(self.end_time - self.start_time, 2) 

        entered_text = self.txtbox.get("1.0", END)
        tested_text = self.lbl_text.cget("text")
        ratio = SequenceMatcher(None, tested_text, entered_text).ratio()
        self.accurary = round(ratio*100, 2) # SequenceMatcher(None, self.lbl_text.cget("text"), entered_text).ratio()

        self.wpm = round(len(entered_text.split())*60/self.time,2)

        d = Differ()
        diff = d.compare(tested_text, entered_text)

        # a = [l.strip() for l in list(diff) if l != '   ']
        # print(list(diff))
        # print(a)
        b = ''.join(list(diff))
        print(b)
        self.diff = b
        # print(type(b))

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

        btn_check = Button(self.master, text = "Check", command=self.check_accuracy, font = ('arial', 15))
        btn_check.grid(row = 3, column=0, pady=15)

        btn_clear = Button(self.master, text = "Clear", command=self.clear_text, font = ('arial', 15))
        btn_clear.grid(row = 3, column=1, pady=15)

def main():
    root = Tk()
    
    game = SpeedTest(root)
    
    game.draw_text()
    game.start_game()

    root.mainloop()

if __name__ == "__main__":
    main()