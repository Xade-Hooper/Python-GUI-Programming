"""A better Hello World for Tkinter"""
import tkinter as tk
from tkinter import ttk

class HelloView(tk.Frame):
    """A friendly liltle module"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.number_x = tk.StringVar()
        self.number_y = tk.StringVar()
        self.number_string = tk.StringVar()
        self.number_string.set("Put in dos whole numeros to get sum")
        self.name = tk.StringVar()
        self.hello_string = tk.StringVar()
        self.hello_string.set("Hello World")
        self.config(background='orange')

        name_label = ttk.Label(self, text="Name:")
        name_entry = ttk.Entry(self,textvariable=self.name)
        ch_button = ttk.Button(self, text="Change", command=self.on_change)
        hello_label = ttk.Label(self, textvariable=self.hello_string,
                               font=("TkDefaultFont", 64), wraplength=600)
        hello_label.config(background='orange')
        number_x_entry = ttk.Entry(self,textvariable=self.number_x)
        number_y_entry = ttk.Entry(self,textvariable=self.number_y)
        number_label = ttk.Label(self, textvariable=self.number_string,
                               font=("TkDefaultFont", 64), wraplength=600)
        n_sum_button = ttk.Button(self, text="mathplosion",command=self.math_it())
        #Layout form
        name_label.grid(row=0, column=0, sticky=tk.W)
        name_entry.grid(row=0,column=1,sticky=(tk.W + tk.E))
        ch_button.grid(row=0, column=2, sticky=tk.E)
        hello_label.grid(row=1, column=0, columnspan=3)
        #number_x_entry(row=0, column=1, sticky=tk.W)
        #number_y_entry(row=2, column=1, sticky=tk.W)
        number_label(row=2,column=0,columnspan=3)
        n_sum_button.grid(row=3,column=3, sticky=tk.E)

        self.columnconfigure(1, weight=1)

    def on_change(self):
        if self.name.get().strip():
            self.hello_string.set("Hello " + self.name.get())
        else:
            self.hello_string.set("Hello World")

    def math_it(self):
        if self.number_x.get() + self.number_y.get():
            sum = self.number_x.get() + self.number_y.get()
            self.number_string.set("And the answer is" + sum)


class MyApplication(tk.Tk):
    """Hello World Main Application"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.geometry("900x800")
        self.resizable(width=False, height=False)
        HelloView(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.config(background='orange')
        self.columnconfigure(0,weight=1)


if __name__=='__main__':
    app = MyApplication()
    app.mainloop()
