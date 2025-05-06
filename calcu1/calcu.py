
import tkinter as tk

def calcular():
    try:
        resultado = eval(pantalla.get())
        pantalla.delete(0, tk.END)
        pantalla.insert(0, resultado)
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear la pantalla
pantalla = tk.Entry(ventana,width=20, font=('Arial', 20))
pantalla.grid(row=0, column=0, columnspan=4)

# Crear los botones
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+', '(', ')'
]

fila = 1
columna = 0
for boton in botones:
    tk.Button(ventana, text=boton, width=5, height=2, command=lambda b=boton: pantalla.insert(tk.END, b)).grid(row=fila, column=columna)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1
# Botón para borrar
tk.Button(ventana, text='C', width=5, height=2, command=lambda: pantalla.delete(0, tk.END)).grid(row=fila, column=1, columnspan=4)

# Botón para calcular
tk.Button(ventana, text='=', width=5, height=2, command=calcular).grid(row=fila, column=3, columnspan=4)


ventana.mainloop()