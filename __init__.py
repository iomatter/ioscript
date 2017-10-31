import tkinter as tk
import tkinter.messagebox as m
import sys

class IOscriptError(Exception):
    pass

class Gui:
    def __init__(self):
        self.btnids = []
        self.entids = []
    def newButton(self, val, btnid, command=lambda:m.showinfo('title', 'message')):
       self.btnids.append(btnid)
       tkbtn = int(btnid) + 1
       self.btnids.append(tkbtn)
       self.btnids[tkbtn]=tk.Button(std.root, text=val, command=command).pack()
    def newTextField(self, que, lblid):
        self.entids.append(lblid)
        tkent = int(lblid) + 1
        self.entids.append(tkent)
        std.out(que)
        self.entids[tkent] = tk.Entry(std.root)
        self.entids[tkent].pack()
    def getFromTextField(self, entid):
        return self.entids[int(entid) + 1].get()
        
class Std:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("STDOUT")
        self.stdouttext = [""]
        self.gui = Gui()
        self.outstd = tk.Label(self.root, text=self.stdouttext)
        self.outstd.pack()
    def out(self, value):
        self.stdouttext.append(value + "\n")
        self.outstd.config(text=''.join(self.stdouttext))
    def start(self):
        self.root.mainloop()

std = Std()

# just a test

def __test__():
    std.out("Hello!")
    std.gui.newTextField("How are you?", "0")
    std.gui.newButton("I anwsered!", 0, command=lambda:m.showinfo("Nope.", std.gui.getFromTextField("0")))
    std.gui.newButton("I anwsered!", 1, command=lambda:m.showinfo("2", "Hello 2"))  
    std.start()
