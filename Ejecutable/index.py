from tkinter import ttk
from tkinter import *

class CovidDrawer:
    
    def __init__(self, window):
        self.wind = window
        self.wind.title('Graficador Casos Covid')
    
        frame = LabelFrame(self.wind, text = 'Menú', height=200, width=400)
        frame.grid(row = 0, column= 0, columnspan= 3, pady= 20)

        ttk.Button(frame, text= 'Opción 1').grid(row=3, columnspan=2, sticky=W+E)
        ttk.Button(frame, text= 'Opción 2').grid(row=4 ,columnspan=2, sticky=W+E)
        ttk.Button(frame, text= 'Opción 3').grid(row=5 ,columnspan=2, sticky=W+E)
        ttk.Button(frame, text= 'Opción 4').grid(row=6 ,columnspan=2, sticky=W+E)

        Label(frame, text='INFO OPCION 1').grid(row=3, column=2)
        Label(frame, text='INFO OPCION 2').grid(row=4, column=2)
        Label(frame, text='INFO OPCION 3').grid(row=5, column=2)
        Label(frame, text='INFO OPCION 4').grid(row=6, column=2)

if __name__ == '__main__':
    window = Tk()
    window.geometry("800x600")
    application = CovidDrawer(window)
    window.mainloop()