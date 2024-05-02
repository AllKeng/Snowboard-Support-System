from __future__ import annotations
from threading import Thread, Lock
from bluetoothESP import scan_and_connect
import asyncio

import sys
import tkinter as tk
import tkinter.ttk as ttk
from threading import Thread, Lock
from tkinter.messagebox import showerror

def detached_callback(f):
    return lambda *args, **kwargs: Thread(target=f, args=args, kwargs=kwargs).start()

class ConsoleRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.config(state=tk.NORMAL)  
        self.text_widget.insert(tk.END, text)
        self.text_widget.see(tk.END)  
        self.text_widget.config(state=tk.DISABLED)

class App(tk.Tk):
    _lock: Lock = Lock()
    
    def __init__(self):
        super().__init__()
        
        self.title("Snowboard")
        self.geometry("800x600")
        self.calibration = []
        self.connectblue = tk.IntVar()

        self.output = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        self.checkButton = tk.Checkbutton(self, text="Connect to Bluetooth",  variable=self.connectblue, onvalue=1, offvalue=0,command=lambda : self.toggle_bluetooth(self.connectblue))
        self.checkButton.pack(side=tk.TOP, anchor=tk.E, padx=10, pady=10)
        ttk.Button(self, text='calibrate', command=self.update_calibration).pack(side=tk.TOP, anchor=tk.E, padx=10, pady=10)
        self.display = tk.Text(self, height=5, width=80, state=tk.DISABLED)
        self.console = tk.Text(self, height=10, width=80, state=tk.DISABLED)
        self.console.pack(side=tk.BOTTOM, fill="both", expand=True, anchor=tk.W,padx=50, pady=10)
        tk.Label(self, text="Console").pack(side=tk.BOTTOM, anchor=tk.W,padx=50)
        self.display.pack(side=tk.BOTTOM, anchor=tk.W,padx=50, pady=10)
        tk.Label(self, text="Display").pack(side=tk.BOTTOM, anchor=tk.W,padx=50)
        
        
        sys.stdout = ConsoleRedirector(self.console)


        
        #self.after(1000, self.update_output)
        #self.after(1000, self.update_text)
        self.mainloop()

    @detached_callback
    def update_calibration(self):
        with self._lock:
            popup_window = tk.Toplevel(self)
            popup_window.geometry("200x100")

            label = tk.Label(popup_window, text="This is a popup window")
            label.pack(pady=10)
    
            close_button = tk.Button(popup_window, text="Close", command=popup_window.destroy)
            close_button.pack()
            return
    
    
    @detached_callback
    def toggle_bluetooth(self, state):
        with self._lock:
            if self.connectblue.get()==1:
                print(f"Creating Scanner Instance...") 
                result = asyncio.run(scan_and_connect())
                if (result):
                    return
                else:
                    self.connectblue = 0
           
            
            else:
                self.disconnect_bluetooth() 
                print(f"Disconnected from Bluetooth Device") 
            
            return  
    
    @detached_callback
    def disconnect_bluetooth(self):
        with self._lock:
            return

    @detached_callback
    def update_text(self):
        with self._lock:
            self.display.config(state=tk.NORMAL)  
            self.display.delete("1.0", tk.END)  
            self.display.insert(tk.END, self.output)  
            self.display.config(state=tk.DISABLED)
            self.after(1000,self.update_text)  
    
    @detached_callback
    def update_output(self):
        with self._lock:
            print(self.output)
            self.after(1000,self.update_output)  
    
    
    def toString():
        return
        
if __name__ == "__main__":
    app = App()