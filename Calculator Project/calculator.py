import tkinter as tk
import math

# Ana Pencereyi Oluşturma
root = tk.Tk()
root.title("Calculator")
root.geometry("615x600")  # Pencere boyutunu arttırdık
root.config(bg="#1E3A5F")  # Arka plan rengini mavi tonlarında yapıyoruz

# Ekran  için bir alan oluşturduk burda
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=3, relief="solid", justify="right", bg="#ffffff", fg="#000000")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Geçmiş işlemler için...
history_label = tk.Label(root, text="İşlem Geçmişi", font=('Arial', 14), fg="#ffffff", bg="#1F6CA3", anchor='w')
history_label.grid(row=1, column=4, columnspan=2, padx=5, pady=10, sticky="n")

history_text = tk.Text(root, height=15, width=20, font=('Arial', 12), wrap=tk.WORD, bg="#4A90E2", fg="#ffffff", state=tk.DISABLED)
history_text.grid(row=2, column=4, rowspan=4, padx=5, pady=10, sticky="nsew")

def update_history(entry):
    history_text.config(state=tk.NORMAL)  
    history_text.insert(tk.END, entry + "\n")
    history_text.config(state=tk.DISABLED)  
    history_text.yview(tk.END) 


def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())  # Kullanıcının girdiği matematiksel ifadeyi işler
        update_history(f"{entry.get()} = {result}")  # İşlemi geçmişe ekler
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Hata")

def sqrt_func():
    try:
        result = math.sqrt(float(entry.get()))
        update_history(f"√{entry.get()} = {result}")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Hata")

def factorial():
    try:
        result = math.factorial(int(entry.get()))
        update_history(f"{entry.get()}! = {result}")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Hata")

def mod_func():
    try:
        current = entry.get().split('%')
        result = float(current[0]) % float(current[1])
        update_history(f"{current[0]} % {current[1]} = {result}")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Hata")

def trig_func(function):
    try:
        value = float(entry.get())
        if function == "sin":
            result = math.sin(math.radians(value))
        elif function == "cos":
            result = math.cos(math.radians(value))
        elif function == "tan":
            result = math.tan(math.radians(value))
        update_history(f"{function}({value}) = {result}")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Hata")

def log_func():
    try:
        value = float(entry.get())
        result = math.log(value)
        update_history(f"log({value}) = {result}")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Hata")

def exp_func():
    try:
        value = float(entry.get())
        result = math.exp(value)
        update_history(f"exp({value}) = {result}")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Hata")

# Sayı butonları ve İşlem Butonları
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row, col = 1, 0
for button in buttons:
    btn = tk.Button(root, text=button, font=('Arial', 20, 'bold'), fg="#ffffff", bg="#2A77A7", relief="flat", borderwidth=0, activebackground="#3C8DBC", command=lambda key=button: press(key) if key != "=" else calculate())
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew", ipadx=10, ipady=10)  # Daha geniş butonlar
    col += 1
    if col > 3:
        col = 0
        row += 1

functions = [
    ("√", sqrt_func),
    ("x!", factorial),
    ("%", mod_func),
    ("sin", lambda: trig_func("sin")),
    ("cos", lambda: trig_func("cos")),
    ("tan", lambda: trig_func("tan")),
    ("log", log_func),
    ("exp", exp_func)
]

row, col = row + 1, 0
for (text, func) in functions:
    btn = tk.Button(root, text=text, font=('Arial', 16, 'bold'), fg="#ffffff", bg="#1F6CA3", relief="flat", borderwidth=0, activebackground="#3C8DBC", command=func)
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew", ipadx=10, ipady=10) 
    col += 1
    if col > 3:
        col = 0
        row += 1

# C butonu
clear_button = tk.Button(root, text="C", font=('Arial', 20, 'bold'), fg="#ffffff", bg="#e53935", relief="flat", borderwidth=0, activebackground="#d32f2f", command=clear)
clear_button.grid(row=row, column=0, columnspan=4, padx=5, pady=10, sticky="nsew", ipadx=10, ipady=10)

# pencere boyutu büyüdükçe butonların da büyümesini sağlar
for i in range(6):  
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1) 
root.mainloop()
