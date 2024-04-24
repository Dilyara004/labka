import tkinter as tk
#dilyara_shaimerden
def increment_counter():
    global counter
    counter += 1
    label.config(text="Счетчик: " + str(counter))

def decrement_counter():
    global counter
    counter -= 1
    label.config(text="Счетчик: " + str(counter))

counter = 0

root = tk.Tk()
root.title("Реактивный счетчик")

label = tk.Label(root, text="Счетчик: " + str(counter))
label.pack(pady=10)

increment_button = tk.Button(root, text="Увеличить", command=increment_counter)
increment_button.pack(side=tk.LEFT, padx=10)

decrement_button = tk.Button(root, text="Уменьшить", command=decrement_counter)
decrement_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()
