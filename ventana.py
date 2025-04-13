import tkinter as tk


ventana = tk.Tk()
ventana.title("Ventana basica")

def incrementNum():
    global numvar
    numvar += 1
    btn.config(text=str(numvar))

numvar = 1
btn = tk.Button(ventana, text=str(numvar), font=('Consolas 60'), command=incrementNum)
btn.pack(expand=True, fill=tk.BOTH)


ventana.geometry("300x150")
ventana.mainloop()