import tkinter as tk


ventana = tk.Tk()
ventana.title("Ventana basica")

numvar = 1
btn = tk.Button(ventana, text=str(numvar), font=('Consolas 60'))
btn.pack(expand=True, fill=tk.BOTH)


ventana.geometry("200x300")
ventana.mainloop()